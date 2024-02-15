Bienvenido a la prueba de Backend en python para Banpay.

Este proyecto utiliza Python 3.11
Para poder levantar el proyecto es necesario la creacion de un entorno virtual e instalacion de sus dependencias.
Puedes instalar todas las dependencias por medio del archivo requirements.txt de la siguiente manera:

 --  pip install -r requirements.txt


 ---Uso de alembic futuro a implementarse---
Tambien deberas crear una base de datos y una tabla con el siguiente comando:

-- Table: public.users

-- DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    id integer NOT NULL,
    name character varying(255) COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    role character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT users_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;


Asegurate de modificar las variables de entorno en el archivo .env para la conexion a tu base de datos:


Para correr el proyecto solo teclea el siguiente comando en la consola:
--  uvicorn main:app --reload

Una vez que la aplicacion se haya iniciado dirigete a tu navegador e ingresa la siguiente direccion para poder visualizar el swagger:

http://127.0.0.1:8000/docs#/


