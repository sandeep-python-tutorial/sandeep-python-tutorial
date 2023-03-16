#!/usr/bin/python

import sqlite3
from sqlite3 import IntegrityError

class Model(object):
    def __init__(self, DB_Name, TABLE_NAME, TABLE_VALUES):
        self.db_name = DB_Name
        self.table_name = TABLE_NAME
        self.table_value = TABLE_VALUES
        try:
            print("Connecting the Database: %s" % self.db_name)
            self.conn = sqlite3.connect(self.db_name)
            print ("Opened database successfully: %s" % self.db_name)
        except Exception as ex:
            raise Exception("Failed to connect Database: %s" % self.db_name)

    def create_table(self):
        try:
            print("Creating new table: %s" % self.table_name)
            self.conn.execute('''CREATE TABLE %s
                 (%s CHAR(50) PRIMARY KEY     NOT NULL);''' % (self.table_name, self.table_value))
            print ("Table created successfully: %s" % self.table_name)
        except:
            print("%s table Present in Database: %s" % (self.table_name,self.db_name))


    def insert_data_in_table(self, value):
        try:
            print("Inserting the Value %s in table %s" %(value, self.table_name))
            self.conn.execute("INSERT INTO %s (%s) VALUES ('%s')" % (self.table_name, self.table_value, value))
            self.conn.commit()
            print ("Records created successfully")
            return True
        except IntegrityError:
            print("%s value present in table %s" % (value, self.table_name))
            return False
        except Exception as ex:
            raise Exception("Failed to add value %s in table %s/n %s" % (value, self.table_name, ex))
