# Pet Clinic Backend
This is a course project.

---

## Preparation 
- Database Server: MariaDB 10.11.2 (port: 3366, password: 123456, database name: "clinic")
- Programming Language: Python 3.11
- Backend Framework: Django 4.1.7
### Dependencies

- For connecting MariaDB: PyMySQL 1.0.2
- For authentication (REST API)
  - djangorestframework 3.14.0
  - djangorestframework-simplejwt 5.2.2
- For cross domain issue: django-cors-headers 3.14.0

---

## Structure

```text
PetClinicBackend
|
|---case                        For case management
|
|---PetClinicBackend            Django main folder
|
|---quiz                        For quiz management
|
|---user                        For user management

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


## Interfaces

### Authentication

**/authentication/**

- GET (get user list)
  - Need auth: yes
  - Body: None
  - Return:
    ```json
    { 
      "success": true, 
      "message": "msg",
      "list": [
        {
          "id": 1,
          "username": "asd"
        }
      ]
    }
    ```
- POST (create a new user)
  - Need auth: yes
  - Body
    ```json
    { "username": "asd", "password": "123" }
    ```
  - Return
    ```json
    { "success": true, "message": "msg" }
    ```
- PUT (Modify the useranme or password)
  - Need auth: yes
  - Body 
    ```json 
    { "id": 1, "username": "new_name", "password": "new_pword" }
    ```
  - Return
    ```json
    { "success": true, "message": "msg" }
    ```
- DELETE
  - Need auth: yes
  - Body
    ```json
    { "id": 1}
    ```
  - Return
    ```json
    { "success": true, "message": "msg" }
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

---

### Table Definitions

**Basic architecture and functionalities management**


| Table name              | Table items                                                     |
|-------------------------|-----------------------------------------------------------------|
| department（科室信息）        | id, name, description, reserved1, reserved2, reserved3          |
| medicine（药品，疫苗信息）       | id, name, tag, type, price, description, reserved1, reserved2   |
| instrumentation（医院器械信息） | id, dept_id, name, description, reserved1, reserved2, reserved3 |
 | checkup（化验项目信息）         | id, name, price, description, reserved1, reserved2, reserved3   |
| role（医院中的人员信息）          | id, name, department_name, description, reserved1, reserved2    |
 | hospitalization（住院信息）   | -                                                               |

**User management**

| Table name | Table items              |
|------------|--------------------------|
| user       | id, name, password, role |

**Disease case management**

| Table name                 | Table items                                                          |
|------------------------------|----------------------------------------------------------------------|
| case(基本信息)              | id, case_number(unique), disease_type, disease_name, pet_name, pet_species, pet_age, owner_name, owner_phone, symptom, diagnosis_result, treatment |
| checkup(检查信息)           | id, case_number, checkup_item, checkup_result |
| category(导航分类信息)      | id, key, title, children |

**Testing management**

| Table name             | Table items                                                     |
|------------------------|-----------------------------------------------------------------|
| quiz                   | id, duration, questions, students                               |
| single_choice_question | id, description, option_a, option_b answer, disease_type, score |

---

