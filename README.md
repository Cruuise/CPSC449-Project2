# CPSC449-Project2
By: Edgar Cruz

# Files
The project submission includes 4 files for the initial database set up. These files can be found in the bin folder. Init.sh is a script that will run users_setup.py, followers_setup.py, and posts_setup.py. The aforementioned files set up their respective data sets.

The var folder contains the databases used by timeline.py and users.py. Users only makes use of all_users.db, and timeline only uses all_posts.db.

The two python files on the root of the project contain the two APIs required for this project. Users.py handles all the requests to the users service; it does not depend on any services from timeline.py. On the other hand, timeline.py handles all the requests for the timeline service. Timeline.py acquires data from the users service through http requests. 

# Getting Started
Install the requirements with the following commands
> sudo apt update  
> sudo apt install --yes python3-pip ruby-foreman httpie sqlite3  
> python3 -m pip install hug sqlite-utils  
> sudo apt install --yes haproxy gunicorn  


The init file causes some issues on the virtual machine. You can initialize the databases by opening a terminal in the root folder and running the following commands:  
> python3 bin/users_setup.py  
> python3 bin/followers_setup.py  
> python3 bin/posts_setup.py  


Once the databases are initialized, restart haproxy with the following command  
> sudo systemctl restart haproxy

Start foreman with the following command:  
> foreman start -m "users=1, timeline=3"  

This starts 1 instance of the user API and 3 instances of the timeline API. You can make sure that haproxy is running with the following command:  
> sudo systemctl status haproxy

Users API is running on port 8000, whereas the 3 instances of the timeline API are running on ports 8100. 8101, and 8102. Keep these ports in mind when looking at the example API calls.  

**NOTE:** Pay attention to which ports foreman starts the services in. In a fresh install of all the files, foreman started the users service in port 5000 and the timeline service instances in ports 5100, 51001, and 5002.  

# API Services

Below are the routes followed by a description of what each does. The bullet point below each route is an example that can be ran using httpie  
**Users**  
*GET*  

> `/users`  --------------------------------------> Gets all users  
- http GET localhost:8000/users


> `/users/{username}`  ---------------------------> Gets a specific user  
- http GET localhost:8000/users/Dhsod


> `/users/{username}/followers` ------------------> Gets all the followers for the given username  
- http GET localhost:8000/users/Jane123/followers


> `/user/{username}/follows` ---------------------> Gets all the people that the given user follows  
- http GET localhost:8000/users/kev/follows

  

*POST*  
> `/users/{username}/follow` ---------------------> Makes the user follow a given username. Username must be unique  
- http POST localhost:8000/users/kev/follow username=kev follows=anonymous


> `/users` ---------------------------------------> Creates a new user  
- http POST localhost:8000/users username=Someone bio="my bio" password=123 email=email@e.com


**Timeline**  
*GET*  
> `/public` --------------------------------------> Returns public timeline of all posts  
- http GET localhost:8100/public  


> `/posts/{id}` ---------------------------------> Returns a specific post given an ID  
- http GET localhost:81001/posts/3  


> `/{username}/user_timeline` -------------------> Returns a timeline of all a given users posts  
- http GET localhost:8100/Ash/user_timeline  


> `/{username}/home_timeline` -------------------> Returns a timeline of all the posts from the people the user follows. Requires authentication  
- http GET Ash:something@localhost:8100/Ash/home_timeline  
- Authentication is passed along in the following format "username:password@domain"  


*POST*  
> `/post` ---------------------------------------> Makes a post. Requires authentication  
- http POST Ash:something@localhost:8100/post username=Ash text="Im kev"   
