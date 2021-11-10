#todo turn this into a function somehow
cols_contacts = ','.join([str(i) for i in contact_details.columns.tolist()])

insert_contacts = f'INSERT INTO contacts ({cols_contacts}) values(?,?,?,?,?,?,?,?,?,?)'

for index, row in contact_details.iterrows():
     crsr.execute(insert_contacts,tuple(row))

conn.commit()



insert_chats = f'INSERT INTO whatsapp_chats ({cols}) values(?,?,?,?,?)'

for index, row in whatsapp_df.iterrows():
     crsr.execute(insert_chats,tuple(row))

conn.commit()



cols = ','.join([str(i) for i in contact_details.columns.tolist()])

insert_contacts = f'INSERT INTO contacts ({cols}) values(?,?,?,?,?,?,?,?,?,?)'

for index, row in contact_details.iterrows():
     crsr.execute(insert_contacts,tuple(row))

conn.commit()