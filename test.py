import re
import pandas as pd
# 2018/02/18, 18:52 - Sechaba: Small pulled pork tramazinni with mozzarella and sweet chilli+ 1000 islands
# 2018/02/18, 18:52 - Lungelo: Ok
# 2018/02/18, 19:02 - Sechaba: Thanks
# 2018/02/18, 21:08 - Lungelo: Dd you tell her about the braai

# pattern - date + time + dash + space, name, colon, message

with open('Lungelo.txt',encoding='utf8') as file:
     text_messages = file.readlines()

for line in text_messages:
    try:
        date = re.search(r'\d{4}/\d{2}/\d{2}',line).group()
        time = re.search(r'\d{2}:\d{2}',line).group()
        author = re.search(r'- .*?:',line).group()[2:-1] #todo worked but don't know why we put the qualifier before and not after
        message = re.search(r':\s.*',line).group()[2:]
        columns = {'date':[date],'time':[time],'author':[author],'message':[message]}
        whatsapp_df = pd.DataFrame(data=columns)
    except:
        print('Error transforming the whatsapp chat')



