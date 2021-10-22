from sqlite_utils import Database
from datetime import datetime
import sqlite3

2011, 11, 4, 0, 5, 23, 283000
#Creating the all users db and users table
db = Database(sqlite3.connect("./var/all_posts.db"))
posts = db["posts"]
posts.insert({
    "id": 0,
    "author": "anonymous",
    "text": "Dhsods password is superoriginal",
    "timestamp": datetime(2021, 10, 1),
    "repost": "no",
}, pk = "id")

posts.insert({
    "id": 1,
    "author": "Dhsod",
    "text": "I feel like someone has my password",
    "timestamp": datetime(2021, 10, 2),
    "repost": "no",
})

posts.insert({
    "id": 2,
    "author": "Jane123",
    "text": "anonomyous is fake",
    "timestamp": datetime(2021, 10, 3),
    "repost": "no",
})

posts.insert({
    "id": 3,
    "author": "kev",
    "text": "Im kev",
    "timestamp": datetime(2021, 10, 4),
    "repost": "no",
})

posts.insert({
    "id": 4,
    "author": "Ash",
    "text": "Im kev",
    "timestamp": datetime(2021, 10, 5),
    "repost": "yes",
})