from sqlite3.dbapi2 import connect
from numpy import dtype
import pandas as pd
import sqlite3
import sqlalchemy

# connecting to a databse
# connection = sqlite3.connect('contacts.db')
# crsr = connection.cursor()

# print('Connected to the database')
# #close the connection

# contacts_table = '''CREATE TABLE contacts (
#     contact_id integer primary key,
#     first_name varchar(250),
#     last_name varchar(250),
#     cell_number char(30)
#     date_of_birth date,
#     occupation char(200),
#     education char(200),
#     gender enum (male, female,other),
#     location char(100),
#     id_number char(30)
# )'''

# crsr.execute(contacts_table).fetchall()

# all_contacts = 'select * from contacts;'

# pd.read_sql_query(all_contacts,connection)

# connection.close()


contact_details = pd.read_excel('contact_details.xlsx',dtype={'Cell number':str},na_values='Missing')

# print(contact_details.head())


column_index = input('Which column would you like to search on? ').capitalize()
contact_search = input('Which item would you like to find? ').capitalize()



if contact_details.loc[contact_details[column_index].isin([contact_search])].empty == False:
    print(contact_details.loc[contact_details[column_index] == contact_search])
else:
    print(f'{column_index} does not exist')



