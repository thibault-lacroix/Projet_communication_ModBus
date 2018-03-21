#!/usr/bin/env python
import minimalmodbus
import MySQLdb
import time
minimalmodbus.BAUDRATE = 19200 #initialisation du baudrate
minimalmodbus.TIMEOUT = 5

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # Nom du port, adresse de l'esclave 

while True:
    #Register number, number of decimals, function code
    temperature = instrument.read_register(1, 2, 4)
    print "Temperature: ", temperature
    time.sleep(1)
    
    debit = instrument.read_register(0, 0, 4)
    print "Debit:", debit
    time.sleep(1)

    db = MySQLdb.connect("localhost","root","btsir123","ormeaux") #Query de connexion

    cursor = db.cursor()
    
    sql = ("""INSERT INTO capteur(capt_temp, capt_debit) VALUES (%s, %s)""") #Query SQL
    data = (temperature, debit)
    print "ok"
    try:
        cursor.execute(sql, data) #Execution de la query
        print "test"
        db.commit() 
        print "commit"

    except:
        db.rollback() #en cas d'erreur
        print "erreur"
    db.close() #fermeture de la connexion avec la base de donnees
    print "deconnecte"
    time.sleep(1)