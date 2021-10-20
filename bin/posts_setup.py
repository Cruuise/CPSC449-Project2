from sqlite3.dbapi2 import Date
from sqlite_utils import Database
import sqlite3

#Creating the all users db and users table
db = Database(sqlite3.connect("./var/all_posts.db"))
posts = db["posts"]
posts.insert({
    "id": 0,
    "author": "anonymous",
    "text": "Dhsod's password is superoriginal",
    "timestamp": Date(2021, 10, 1),
    "repost": "no",
}, pk = "id")

posts.insert({
    "id": 1,
    "author": "Dhsod",
    "text": "I feel like someone has my password",
    "timestamp": Date(2021, 10, 2),
    "repost": "no",
})

posts.insert({
    "id": 2,
    "author": "Jane123",
    "text": "anonomyous is fake",
    "timestamp": Date(2021, 10, 3),
    "repost": "no",
})

posts.insert({
    "id": 3,
    "author": "kev",
    "text": "I'm kev",
    "timestamp": Date(2021, 10, 4),
    "repost": "no",
})

posts.insert({
    "id": 4,
    "author": "Ash",
    "text": "I'm kev",
    "timestamp": Date(2021, 10, 5),
    "repost": "yes",
})