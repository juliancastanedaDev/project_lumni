#!/usr/bin/env python3

import MySQLdb
import os
import users
from datetime import datetime


def main():
    name_articulo= input('name articulo\n')
    
    class Entrega:
        def __init__(self, fecha_entrega):
            self.fecha_entrega = fecha_entrega
            
            

        def send_data_db(self, fecha_entrega):
            connection = MySQLdb.connect(
            host="localhost",
            user="root",
            password="Dev.1",
            db="casa_de_subastas"
)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM subasta WHERE subasta.name_articulo=%s;",[name_articulo])
            query_rows = cursor.fetchall()
            for row in query_rows:
                cursor.execute("INSERT INTO subasta(id_subasta, fecha_entrega)\
                         VALUES(%s, %s,);",\
                         (row[1], fecha_entrega))

            connection.commit()
            os.system ("cls")
            
    fecha_entrega = datetime.now()
    entrega = Entrega(fecha_entrega)
    entrega.send_data_db(entrega.fecha_entrega)

    if __name__ == "__main__":
        main()