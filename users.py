import hug
import sqlite3
from sqlite_utils import Database

db = sqlite3.connect("./var/all_users.db")
cursor = db.cursor()
api = hug.get(on_invalid=hug.redirect.not_found)


@hug.get('/users')
def get_all_users():
    return cursor.execute("SELECT username FROM users").fetchall()

@hug.get('/users/{username}')
def get_user_home():
    #will need list of followers
    return 'Welcome home!'

@hug.post('/users/{username}/{follow_name}')
def follow_users():
    return 'Welcome home!'

