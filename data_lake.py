# streaming data + batch data
# security - hashing + salting of sensitive data
# apis - events, food and drink,geocoding,jobs,music,open data,shopping,social,weather


import pandas as pd




#todo do i need to index one of the columns below? Indexes make searching faster
contact_details = pd.read_excel('contact_details.xlsx',dtype={'cell_number':str},na_values='Missing',names=['first_name','last_name','cell_number','email_address','date_of_birth','occupation','education','gender','location','id_number'])

