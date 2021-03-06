import hug
import sqlite3
import sqlite_utils
from sqlite_utils import Database

# Makes the output JSON more legible
hug.defaults.output_format = hug.output_format.pretty_json
db = Database(sqlite3.connect("./var/all_users.db"))

# Getting all the usernames
@hug.get('/users')
def get_all_users():
    return db.query("SELECT * FROM users")

# Getting a single user users, shows password for demonstration purposes
@hug.get('/users/{username}')
def get_single_users(response, username:str):
    # Checking to see if user exists
    try:
        db.query(f"SELECT bio FROM users WHERE username='{username}'")
    except sqlite_utils.db.NotFoundError:
        response.status = hug.falcon.HTTP_404
    query_string = (f"SELECT * FROM users WHERE username='{username}'")
    return db.query(query_string)

# Getting all the followers from specific user
@hug.get('/users/{username}/followers')
def get_user_followers(username: str, response):
    query_string = f"SELECT user FROM followers WHERE follows='{username}'"
    try:
        db.query(query_string)
    except Exception as e:
        response.status = hug.falcon.HTTP_404
        return {"error": str(e)}
    return db.query(query_string)


# Getting all the people the user follows
@hug.get('/users/{username}/follows')
def get_user_followers(username: str):
    query_string = f"SELECT follows FROM followers WHERE user='{username}'"
    return db.query(query_string)

# POST to create a follower, usename ----follow----> follows
@hug.post("/users/{username}/follow", status=hug.falcon.HTTP_201)
def create_follower(
    response,
    username: hug.types.text,
    follows: hug.types.text,
):
    users = db["followers"]

    user = {
        "user": username,
        "follows": follows,
    }
    # Checking to see if users exist 
    try:
        db.query(f"SELECT username FROM users WHERE username='{username}'")
        db.query(f"SELECT username FROM users WHERE username='{follows}'")

    except Exception as e:
        response.status = hug.falcon.HTTP_404
        return {"error": str(e)}

    # inserting user to followers table
    try:
        users.insert(user)
    except Exception as e:
        response.status = hug.falcon.HTTP_409
        return {"error": str(e)}

    return user

@hug.post("/users", status=hug.falcon.HTTP_201)
def create_user(
    response,
    username: hug.types.text,
    bio: hug.types.text,
    password: hug.types.text,
    email: hug.types.text,
):
    users = db["users"]

    user = {
        "username": username,
        "bio": bio,
        "password": password,
        "email": email 
    }
    try:
        users.insert(user)
    except Exception as e:
        response.status = hug.falcon.HTTP_409
        return {"error": str(e)}

    response.set_header("Location", f"/users/{user['username']}")
    return user
