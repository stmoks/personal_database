import pandas as pd
import pyodbc #seems important but haven't figured out where I'm going to use it yet - odbc is a db api
import sqlite3
import sqlalchemy

import database_connection

from sqlalchemy import create_engine
from sqlite3.dbapi2 import connect
from typing import final
from numpy import dtype, e, insert

from whatsapp_messages import WhatsappChat
from create_tables import CreateTable



database_name = input('Enter the database name: ')

if __name__ == '__main__':
    db_object = database_connection.Database()
    conn = db_object.create_connection(database_name)
    crsr = conn.cursor()

table_definition = CreateTable()
table_definition.create_table(conn)

# table_definition.create_table(conn,[['customer_id','integer','primary_key','not null']])

#todo do i need to index one of the columns below? Indexes make searching faster
contact_details = pd.read_excel('contact_details.xlsx',dtype={'cell_number':str},na_values='Missing',names=['first_name','last_name','cell_number','email_address','date_of_birth','occupation','education','gender','location','id_number'])

print(contact_details.head())



# column_index = input('Which column would you like to search on? ').capitalize()
# contact_search = input('Which item would you like to find? ').capitalize()
contact_search = 'Lungelo'



# if contact_details.loc[contact_details[column_index].isin([contact_search])].empty == False:
#     print(contact_details.loc[contact_details[column_index] == contact_search])
# else:
#     print(f'{column_index} does not exist')


#todo turn this into a function somehow
cols_contacts = ','.join([str(i) for i in contact_details.columns.tolist()])

insert_contacts = f'INSERT INTO contacts ({cols_contacts}) values(?,?,?,?,?,?,?,?,?,?)'

for index, row in contact_details.iterrows():
     crsr.execute(insert_contacts,tuple(row))

conn.commit()


# connect database to the Whatsapp messages
whatsapp_chat = WhatsappChat(input('Enter the name: '))
whatsapp_df = WhatsappChat(contact_search)


print(whatsapp_df)
cols = list(whatsapp_df.columns.values)

insert_chats = f'INSERT INTO whatsapp_chats ({cols}) values(?,?,?,?,?)'

for index, row in whatsapp_df.iterrows():
     crsr.execute(insert_chats,tuple(row))

conn.commit()

cols = ','.join([str(i) for i in contact_details.columns.tolist()])

insert_contacts = f'INSERT INTO contacts ({cols}) values(?,?,?,?,?,?,?,?,?,?)'

for index, row in contact_details.iterrows():
     crsr.execute(insert_contacts,tuple(row))

conn.commit()

# whatsapp_join = f'SELECT * FROM contacts a LEFT JOIN ... ON a.first_name = b.name'
# crsr.execute(whatsapp_join).fetchall()


#todo perform nlp on the whatsapp text


all_contacts = 'select * from contacts;'

print(pd.read_sql_query(all_contacts,conn))


#close the connection
conn.close()
