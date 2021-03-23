#!/usr/bin/env python3

import MySQLdb

def main():
    email= input('email\n')
    class Article:
        """
            funcion crea articulo a subastar
        """
        def __init__(self, name, description):
            self.name = name 
            self.description = description

        def create_article(self, name, description):
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
                cur.execute("INSERT INTO article(name, descripcion, id_user) VALUES(%s, %s, %s);", (name, description, row[0]))

            conn.commit()

    article= Article(input('nombre\n'), input('description\n'))
    article.create_article(article.name, article.description)

    if __name__ == "__main__":
            main()