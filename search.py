# column_index = input('Which column would you like to search on? ').capitalize()
# contact_search = input('Which item would you like to find? ').capitalize()
contact_search = 'Lungelo'


# if contact_details.loc[contact_details[column_index].isin([contact_search])].empty == False:
#     print(contact_details.loc[contact_details[column_index] == contact_search])
# else:
#     print(f'{column_index} does not exist')


all_contacts = 'select * from contacts;'

print(pd.read_sql_query(all_contacts,conn))