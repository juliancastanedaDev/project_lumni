#!/usr/bin/env python3

import MySQLdb
import os

def main():
    class User:
        def __init__(self, name, email, phone, password):
            self.name = name 
            self.email = email
            self.phone = phone
            self.password = password

        def send_data_db(self, name, email, phone, password):
            connection = MySQLdb.connect(
            host="localhost",
            user="root",
            password="Dev.1",
            db="casa_de_subastas"
)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO user(name, email, phone, password) VALUES(%s, %s, %s, %s);", (name, email, phone, password))

            connection.commit()
            os.system ("cls")
            print('\n\n!REGISTRO EXITOSO¡\n\n\n')

    user = User(input('nombre \n'), input('email \n'),int(input('phone\n')), input('password \n'))
    user.send_data_db(user.name, user.email, user.phone, user.password)


    if __name__ == "__main__":
        main()