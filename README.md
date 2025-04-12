# About
This is a django rest api project

## How to run it
1. You should create a virtual environment, there are plenty of ways
to do it, but I recommend to use anaconda 

`conda create --name globant_human-resources_api python=3.13.2`  
`conda activate globant_human-resources_api`  
`pip install -r requirements.txt`  

2. Update your database's host and credentials  
   2.1. Update your variable secret_name in project/project/controller/secrets_manager.py.  
   2.2. Update HOST in settings.py file.  
3. Migrating the database   
`cd project`  
`python manage.py makemigrations`  
`python manage migrate`
4. Run
`python manage.py runserver`