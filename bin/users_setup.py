from sqlite_utils import Database
import sqlite3

#Creating the all users db and users table
db = Database(sqlite3.connect("./var/all_users.db"))
users = db["users"]
users.insert({
    "username": "anonymous",
    "bio": "I am everywhere",
    "password": "superlegitpass",
    "email": "anon@fake.com",
}, pk = "username")

users.insert({
    "username": "kev",
    "bio": "kev is short for kevin",
    "password": "keviniscool",
    "email": "turtles@awesome.com",
})

users.insert({
    "username": "Dhsod",
    "bio": "My username is original",
    "password": "superoriginal",
    "email": "test@fake.com",
})

users.insert({
    "username": "Jane123",
    "bio": "I didn't check if 'Jane' was taken",
    "password": "Ishouldvechecked",
    "email": "Jane@123.com",
})

users.insert({
    "username": "Ash",
    "bio": "bio",
    "password": "something",
    "email": "Ash@sha.com",
})