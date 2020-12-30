import json
import os
import mysql.connector

config = json.load(open("config.json"))

db = {}


def initialize():
    files = os.scandir('./models')
    db_ = mysql.connector.connect(
        host=config["database_host"],
        user=config["database_user"],
        password=config["database_password"])
    db_cursor = db_.cursor()
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS " + config["database_schema"])

    db_ = mysql.connector.connect(
        host=config["database_host"],
        user=config["database_user"],
        password=config["database_password"],
        database=config["database_schema"])
    db_cursor = db_.cursor()
    for file in files:
        if file.name != "index.py" and file.name != "__pycache__":
            data = json.load(open(file))
            data_string = ""
            for key, value in data.items():
                data_string += key + " " + value['type'] + " DEFAULT " + value['default'] + ", "
            db_cursor.execute("CREATE TABLE IF NOT EXISTS db_" + file.name[:-5] + " (id INT AUTO_INCREMENT PRIMARY "
                                                                                  "KEY, " + data_string[:-2] + ")")
    global db
    db = db_


def create(table_name, **kwargs):
    db_cursor = db.cursor()
    key_string = ""
    value_string = ""
    for key, value in kwargs.items():
        key_string += "" + key + ", "
        value_string += "'" + value + "', "
    create_string = "INSERT INTO db_" + table_name + " (" + key_string[:-2] + ") VALUES (" + value_string[:-2] + ");"
    db_cursor.execute(create_string)
    db.commit()


def read(table_name, **kwargs):
    db_cursor = db.cursor()
    columns = ""
    where = ""
    for key, value in kwargs.items():
        if key == "columns":
            columns = value
        if key == "where":
            where = value
    read_string = "SELECT " + columns + " FROM db_" + table_name
    if where != "":
        read_string += " WHERE " + where + ";"
    db_cursor.execute(read_string)
    return db_cursor.fetchall()


def update(table_name, **kwargs):
    db_cursor = db.cursor()
    update_string = "UPDATE db_" + table_name + " SET "
    where = ""
    for key, value in kwargs.items():
        if key != "where":
            update_string += key + " = '" + value + "', "
        else:
            where = value
    update_string = update_string[:-2] + " WHERE " + where + ";"
    db_cursor.execute(update_string)
    db.commit()


def delete(table_name, where):
    db_cursor = db.cursor()
    delete_string = "DELETE from db_" + table_name + " WHERE " + where
    db_cursor.execute(delete_string)
    db.commit()
