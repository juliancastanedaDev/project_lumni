/*
Este script crea la base de datos y lass tablas para la casa de 
subastas, ejecutar codigo en mysql  $source <path del archivo>
*/


CREATE DATABASE IF NOT EXISTS casa_de_subastas;
USE casa_de_subastas;

/*Tabla de usuarios*/
CREATE TABLE IF NOT EXISTS user(
    id_user INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone INT NOT NULL,
    password VARCHAR(20),
    PRIMARY KEY (id_user));

/*tabla de articulos a subastar*/
CREATE TABLE IF NOT EXISTS article(
    id_article INT AUTO_INCREMENT NOT NULL,
    id_user INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    descripcion VARCHAR(200),
    PRIMARY KEY (id_article),
    FOREIGN KEY (id_user) REFERENCES user(id_user));

/*tabla de subasta*/
CREATE TABLE IF NOT EXISTS subasta(
    id_subasta INT AUTO_INCREMENT NOT NULL,
    id_article INT NOT NULL,
    name_articulo VARCHAR(50),
    fecha_inicial DATE,
    fecha_final DATE,
    precio_inicial INT NOT NULL,
    ofertas INT NOT NULL,
    precio_final INT NOT NULL,
    estado VARCHAR(20) NOT NULL,
    PRIMARY KEY (id_subasta),
    FOREIGN KEY (id_article) REFERENCES article(id_article));
    
/*tabla de fecha de entrega de articulos vendidos*/
CREATE TABLE If NOT EXISTS fecha_entrega(
    id_entrega INT AUTO_INCREMENT NOT NULL,
    id_subasta INT NOT NULL,
    fecha_entrega DATE,
    PRIMARY KEY (id_entrega),
    FOREIGN KEY (id_subasta) REFERENCES subasta(id_subasta));


