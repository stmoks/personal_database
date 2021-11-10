import sqlite3


import database_connection
from create_tables import CreateTable



database_name = input('Enter the database name: ')

if __name__ == '__main__':
    db_object = database_connection.Database()
    conn = db_object.create_connection(database_name)
    crsr = conn.cursor()

table_definition = CreateTable()
table_definition.create_table(conn)

# table_definition.create_table(conn,[['customer_id','integer','primary_key','not null']])



class Database:
    def __init__(self):
        self.connection = None
        
    def create_connection(self,database_name = ':memory:'): 
        '''create a database connection to a database that will reside in memory'''
        self.database_name = database_name
        try:
            self.connection = sqlite3.connect(self.database_name)
            print('Connected to the database')
            return self.connection
        except sqlite3.Error as e:
            return print(e)
 

#close the connection
conn.close()
