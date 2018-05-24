#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import minimalmodbus
import MySQLdb
import time
from settings import *


while True:

    print "Adresse de l'esclave: ", slave_addr
    time.sleep(1)
    print "Température: ", temperature,"°C"
    time.sleep(1)
    print "Débit: ", debit
    time.sleep(1)

    db = MySQLdb.connect("localhost","root","btsir123","ormeaux") # Query de connexion

    cursor = db.cursor()
    curseur = db.cursor()
    idcurs = db.cursor()

    query = ("SELECT valeurs FROM settings")
    
    sql = ("""INSERT INTO mesure(temp, debit, id_bassin) VALUES (%s, %s, %s)""") # Query SQL
    data = (temperature, debit, slave_addr)
    iD = ("SELECT id_mesure FROM mesure WHERE id_bassin=1 ORDER BY datetime DESC LIMIT 1")

    print "Query ok"
    try:
        cursor.execute(sql, data) # Execution de la query
        print "Connexion à la db"

        curseur.execute(query) 
        row = curseur.fetchone() # Resultat de la query 
        valeur = row[0] # Affichage de la première valeur du tableau

        idcurs.execute(iD)
        val = idcurs.fetchone()
        id_mes = val[0]        

        db.commit() 
        print "Envoi"

    except:
        db.rollback() # En cas d'erreur
        print "Erreur"

    db.close() # Fermeture de la connexion avec la base de donnees
    print "ID", id_mes+1
    print "sleep: ",valeur
    print "Déconnexion de la db"
    print "--------------------"
    print "                    "
    time.sleep(valeur)