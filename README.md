# Pet Clinic Backend

This is a course project of software engineering.

---

## Preparation 

- Database Server: MariaDB 10.11.2 (port: 3366, password: 123456, database name: "clinic")
- Programming Language: Python 3.11
- Backend Framework: Django 4.1.7

If the configuration of port, password and database name is different from here, 
one can modify `DATABASES` configuration in the [PetClinicBackend/setting.py](./PetClinicBackend/settings.py).

### Dependencies

There are other dependencies which are required to run this server:

- For connecting MariaDB: PyMySQL 1.0.2
- For authentication (REST API)
  - djangorestframework 3.14.0
  - djangorestframework-simplejwt 5.2.2
- For cross domain issue: django-cors-headers 3.14.0

---

## Structure of The Project

```text
PetClinicBackend
|
|--- authentication             For user management and login/logout
|
|--- case                       For case management
|
|--- data                       Some data files for database initialization
|
|--- management                 For clinic's system management
|
|--- media                      Static files
    |       
    |--- init_pic               
    |--- init_video
    |
|--- PetClinicBackend            Django main folder
|
|--- quiz                        For quiz management
|
|--- role                        For the role-playing module
```

---

## Run This Server

### Run locally

To run this server locally, you need to install [MariaDB](https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.11.2&os=windows&cpu=x86_64&pkg=msi&m=blendbyte) first. 
The MariaDB setting are shown in the [Preparation](#preparation)
Then clone this repo and `cd` into it.

```shell
git clone https://github.com/Apochens/PetClinicBackend.git
cd PetClinicBackend
```
Then install the python libraries listed in the [Dockerfile](./Dockerfile) and use the following command to start the server.

```shell
python3 makemigrations
python3 migrate
python3 manage.py runserver 127.0.0.1:8000
```

Then visit `127.0.0.1:8000` in the bowser for fun!

### Run with Docker

Only one command to start the server:

```shell
docker-compose up
```
To shut down the docker:

```shell
docker-compose down
```

---

## About Authentication

```python
# In some_app/views.py
from rest_framework.views import APIView

class MyView(APIView):
    
    def get(self, request):
        """The response for GET request"""
        return
    
    def post(self, request):
        """The response for POST request"""
        return

# In some_app/urls.py
from django.urls import path
from . import views

urlpattern = [
    path('myview', views.MyView.as_view())
]
```
