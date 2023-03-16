#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE KOHLER
         (Name CHAR(20) PRIMARY KEY     NOT NULL);''')
print ("Table created successfully")


conn.execute("INSERT INTO COMPANY (NAME) VALUES ('Paul')")

conn.execute("INSERT INTO COMPANY (NAME) VALUES ('Allen')")

conn.execute("INSERT INTO COMPANY (NAME) VALUES ('Teddy')")

conn.execute("INSERT INTO COMPANY (NAME) VALUES ('Mark')")

conn.commit()
print ("Records created successfully")
conn.close()
