#include <SimpleModbusSlave.h>
#include <OneWire.h>


/* Broche du bus 1-Wire */
const byte BROCHE_ONEWIRE = 7;

/* Code de retour de la fonction getTemperature() */
enum DS18B20_RCODES {
  READ_OK,  // Lecture ok
  NO_SENSOR_FOUND,  // Pas de capteur
  INVALID_ADDRESS,  // Adresse reçue invalide
  INVALID_SENSOR  // Capteur invalide (pas un DS18B20)
};

//////////////// registers of your slave ///////////////////
enum 
{     
  // just add or remove registers and your good to go...
  // The first register starts at address 0
  DEBIT,  
  TEMP,
  VANNE_STATE,
  DEBIT_STATE,
  TOTAL_ERRORS,
  // leave this one
  TOTAL_REGS_SIZE 
  // total number of registers for function 3 and 16 share the same register array
};

unsigned int holdingRegs[TOTAL_REGS_SIZE]; // function 3 and 16 register array
////////////////////////////////////////////////////////////


/* Création de l'objet OneWire pour manipuler le bus 1-Wire */
OneWire ds(BROCHE_ONEWIRE);

const int vanne = 8; //broche electrovanne
const int tpsvanne = 5000;

volatile int NbTopsFan; //measuring the rising edges of the signal
int Calc;
int hallsensor = 2; //capteur debit
float temperature;

void setup() {
  modbus_configure(19200, 1, 5, TOTAL_REGS_SIZE, 0);
  pinMode(vanne, OUTPUT);//la vanne en sortie
  pinMode(hallsensor, INPUT);//debit
  pinMode(temperature, INPUT);//temperature

    
  Serial.begin(9600);
  Serial.println("Démarrage du programme");
  attachInterrupt(0, rpm, RISING); //and the interrupt is attached
}

void loop() {
  // modbus_update() is the only method used in loop(). It returns the total error
  // count since the slave started. You don't have to use it but it's useful
  // for fault finding by the modbus master.
  holdingRegs[TOTAL_ERRORS] = modbus_update(holdingRegs);
  Serial.print("Erreurs : ");
  Serial.println( holdingRegs[TOTAL_ERRORS]);
  Serial.print("Electro State : ");
  Serial.println( holdingRegs[VANNE_STATE]);

  if (holdingRegs[VANNE_STATE]==1)
  {
    Serial.println("Electrovanne en marche");
    //digitalWrite(vanne, HIGH);
  }
  else if (holdingRegs[VANNE_STATE]==0)
  {
    Serial.println("Electrovanne a l'arret");
    //digitalWrite(vanne, LOW);
  }
  else
  {
    Serial.print ("Erreur electrovanne"); 
  }
  
  /*digitalWrite(vanne, HIGH);
  delay(tpsvanne);
  digitalWrite(vanne, LOW);
  delay(tpsvanne);*/
  /* Lit la température ambiante à ~1Hz */
  if (getTemperature(&temperature, true) != READ_OK) {
    Serial.println("erreur de lecture de température");
    return;
  }
  temperature = temperature * 100; //envoyer 4 chiffres au lieu de deux dans un int
  Serial.print("Température:");
  Serial.println(temperature);

  NbTopsFan = 0; //Set NbTops to 0 ready for calculations
  //sei(); //Enables interrupts
    delay (1000); //Wait 1 second
  //cli(); //Disable interrupts
  Calc = (NbTopsFan * 60 / 7.5); //(Pulse frequency x 60) / 7.5Q, = flow rate
  Serial.print("Débit: ");
  Serial.println(Calc);
  
   holdingRegs[DEBIT]=Calc;
   holdingRegs[TEMP]=temperature;   
  //uint16_t au16data[2] = {Calc, temperature};
}

/**
   Fonction de lecture de la température via un capteur DS18B20.
*/
byte getTemperature(float *temperature, byte reset_search) {
  byte data[9], addr[8];
  // data[] : Données lues depuis le scratchpad
  // addr[] : Adresse du module 1-Wire détecté

  /* Reset le bus 1-Wire ci nécessaire (requis pour la lecture du premier capteur) */
  if (reset_search) {
    ds.reset_search();
  }

  /* Recherche le prochain capteur 1-Wire disponible */
  if (!ds.search(addr)) {
    // Pas de capteur
    return NO_SENSOR_FOUND;
  }

  /* Vérifie que l'adresse a été correctement reçue */
  if (OneWire::crc8(addr, 7) != addr[7]) {
    // Adresse invalide
    return INVALID_ADDRESS;
  }

  /* Vérifie qu'il s'agit bien d'un DS18B20 */
  if (addr[0] != 0x28) {
    // Mauvais type de capteur
    return INVALID_SENSOR;
  }

  /* Reset le bus 1-Wire et sélectionne le capteur */
  ds.reset();
  ds.select(addr);

  /* Lance une prise de mesure de température et attend la fin de la mesure */
  ds.write(0x44, 1);
  delay(800);

  /* Reset le bus 1-Wire, sélectionne le capteur et envoie une demande de lecture du scratchpad */
  ds.reset();
  ds.select(addr);
  ds.write(0xBE);

  /* Lecture du scratchpad */
  for (byte i = 0; i < 9; i++) {
    data[i] = ds.read();
  }

  /* Calcul de la température en degré Celsius */
  *temperature = (int16_t) ((data[1] << 8) | data[0]) * 0.0625;

  // Pas d'erreur
  return READ_OK;
}

void rpm () //This is the function that the interupt calls
{
  NbTopsFan++; //This function measures the rising and falling edge of the

}
