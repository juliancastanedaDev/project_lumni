#!/usr/bin/env python3

import MySQLdb
import os
import users
from datetime import datetime


def main():
    name_articulo= input('name articulo\n')
    
    class Subasta:
        def __init__(self, fecha_inicial, fecha_final, precio_inicial):
            self.fecha_inicial = fecha_inicial
            self.fecha_final = fecha_final
            self.precio_inicial = precio_inicial
            
            

        def send_data_db(self,fecha_inicial, fecha_final, precio_inicial):
            connection = MySQLdb.connect(
            host="localhost",
            user="root",
            password="Dev.1",
            db="casa_de_subastas"
)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM article WHERE article.name=%s;",[name_articulo])
            query_rows = cursor.fetchall()
            for row in query_rows:
                cursor.execute("INSERT INTO subasta(id_article, name_articulo, fecha_inicial, fecha_final, precio_inicial, ofertas, precio_final, estado)\
                         VALUES(%s, %s, %s, %s, %s, 0, 0, 'Activo');",\
                         (row[0], row[1], fecha_inicial, fecha_final, precio_inicial))

            connection.commit()
            os.system ("cls")
            
    fecha_inicial = datetime.now()
    fecha_final=datetime.now()
    precio_inicial = int(input('Ingrese valor inicial de la subasta\n'))
    subasta = Subasta(fecha_inicial, fecha_final, precio_inicial)
    subasta.send_data_db(subasta.fecha_inicial, subasta.fecha_final, subasta.precio_inicial)

    if __name__ == "__main__":
        main()