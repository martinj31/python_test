import mysql.connector
import csv
import time 
from datetime import datetime, date

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test_python')
cursor = cnx.cursor()


with open('data/lieux.csv', newline='') as f:
    readerLieu = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for lieu in readerLieu:
        if lieu[1] == "departement" :
                    continue
        addLieu = ("INSERT INTO lieu "
                "(commune, departement, region) "
                "VALUES (%s, %s, %s)")
        dataLieu = (lieu[0], lieu[1], lieu[2])

        cursor.execute(addLieu, dataLieu)

        cnx.commit()

        

with open('data/people.csv', newline='') as f:
    readerPersonne = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for personne in readerPersonne: 
        if personne[0] == "prenom" :
                    continue
        
        addPersonne = ("INSERT INTO personne "
                      "(prenom, nom, dateNaissance, commune) "
                      "VALUES (%s, %s, %s, %s)")
        #dateNaissance = date.strftime(personne[2], '%Y-%m-%d')
        dataPersonne = (personne[0], personne[1], personne[2], personne[3])

        cursor.execute(addPersonne, dataPersonne)

        cnx.commit()

        
cursor.close()
cnx.close()