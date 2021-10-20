import hug
import sqlite3
import sqlite_utils
from sqlite_utils import Database
import requests

# db will be used for POST, db_query will be used for GET
# db = Database(sqlite3.connect("./var/all_posts.db"))
# db_query = sqlite3.connect("./var/all_postss.db")
# cursor = db_query.cursor()
# api = hug.get(on_invalid=hug.redirect.not_found)

def get_user_info(username):
    req = requests.get(f'http://localhost:8000/users/{username}')
    return req.json()

result = get_user_info("Dhsod")
print(result)
hello = []
hello = result
print(hello['user'][0])