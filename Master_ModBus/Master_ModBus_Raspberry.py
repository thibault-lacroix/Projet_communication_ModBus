#!/usr/bin/env python
# coding: utf-8
import minimalmodbus
import MySQLdb
import time

minimalmodbus.BAUDRATE = 19200 # Initialisation du baudrate
minimalmodbus.TIMEOUT = 60
slave_addr = 1

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', slave_addr) # Nom du port, adresse de l'esclave

while True:

    print "Adresse de l'esclave: ", slave_addr
    
    temperature = instrument.read_register(1, 2) # Donnée dans le tableau, nombre de décimales
    print "Température: ", temperature,"°C"
    time.sleep(1)
    
    debit = instrument.read_register(0, 0)
    print "Débit: ", debit
    time.sleep(1)

    db = MySQLdb.connect("localhost","root","btsir123","ormeaux") # Query de connexion

    cursor = db.cursor()
    curseur = db.cursor()

    query = ("SELECT valeurs FROM settings")

    
    sql = ("""INSERT INTO mesure(temp, debit, id_bassin) VALUES (%s, %s, %s)""") # Query SQL
    data = (temperature, debit, slave_addr)
    print "Query ok"
    try:
        cursor.execute(sql, data) # Execution de la query
        print "Connexion à la db"

        curseur.execute(query) 
        row = curseur.fetchone() # Resultat de la query 
        valeur = row[0] # Affichage de la première valeur du tableau

        db.commit() 
        print "Envoi"

    except:
        db.rollback() # En cas d'erreur
        print "Erreur"

    db.close() # Fermeture de la connexion avec la base de donnees
    print "sleep: ",valeur
    print "Déconnexion de la db"
    print "--------------------"
    print "                    "
    time.sleep(valeur-9)