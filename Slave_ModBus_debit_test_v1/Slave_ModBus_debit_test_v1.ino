/**
 *  Modbus slave example 1:
 *  The purpose of this example is to link a data array
 *  from the Arduino to an external device.
 *
 *  Recommended Modbus Master: QModbus
 *  http://qmodbus.sourceforge.net/
 */
#include <ModbusRtu.h>

volatile int NbTopsFan; //measuring the rising edges of the signal
int Calc;
int hallsensor = 2; //The pin location of the sensor

void rpm () //This is the function that the interupt calls
{
NbTopsFan++; //This function measures the rising and falling edge of the

}

// data array for modbus network sharing
//uint16_t au16data[3] = {2, 4, 5};

/**
 *  Modbus object declaration
 *  u8id : node id = 0 for master, = 1..247 for slave
 *  u8serno : serial port (use 0 for Serial)
 *  u8txenpin : 0 for RS-232 and USB-FTDI 
 *               or any pin number > 1 for RS-485
 */
Modbus slave(1,1,5); // this is slave @1 and RS-232 or USB-FTDI

void setup() {
slave.begin( 19200 ); // baud-rate at 19200
pinMode(hallsensor, INPUT); //initializes digital pin 2 as an input
Serial.begin(9600); //This is the setup function where the serial port is

attachInterrupt(0, rpm, RISING); //and the interrupt is attached
  
}

void loop() {
NbTopsFan = 0; //Set NbTops to 0 ready for calculations

delay (1000); //Wait 1 second

Calc = (NbTopsFan * 60 / 7.5); //(Pulse frequency x 60) / 7.5Q, = flow rate
Serial.print (Calc, DEC);
Serial.print ("L/Heure\r\n");
//uint16_t au16data[1] = Calc;

slave.poll( Calc, 1 );
Serial.print ("envoye");
}
