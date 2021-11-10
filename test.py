import re
import pandas as pd
from datetime import datetime

# 2018/02/18, 18:52 - Sechaba: Small pulled pork tramazinni with mozzarella and sweet chilli+ 1000 islands
# 2018/02/18, 18:52 - Lungelo: Ok
# 2018/02/18, 19:02 - Sechaba: Thanks
# 2018/02/18, 21:08 - Lungelo: Dd you tell her about the braai

# pattern - date + time + dash + space, name, colon, message

with open('Lungelo.txt',encoding='utf8') as file:
     text_messages = file.readlines()[1:]

for line in text_messages:
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
        print(type(whatsapp_df))
    except:
        print('Error transforming the whatsapp chat')


# import pandas as pd
# import pyodbc #seems important but haven't figured out where I'm going to use it yet - odbc is a db api
# import sqlite3
# import sqlalchemy


# from sqlalchemy import create_engine
# from sqlite3.dbapi2 import connect
# from typing import final
# from numpy import dtype, e, insert

# from whatsapp_messages import WhatsappChat
# from create_tables import CreateTable





