#!/usr/bin/env python
# coding: utf-8
import minimalmodbus
import MySQLdb
import time

minimalmodbus.BAUDRATE = 19200 # Initialisation du baudrate
minimalmodbus.TIMEOUT = 60

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # Nom du port, adresse de l'esclave 

while True:
    temperature = instrument.read_register(1, 2) # Donnée dans le tableau, nombre de décimales
    print "Température: ", temperature,"°C"
    time.sleep(1)
    
    debit = instrument.read_register(0, 0)
    print "Débit: ", debit
    time.sleep(1)

    e_vanne = instrument.read(2,0)
    print "Etat de la vanne: ", e_vanne
    time.sleep(1)

    db = MySQLdb.connect("localhost","root","btsir123","ormeaux") # Query de connexion

    cursor = db.cursor()
    
    sql = ("""INSERT INTO capteur(capt_temp, capt_debit) VALUES (%s, %s)""") # Query SQL
    data = (temperature, debit)
    print "Query ok"
    try:
        cursor.execute(sql, data) # Execution de la query
        print "Connexion à la db"
        db.commit() 
        print "Envoi"

    except:
        db.rollback() # En cas d'erreur
        print "Erreur"
    db.close() # Fermeture de la connexion avec la base de donnees
    print "Déconnexion de la db"
    print "--------------------"
    print "                    "
    time.sleep(10)
