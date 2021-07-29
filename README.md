# Fampay
# Tech Stack
1. Python 
2. Django 
3. SQLite
4. Docker

# How to build docker and run
docker build -t fampay-youtube .

docker run -p 8000:8000 fampay-youtube

# APIs 

**GET APIs**

http://localhost:8000/api/fampay-youtube/videos?limit=10&offset=1 ---> used to get all the videos in limit offset pagination manner that stored in DB

http://localhost:8000/api/fampay-youtube/videos?search="POP"      ---> used to get all the videos that are having "POP" in title and description

http://localhost:8000/api/fampay-youtube/add_key

**POST APIs**

http://localhost:8000/api/fampay-youtube/add_key ---> Used to add the Api Key that will be used for fetching the videos from youtube APIs.

# Create Superuser for checking the Database

docker ps ---> for getting the container-Id

docker exec -it <container-id> python manage.py createsuperuser

If you didn't get response in the Videos Api Try running the cronjob once manually in docker, Then you will get the response.  
  
  

