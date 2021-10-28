# create messages object
# import txt file
# transform the text data
# link the whatsapp messages with the contacts db
# employ nlp (see script) to get a sense of conversations
# make use of matplot to draw cool things - timelines
# write a story - nlp + other tools to make the chats sing

class Whatsapp_Chat:
    def __init__(self,name):
        self.name = name
        self.load_chats(self.name)

    def load_chats(self, name):
        with open(f'{name}'.csv) as file:
            pass
        self.transform_chats(file)

    def transform_chats(self, file):
        pass
        return file


