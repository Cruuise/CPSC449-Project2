from datetime import datetime
from falcon.response import ResponseOptions
import hug
import sqlite3
from requests.api import get
from sqlite_utils import Database
import requests

# Makes the output JSON more legible
hug.defaults.output_format = hug.output_format.pretty_json
# db will be used for POST, db_query will be used for GET
db = Database(sqlite3.connect("./var/all_posts.db"))
api = hug.get(on_invalid=hug.redirect.not_found)

# returns information from a given user. Will use this to auntenticate
def get_user_info(username):
    req = requests.get(f'http://localhost:8000/users/{username}')
    return req.json()

# return ppl that follow username
def get_followers(username):
    req = requests.get(f'http://localhost:8000/users/{username}/followers')
    return req.json()

# checks provided password against password in all_users.db
def authenticate_login(username, password):
    credentials = get_user_info(username)
    if (credentials[0]["password"] == password):
        return True
    return False
#http GET Ash:something@localhost:8001/public

# checks for  reposts, TODO
def check_repost(text):
    repost = "no"
    # repost_id = -1 if original, otherwise get the original post's id
    repost_id = -1
    for row in db.query(f"SELECT * FROM posts WHERE text='{text}' ORDER BY timestamp ASC"):
        id = row["id"]
        respost = f"localhost:8001/posts/{str(id)}" 
        # All we need is the first value of the loop
        break
    return repost

# function for testing purposes, can ignore
def test_function():
    # testing get user info first
    result = get_user_info("Dhsod")
    # returns list with 1 json object in it, it's the json decoder from requests
    print(result)
    # access inside of list with [0], ["username"] is the key we need
    print(result[0]["username"], result[0]["password"])
    

# public timeline, no authentication
@hug.get('/public')
def public_timeline():
    return db.query("SELECT * FROM posts ORDER BY timestamp DESC")
# gets single post by given post id, no authentication required.

@hug.get('/posts/{id}')
def get_post(
    id: hug.types.number
):
    return db.query(f"SELECT * FROM posts WHERE id='{id}'")

# Contains all of the users posts, requires authentication
@hug.get('/{username}/user_timeline')
def user_timeline(username: hug.types.text):
    return db.query(f"SELECT * FROM posts WHERE author='{username}'")

# Contains posts of all the ppl the user follows, requires authentication
@hug.get('/{username}/home_timeline', requires=hug.authentication.basic(authenticate_login))
def home_timeline(username: hug.types.text):
    # followers is a list of JSON users, example [{'user': 'anonymous'}, {'user': 'kev'}, {'user': 'Jane123'}] 
    followers = get_followers(username)
    name_query = []
    for x in followers:
        name_query.append(x["user"])
    name_query = str(name_query)[1:-1]
    return db.query(f"SELECT * FROM posts WHERE author IN ({name_query})")

@hug.post('/post', requires=hug.authentication.basic(authenticate_login))
def create_post(
    response,
    username: hug.directives.user,
    text: hug.types.text
):
    repost = check_repost(text)
    posts = db["posts"]


    post = {
        "author": username,
        "text": text,
        "timestamp": datetime.now,
        "repost": repost 
    }
    try:
        posts.insert(post)
        post["id"] = posts.last_pk
    except Exception as e:
        response.status = hug.falcon.HTTP_409
        return {"error": str(e)}

    response.set_header("Location", f"/posts/{post['id']}")
    return post

# test_function()
# # followers = get_followers("Ash")
# #dictionary has a list insde 
# print(followers)

# name_query = []
# for x in followers:
#     name_query.append(x["user"])
# print(name_query)
# name_query = str(name_query)[1:-1]
# print(name_query)
hug.API(__name__).http.serve(port=8001)

# id = -1
# for row in db.query(f"SELECT * FROM posts WHERE text='I''m kev' ORDER BY timestamp ASC"):
#     id = row["id"]
#     if not row:
#         print("hello there!")
#     break

# print(id)
# exists = db.query(f"SELECT * FROM posts WHERE author='kev!'")
# if id == -1:
#     print("i am empty")
# else:
#     print("I am not empty")