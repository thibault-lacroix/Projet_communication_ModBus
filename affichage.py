#!/usr/bin/env python
# coding: utf-8

print "Content-type: text/html\n\n"
import MySQLdb




db = MySQLdb.connect("127.0.0.1","root","btsir123","ormeaux")

cursor = db.cursor()
sql = "SELECT temp FROM mesure WHERE id_bassin=1 ORDER BY datetime DESC LIMIT 1 "

cursor.execute(sql)
row = cursor.fetchone()
print"Temperature: ",row, sql

db.close()
