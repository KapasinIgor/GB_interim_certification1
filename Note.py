from datetime import datetime
import uuid


class Note:
    def __init__(self, id=str(uuid.uuid1())[0:3], title="", text="",
                 date=str(datetime.now().strftime('%Y, %B %d, %A | %H:%M'))):
        self.id = id
        self.title = title
        self.text = text
        self.date = date

    def set_id(self):
        self.id = str(uuid.uuid1())[0:3]

    def set_title(self, title):
        self.title = title

    def set_date(self):
        self.date = datetime.now().strftime('%Y, %B %d, %A | %H:%M')

    def set_text(self, text):
        self.text = text

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_date(self):
        return self.date

    def get_text(self):
        return self.text

    def to_string(self):
        return f'{self.id};{self.title};{self.text};{self.date}'

    def map_note(self):
        return f'\nId: {self.id}\nЗаголовок: {self.title}\nТекст: {self.text}\nДата: {self.date}'

