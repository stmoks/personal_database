import pandas as pd
import pyodbc #seems important but haven't figured out where I'm going to use it yet
import sqlite3
import sqlalchemy

import database_connection

from sqlalchemy import create_engine
from sqlite3.dbapi2 import connect
from typing import final
from numpy import dtype, e, insert

from whatsapp_messages import Whatsapp_Chat



database_name = input('Enter the database name: ')

if __name__ == '__main__':
    db_object = database_connection.Database()
    conn = db_object.create_connection(database_name)
    crsr = conn.cursor()

drop_table = 'drop table if exists contacts;'

crsr.execute(drop_table)

contacts_table = '''CREATE TABLE contacts (
    contact_id integer primary key,
    first_name varchar(250) not null,
    last_name varchar(250) not null,
    cell_number char(30) null,
    email_address char(50) null,
    date_of_birth date not null,
    occupation char(200) null,
    education char(200) null,
    gender char check(gender in ('male', 'female','other')) not null,
    location char(100) not null,
    id_number char(30) null
)'''

crsr.execute(contacts_table).fetchall()


contact_details = pd.read_excel('contact_details.xlsx',dtype={'cell_number':str},na_values='Missing',names=['first_name','last_name','cell_number','email_address','date_of_birth','occupation','education','gender','location','id_number'])

print(contact_details.head())



# column_index = input('Which column would you like to search on? ').capitalize()
# contact_search = input('Which item would you like to find? ').capitalize()



# if contact_details.loc[contact_details[column_index].isin([contact_search])].empty == False:
#     print(contact_details.loc[contact_details[column_index] == contact_search])
# else:
#     print(f'{column_index} does not exist')


cols = ','.join([str(i) for i in contact_details.columns.tolist()])

insert_contacts = f'INSERT INTO contacts ({cols}) values(?,?,?,?,?,?,?,?,?,?)'

for index, row in contact_details.iterrows():
     crsr.execute(insert_contacts,tuple(row))

conn.commit()


# connect database to the Whatsapp messages
whatsapp_chat = Whatsapp_Chat(input('Enter the name: '))
whatsapp_join = 'SELECT * FROM contacts a LEFT JOIN ... ON a.first_name = b.name'
crsr.execute(whatsapp_join).fetchall()


# perform nlp on the whatsapp text




all_contacts = 'select * from contacts;'

print(crsr.execute(all_contacts).fetchone())

pd.read_sql_query(all_contacts,conn)


#close the connection
conn.close()
