#!/usr/bin/env python
# coding: utf-8
import MySQLdb
import cgi, cgitb

print "Content-type: text/html; charset=UTF-8\n\n"
print

print'<html><head><title>PAGE TEST</title></head>'


db = MySQLdb.connect("127.0.0.1","root","btsir123","ormeaux")

cursor = db.cursor()
sql = "SELECT id_bassin, temp, debit, datetime FROM mesure WHERE id_bassin=1 ORDER BY datetime DESC LIMIT 1 "

cursor.execute(sql)
row = cursor.fetchone()
nbass = row[0]
tempe = row[1]
debit = row[2]
heure = row[3]

print"Numéro du bassin: ",nbass
print"//-//"
print"Température: ",tempe
print"//-//"
print"Débit: ",debit
print"//-//"
print"Date/Heure de la mesure: ",heure
db.close()
