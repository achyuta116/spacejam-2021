import sqlite3
import datetime
import unittest

conn = sqlite3.connect("decks.db")
c = conn.cursor()


def insert_new_deck(name):
    c.execute("CREATE TABLE {} (current_interval real, current_EF real, mode text, question text, answer text, next_date text);".format(name))


def insert_new_card(deck_name, question, answer):
    l = list_decks()
    if deck_name not in l:
        c.execute("CREATE TABLE {}(current_interval real, current_EF real, mode text, question text, answer text, next_date text);".format(deck_name))
    c.execute('INSERT INTO {} VALUES (1,2.5,"learn","{}","{}","");'.format(deck_name, question, answer))


def get_cards(deck_name):
    c.execute("SELECT * FROM {}".format(deck_name))
    return c.fetchall()


def get_learn_cards(deck_name, learn_limit):
    return c.execute('SELECT * FROM {} WHERE mode="learn" LIMIT {}'.format(deck_name, learn_limit))

def get_review_cards(deck_name,review_limit):
    cards = []
    rows = c.execute('SELECT * FROM {} WHERE mode="review" '.format(deck_name))
    for i in rows:
        date = i['date']
        if date < datetime.date.today():
            cards.append(i)
    return cards

def list_decks():
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return list(map(lambda x:x[0],c.fetchall()))
    
def intervals(current_intv, current_EF):
    next_intv = []
    for i in range(5):
        if i < 2:
            next_intv.append(1)
        else:
            if current_EF < 1.3:
                current_EF = 1.3
            next_intv.append(
                current_intv*(current_EF+(0.1-(4-i)*(0.08+(4-i)*0.02))))
    return next_intv


def update_card(deck_name, question, new_interval, new_EF):
    new_date = datetime.date.today()+datetime.timedelta(new_interval)
    c.execute('UPDATE {} set current_interval={}, current_EF={}, next_date={}, mode="review" WHERE question={}'.format(
        deck_name, new_interval, new_EF, question, str(new_date)))

def new_EF_calculation(current_EF, q):
    return current_EF+0.1-(5-q)*(0.08+(5-q)*0.02)

def delete_deck(deck_name):
    c.execute('DROP TABLE {}'.format(deck_name))

def delete_card(deck_name, question):
    c.execute("DELETE FROM {} WHERE question={}".format(deck_name, question))
