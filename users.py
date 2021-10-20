import hug
import sqlite3
import sqlite_utils
from sqlite_utils import Database

# db will be used for POST, db_query will be used for GET
db = Database(sqlite3.connect("./var/all_users.db"))
db_query = sqlite3.connect("./var/all_users.db")
cursor = db_query.cursor()
api = hug.get(on_invalid=hug.redirect.not_found)

# Getting all the users
@hug.get('/users')
def get_all_users():
    return {"users" : cursor.execute("SELECT username FROM users").fetchall()}

# Getting a single user users, shows password for demonstration purposes
@hug.get('/users/{username}')
def get_single_users(response, username:str):
    # Checking to see if user exists
    try:
        cursor.execute(f"SELECT bio FROM users WHERE username='{username}'")
    except sqlite_utils.db.NotFoundError:
        response.status = hug.falcon.HTTP_404

    return {"user" : cursor.execute(f"SELECT * FROM users WHERE username='{username}'").fetchall()}

# Getting all the users from specific user
@hug.get('/users/{username}/followers')
def get_user_home(username: str):
    action = f"SELECT user FROM followers WHERE follows='{username}'"
    return {"followers" : cursor.execute(action)}

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
        cursor.execute(f"SELECT username FROM users WHERE username='{username}'")
        cursor.execute(f"SELECT username FROM users WHERE username='{follows}'")

    except Exception as e:
        response.status = hug.falcon.HTTP_404
        return {"error": str(e)}

    # inserting user to followers table
    try:
        users.insert(user)
    except Exception as e:
        response.status = hug.falcon.HTTP_409
        return {"error": str(e)}

    response.set_header("Location", f"/books/{follows['id']}")
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