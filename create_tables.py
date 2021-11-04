import sqlite3

class CreateTable():
    def __init__(self):
        pass

    def create_table(self,connection):
        self.connection = connection
        self.crsr = self.connection.cursor()
       
        drop_table = 'drop table if exists contacts;'
        self.crsr.execute(drop_table)
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
        self.crsr.execute(contacts_table).fetchall()

        drop_table = 'drop table if exists whatsapp_chats;'
        self.crsr.execute(drop_table)
        whatsapp_chats = '''CREATE TABLE whatsapp_chats (
            date date not null,
            day varchar(9) not null,
            time varchar(5) not null,
            author varchar(250) not null,
            message varchar(1000) not null
        )'''
        self.crsr.execute(whatsapp_chats).fetchall()
        

        #todo figure out how to turn my WhatsappChat object into a dataframe