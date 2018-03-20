#!/usr/bin/env python
import minimalmodbus
import MySQLdb
import time
minimalmodbus.BAUDRATE = 19200 #initialisation du baudrate
minimalmodbus.TIMEOUT = 1.5

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # Nom du port, adresse de l'esclave 

while True:
    #Register number, number of decimals, function code
    #temperature = instrument.read_register(1, 2, 4)
    #print "Temperature: ", temperature
    
    debit = instrument.read_register(0, 0, 4)
    print "Debit:", debit
    time.sleep(1)

    #Query de connexion
    db = MySQLdb.connect("localhost","root","btsir123","ormeaux") 

    cursor = db.cursor()
    #Query SQL
    sql = ("""INSERT INTO capteur(capt_temp, capt_debit) VALUES (%s, %s)""") 
    data = (5, debit)
    print "ok"
    try:
        #Execution de la query
        cursor.execute(sql, data) 
        print "test"
        db.commit() 
        print "commit"

    except:
        #en cas d'erreur
        db.rollback() 
        print "erreur"
    #fermeture de la connexion avec la base de donnees
    db.close()
    print "deconnecte"