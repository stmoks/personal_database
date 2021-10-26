import sqlite3

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
 
