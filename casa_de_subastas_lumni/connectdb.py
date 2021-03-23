#!/usr/bin/env python3

import MySQLdb
from users.py import create_user

def __init__(self, id_user, name, email, phone, password):
       print ("{}{}{}{}".format(self, name, email, phone, password))

       connection = MySQLdb.connect(
       host="localhost",
       user="root",
       password="Dev.1",
       db="casa_de_subastas"
       )

       cursor = connection.cursor()
       
       sql = "INSERT INTO user(id_user, name, email, phone, password) VALUES(4, ?, ?, ?, ?)"

       cursor.execute(sql)

       connection.commit()
