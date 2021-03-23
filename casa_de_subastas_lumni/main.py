#!/usr/bin/env python3

"""
        Este script inicializa programa casa de subastas
"""
import MySQLdb
import users
import subasta
import articulo

options = int(input('Ingres el numero de la opcion que desea \n 1- Iniciar sesión.\n 2- Registrarme.\n'))

if (options == 1):
        email = input('ingrese email\n')
        password = input('contraseña\n')
        if __name__ == "__main__":
                #Conceccion a base de datos
                conn = MySQLdb.connect(
                        host="localhost",
                        user="root",
                        password="Dev.1",
                        db="casa_de_subastas"
                
)
                cur = conn.cursor()
                cur.execute("SELECT * FROM user WHERE user.email=%s;",[email])
                query_rows = cur.fetchall()
                for row in query_rows:
                        if row[4] == password:
                                #Opciones ara usuarios registrados
                                options_user = int(input('1- Subastar\n2- Ofertar\n3- Registrar articulo para vender\n'))
                                if (options_user == 1):
                                        subasta.main()
                                elif (options_user == 2):
                                        print('Ofertar en construcción')
                                elif (options_user == 3):
                                        articulo.main()
                                else:
                                        print('Opcion invalida')        
                        else:
                                print('correo o contraseña incorrectos')        
                                      
                cur.close()
                conn.close()
elif (options == 2):
        users.main()
else:
        print('Opcion invalida')