import hug
import sqlite3
import sqlite_utils
from sqlite_utils import Database

# db will be used for POST, db_query will be used for GET
db = Database(sqlite3.connect("./var/all_users.db"))
db_query = sqlite3.connect("./var/all_users.db")
cursor = db_query.cursor()
api = hug.get(on_invalid=hug.redirect.not_found)
