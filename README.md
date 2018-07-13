#   PROJET ORMEAUZEN

###################################################################################################################################
# ModBus RS 485
Permet la communication ModBus entre deux module RS 485, un Max485 du côté Arduino Mega, et un module UNITEK Y-1082 USB RS485 RS422 
du côté Raspberry pi 3b.


# Rasperry
Le driver de de la Raspberry envoie des requêtes Modbus à l'Arduino regulièrement pour lui demander les valeurs des capteurs (requêtes de lecture).
Les valeurs reçues, elles sont envoyées dans un base de données.
Deux autres programmes permettent de changer le débit souhaité, et de contrôler l'éléctrovanne depuis la Raspberry (requêtes d'écriture).


# Arduino
Le programme de l'Arduino permet de faire des prises régulières de données sur des capteurs, de température, et de débit. 
Ces données sont stockées dans des variables (DEBIT,TEMP). Celles-ci sont envoyées à chaque requêtes de la Raspberry.
La reception des données des requêtes d'écriture stocke les valeurs reçues dans des variables d'état (VANNE_STATE,DEBIT_STATE).


###################################################################################################################################
PROJET DE BTS SN IR 2eme ANNÉE 2018
LA CROIX ROUGE LA SALLE BREST
