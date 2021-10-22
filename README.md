# CPSC449-Project2
By: Edgar Cruz

# Files
The project submission includes 4 files for the initial database set up. These files can be found in the bin folder. Init.sh is a script that will run users_setup.py, followers_setup.py, and posts_setup.py. The aforementioned files set up their respective data sets.

The var folder contains the databases used by timeline.py and users.py. Users only makes use of all_users.db, and timeline only uses all_posts.db.

The two python files on the root of the project contain the two APIs required for this project. Users.py handles all the requests to the users service; it does not depend on any services from timeline.py. On the other hand, timeline.py handles all the requests for the timeline service. Timeline.py acquires data from the users service through http requests. 

# Getting Started
Note: The project does not need any other libraries besides the once stated in the

# API Services

**Users**
*GET*  
/users            ------> Gets all users  
/users/{username}  -------> Gets a specific user  
/users/{username}/followers -----> Gets all the followers for the given username  
/user/{username}/follows -------> Gets all the people that the given user follows  
  

*POST*  
/users/{username}/follow -----> Makes the user follow a given username  
/users -------> Creates a new user  

**Timeline**
*GET*  
/public -----> Returns public timeline of all posts  
/posts/{id} -----> Returns a specific post given an ID  
/{username}/user_timeline ----> Returns a timeline of all a given users posts  
/{username}/home_timeline ---> Returns a timeline of all the posts from the people the user follows. Requires authentication  
http GET localhost:8001/public  
http GET localhost:8001/posts/3  
http GET localhost:8001/Ash/user_timeline  
http GET Ash:something@localhost:8001/Ash/home_timeline  

*POST*  
/post -----> Makes a post. Requires authentication  
http POST Ash:something@localhost:8001/post username=Ash text="Im kev"   
