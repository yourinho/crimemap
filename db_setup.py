import pymysql
# This file will be stored on our local machine (we don't want store it in our repo).
import dbconfig
# Representation of a socket with a mysql server: https://pymysql.readthedocs.io/en/latest/modules/connections.html
connection = pymysql.connect(host='localhost',
                             user=dbconfig.db_user,
                             passwd=dbconfig.db_password)

try:
        # Cursor is the object we use to interact with the database.
        # Cursor is an object that points to a place in the db where we want to CRUD data.
        with connection.cursor() as cursor:
            sql = "CREATE DATABASE IF NOT EXISTS crimemap"
            cursor.execute(sql)
            sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
            id int NOT NULL AUTO_INCREMENT,
            latitude FLOAT(10, 6),
            longitude FLOAT(10, 6),
            date DATETIME,
            category VARCHAR(50),
            description VARCHAR(1000),
            updated_at TIMESTAMP,
            PRIMARY KEY (id)
            )"""
            cursor.execute(sql);
        connection.commit()
finally:
    connection.close()
