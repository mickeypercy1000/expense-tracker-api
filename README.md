# expenses_code_api
Backend Take Home Challenge. This project contains RESTful APIS that allows a user manage their income and expenses. All income and expenses are tied to a user. The API returns responses for SUCCESS, FAILED, NOT FOUND based on your operation.


```APIs are browsable via SWAGGER on``` 
- "http://127.0.0.1:8000/swagger/"


```Base URL for all requests is 127.0.0.1:8000 ```
The APIs allow you to:
* Create a new custom user with the following payload
- email(required)
- firstname(optional)
- lastname(optional)
- username(required) --> Even though username won't be used for logins, it is a unique filed. Hence, it is required on signup
- password(required)

```/auth/signup/  POST REQUEST```

SAMPLE PAYLOAD FOR SIGNUP
{
    "email":"mike@gmail.com",
    "firstname":"michael",
    "lastname":"amoo",
    "username":"mike100",
    "password":"Were-r11"
}

* Login a user
```/auth/login/  POST REQUEST```
SAMPLE PAYLOAD
{
    "email":"mike@mike.com",
    "password":"Mike.100"
}
Both email and password fields are required.


* Fetch an existing user records
```/auth/user/{userID}/profile/  GET REQUEST```
No payload required. Simply pass the user's ID in the URL


* Update existing user records
```/auth/user/{userID}/profile/  PUT REQUEST```
Provide any of the fields specified in the signup payload to update a user's profile


* Get all incomes belonging to you. You must be logged in to perform this action
```/user/income/  GET REQUEST```


* Create a new income item. You must be logged in to perform this action
```/user/income/  POST REQUEST```
SAMPLE PAYLOAD
{
    "nameOfRevenue":"salary",
    "amount":"100"
}
Both fields are required


* Fetch a single income item by ID. You must be logged in to perform this action
```/user/income/{incomeID}  GET REQUEST```
No payload required. Simply pass the income ID in the URL


* Update an existing income item. You must be logged in to perform this action
```/user/income/{incomeID}  PUT REQUEST```
Provide any of the fields specified in creating a new income item


* Delete a single income item by ID. You must be logged in to perform this action
```/user/income/{incomeID}  DELETE REQUEST```
No payload required. Simply pass the income ID in the URL


* Create a new expenditure item. You must be logged in to perform this action
```user/expenditure/  POST REQUEST```
SAMPLE PAYLOAD
{
    "category":"fuel",
    "nameOfItem":"fuel for the weekend",
    "estimatedAmount":"110"
}

"category" field options:
- fuel
- dress
- transportation
- food

All fields are required


* Get all expenditure belonging to you. You must be logged in to perform this action
```/user/expenditure/  GET REQUEST```


* Fetch a single expenditure item by ID. You must be logged in to perform this action
```/user/expenditure/{expenditureID}  GET REQUEST```
No payload required. Simply pass the expenditure ID in the URL


* Update an existing expenditure item. You must be logged in to perform this action
```/user/expenditure/{expenditureID}  PUT REQUEST```
Provide any of the fields specified in creating a new expenditure item


* Delete an existing expenditure item. You must be logged in to perform this action
```/user/expenditure/{expenditureID}  DELETE REQUEST```
No payload required. Simply pass the expenditure ID in the URL


* Logout a user. You must be logged in to perform this action
```/auth/logout/  POST REQUEST```
SAMPLE PAYLOAD
{
    "refresh":"33523r34rfewfefe-gerger-r-fger-34-erfd--4tr-ef-dsv-et"
}
The "refresh" key refers to the refresh token generated on login.


## Postman Collection Included
* The project also contains a complete list of the postman collections


## Fun Fact
* All API endpoints respond within 20ms

## Technologies
* Python 3.10
* Django 4.1
* Django REST FRAMEWORK
* PostgreSQL
* Docker

### Setup
## Installation on Windows, Linux and Mac OS

* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo

* [Follow the guide here](https://docs.docker.com/docker-for-windows/install/) on how to set up Docker for windows
* [Follow the guide here](https://docs.docker.com/engine/install/ubuntu/) on how to set up Docker for Linux
* [Follow the guide here](https://docs.docker.com/docker-for-mac/install/#:~:text=Install%20and%20run%20Docker%20Desktop,Applications%20folder%20to%20start%20Docker.) on how to set up Docker for Mac OS

* Run project using Docker in simple steps

  ```
  docker-compose up -d --build (Build project docker image and run container)
  
  docker-compose exec web python3 manage.py makemigrations (Make model migrations)
  
  docker-compose exec web python3 manage.py migrate (Migrate models to database)
    
  docker-compose exec web python3 manage.py test (Run Unit Tests on API Endpoints)
  
  ```


* Run the project without docker

- Open the project in your text editor after forking it from Github
- Navigate to the root of the project folder
- Run the following commands:

virtualenv venv (This commands installs a virtual environment)
source venv/bin/activate (This command activates the virtual environment) ------ on mac
pip3 install -r requirements.txt
python3 manage.py makemigrations (Stage model migrations)
python3 manage.py migrate (Make model migrations)
python3 manage.py runserver (Run the Django server)

You can now make the api calls using Postman (https://www.blazemeter.com/blog/how-use-postman-test-apis)