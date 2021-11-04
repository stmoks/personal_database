import re, pandas as pd
from datetime import datetime
# create messages object
# import txt file
# transform the text data
# link the whatsapp messages with the contacts db
# employ nlp (see script) to get a sense of conversations
# create database with all the words used + number of times and use that for the search of topics/sentiment on the front end
# make use of matplot to draw cool things - timelines
# write a story - nlp + other tools to make the chats sing (include the Google translate to speech that chats through the conversation)

# improvements to IO
# - use datatable, dask, vaex or cuDF
# - read the pandas doc

import re

class WhatsappChat:
    def __init__(self,name):
        self.name = name
        self.load_chats(self.name)

    def load_chats(self, name):
        with open(f'{name}.txt',encoding='utf8') as file:
            text_messages = file.readlines()[1:]
        self.transform_chats(text_messages)

    def transform_chats(self, messages):
        '''Transforms the plain text into data that is displayed in a Pandas data frame'''
        for line in messages:
            try:
                date = re.search(r'\d{4}/\d{2}/\d{2}',line).group()
                date = datetime.strptime(date,'%Y/%m/%d')
                day = datetime.strftime(date,'%A')
                time = re.search(r'\d{2}:\d{2}',line).group()
                author = re.search(r'- .*?:',line).group()[2:-1] #todo worked but don't know why we put the qualifier before and not after
                message = re.search(r':\s.*',line).group()[2:]
                columns = {'date':[date],'day':[day],'time':[time],'author':[author],'message':[message]}
                whatsapp_df = pd.DataFrame(data=columns)
                whatsapp_df.set_index('date',inplace=True)
                return pd.DataFrame(whatsapp_df)
            except:
                print('Error transforming the whatsapp chat')
    
        


__doc__ = '''The module helps with basic whatsapp chat transformations. A text file containing the conversation is uploaded, manipulated using regex, and then converted to a Pandas dataframe that sets out the authors, messages, time, date, and day of the week.'''