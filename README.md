# Blog Application 

#### By Peter Kinyanjui

## Description
    This web application is built using Python framework known as Flask. The app displays blogs that have been posted and  by the users and other users can login and  leave a comment.

## Setup/Installation Requirements
First clone the repo
   ```$ git clone https://github.com/raymondyegon/blog-flask.git ```

After cloning, navigate to the project:
   `` $ cd blog-flask``

Create the virtual enviroment
    ``$ python3.6 -m venv --without-pip virtual``

    ``$ source virtual/bin/env``

    ``$ curl https://bootstrap.pypa.io/get-pip.py | python``


Then install all the requirements through pip:
   ```$ pip install -r requirements.txt ```

Make the file executable:
   ```$ chmod +x start.sh```

Run the application:
   ```$ ./start.sh ```

Now navigate to your browser at: ```localhost:5000```

## Technologies Used
* Python
* Jquery
* Flask
* HTML5
* Bootstrap

## BDD
|BEHAVIOUR|INPUT|OUTPUT|
|--------:|-----:|-----:|
|Registration|Sumbmit Registration form|User creates account|
|Subscription|Submit subscription form|User is notified when there is a post|
|Comment on Blog|Access the comment form|Comment for a blog is viewed|

# Contact info
Incase of any challenges or questions, feel free to reach outh via email(petermax2004@gmail.com)

## Lisence
[mit] (LICENSE)
