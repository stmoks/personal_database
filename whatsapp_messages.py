import re, pandas as pd
# create messages object
# import txt file
# transform the text data
# link the whatsapp messages with the contacts db
# employ nlp (see script) to get a sense of conversations
# make use of matplot to draw cool things - timelines
# write a story - nlp + other tools to make the chats sing (include the Google translate to speech that chats through the conversation)

import re

class Whatsapp_Chat:
    def __init__(self,name):
        self.name = name
        self.load_chats(self.name)

    def load_chats(self, name):
        with open(f'{name}'.txt,encoding='utf8') as file:
            text_messages = file.readlines()
        self.transform_chats(text_messages)

    def transform_chats(self, messages):
        for line in messages:
            try:
                date = re.search(r'\d{4}/\d{2}/\d{2}',line).group()
                time = re.search(r'\d{2}:\d{2}',line).group()
                author = re.search(r'- .*?:',line).group()[2:-1] #todo worked but don't know why we put the qualifier before and not after
                message = re.search(r':\s.*',line).group()[2:]
                columns = {'date':[date],'time':[time],'author':[author],'message':[message]}
                whatsapp_df = pd.DataFrame(data=columns)
                return whatsapp_df
            except:
                print('Error transforming the whatsapp chat')


