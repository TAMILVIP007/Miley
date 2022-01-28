from sqlalchemy import Boolean, Column, Integer, String, UnicodeText
from Evie.modules.sql import BASE, SESSION


class Nightmode(BASE):
    __tablename__ = "chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Nightmode.__table__.create(checkfirst=True)


def add_chat(chat_id: str):
    nightmoddy = Nightmode(str(chat_id))
    SESSION.add(nightmoddy)
    SESSION.commit()


def rmchat(chat_id: str):
    if rmnightmoddy := SESSION.query(Nightmode).get(str(chat_id)):
        SESSION.delete(rmnightmoddy)
        SESSION.commit()


def get_all_chat_id():
    stark = SESSION.query(Nightmode).all()
    SESSION.close()
    return stark


def is_chat(chat_id: str):
    try:
        if s__ := SESSION.query(Nightmode).get(str(chat_id)):
            return str(s__.chat_id)
    finally:
        SESSION.close()
