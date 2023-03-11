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

**/authentication/token/**

- POST (get the user token for login)
    - Need auth: no
    - Body
      ```json
      { "username": "uname", "password": "pword"}
      ``` 
    - Return
      ```json
      { "access": "token_str", "refresh": "token_str"}
      ```


**/quiz/**

- GET (get the quiz list)
    - Need auth: yes
    - Body: None
    - Return
      ```json
      { 
        "success": true, 
        "message": "msg",
        "list": [
          {
            "id": 1,
            "name": "quiz_name",
            "duration": 10
          }
        ] 
      }
      ```

**/quiz/<int:quiz_id>/**

- GET
    - Need auth: Yes
    - Body: None
    - Return
      ```json
      { "success": true, "message": "msg", "data": {"id": 1, "name": "quiz_name", } }
      ```

**/quiz/question/**



**/quiz/question/<str:qustion_type>/<int:question_id>**

- GET
    - Need auth: Yes
    - Body: None
    - Return
      ```json
        { 
          "success": true, 
          "message": "msg", 
          "data": { 
            
          } 
        }
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

| Table name      | Table items                                         |
|-----------------|-----------------------------------------------------|
| section         | name, description, pic,                             |
| role            | id                                                  |
| medicine        | id, name, effect, cost, description, picture, video |
| instrumentation | id, name, description, picture, video               |
| examination     | id, name, cost, description, picture, video         |

**User management**

| Table name | Table items              |
|------------|--------------------------|
| user       | id, name, password, role |

**Disease case management**

| Table name | Table items                                                          |
|------------|----------------------------------------------------------------------|
| case       | disease_name, disease_type, diagnosis, examination, result, solution |

**Testing management**

| Table name             | Table items                                                     |
|------------------------|-----------------------------------------------------------------|
| quiz                   | id, duration, questions, students                               |
| single_choice_question | id, description, option_a, option_b answer, disease_type, score |

---

