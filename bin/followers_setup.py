from sqlite_utils import Database
import sqlite3

#Creating the followers table, will have to join values to get full followers
# Ensures values are atomic
db = Database(sqlite3.connect("./var/all_users.db"))
users = db["followers"]
users.insert({
    "user": "anonymous",
    "follows": "kev",
})
users.insert({
    "user": "anonymous",
    "follows": "Dhsod",
})
users.insert({
    "user": "anonymous",
    "follows": "Jane123",
})

users.insert({
    "user": "anonymous",
    "follows": "Ash",
})

users.insert({
    "user": "kev",
    "follows": "Jane123",
})

users.insert({
    "user": "kev",
    "follows": "Ash",
})

users.insert({
    "user": "Dhsod",
    "follows": "kev",
})

users.insert({
    "user": "Dhsod",
    "follows": "Jane123",
})

users.insert({
    "user": "Jane123",
    "follows": "Ash",
})

users.insert({
    "user": "Jane123",
    "follows": "Dhsod",
})

users.insert({
    "user": "Ash",
    "follows": "Jane123",
})

users.insert({
    "user": "Ash",
    "follows": "anonymous",
})







