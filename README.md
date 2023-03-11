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

### Case 

#### **/case/**   --- basic information of cases

- GET(get list of all cases)

  - Need auth: yes

  - Body: None

  - Return:

    ```json
    {
        "success": true,
        "message": "Get All Cases successfully!",
        "Cases": [
            {
                "id": 1,
                "case_number": "test1",
                "disease_type": "寄生虫病",
                "disease_name": "蛔虫病",
                "pet_name": "可爱的狗狗二号",
                "pet_species": "犬科",
                "pet_age": 1,
                "owner_name": "vv",
                "owner_phone": "123123123",
                "expense": 123.4,
                "symptom": {
                    "text": "none1",
                    "pic": "none1",
                    "video": "none1"
                },
                "diagnosis_result": {
                    "text": "none1",
                    "pic": "none1",
                    "video": "none1"
                },
                "treatment": {
                    "text": "none1",
                    "pic": "none1",
                    "video": "none1"
                }
            },
            {
                "id": 2,
                "case_number": "test2",
                "disease_type": "传染病",
                "disease_name": "犬瘟热",
                "pet_name": "tt的狗",
                "pet_species": "犬科",
                "pet_age": 1,
                "owner_name": "tt",
                "owner_phone": "1111111",
                "expense": 2333.3,
                "symptom": {
                    "text": "none2",
                    "pic": "none2",
                    "video": "none2"
                },
                "diagnosis_result": {
                    "text": "none2",
                    "pic": "none2",
                    "video": "none2"
                },
                "treatment": {
                    "text": "none2",
                    "pic": "none2",
                    "video": "none2"
                }
            }
        ]
    }
    ```

- POST(add a new case)

  - Need auth: yes

  - Body: 

    ```json
    {
        "case_number": "test2",
        "disease_type": "传染病",
        "disease_name": "犬瘟热",
        "pet_name": "tt的狗",
        "pet_species": "犬科",
        "pet_age": 1,
        "owner_name": "tt",
        "owner_phone": "1111111",
        "expense": 2333.3,
        "symptom": {
            "text": "none2",
            "pic": "none2",
            "video": "none2"
        },
        "diagnosis_result": {
            "text": "none2",
            "pic": "none2",
            "video": "none2"
        },
        "treatment": {
            "text": "none2",
            "pic": "none2",
            "video": "none2"
        }
    }
    ```

  - Return:

    ```json
    {
        "success": true,
        "message": "Create a new case successfully!"
    }
    ```

  - Note for below ( case_number should be unique) :

    ```json
    {
        "success": false,
        "message": "Failed to create a new case",
        "case_number": [
            "case with this case number already exists."
        ]
    }
    ```

#### /case/checkup --- extra information of cases

- GET(get list of all checkups)
  - Need auth: yes

  - Body: None

  - Return:

    ```json
    {
        "success": true,
        "message": "Get All Checkups successfully!",
        "Checkups": [
            {
                "id": 2,
                "case_number": "test2",
                "checkup_item": "血常规检查",
                "checkup_result": {
                    "text": "n2",
                    "pic": "n2",
                    "video": "n2"
                }
            }
        ]
    }
    ```

- POST

  - Need auth: yes

  - Body: 

    ```json
    {
        "case_number": "test3",
        "checkup_item": "血常规检查",
        "checkup_result": {
            "text": "n2",
            "pic": "n2",
            "video": "n2"
        }
    }
    ```

  - Return:

    ```json
    {
        "success": true,
        "message": "Create a new checkup successfully!"
    }
    ```

  - Note: **case_number** should be unique 

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

| Table name | Table items                                                  |
| ---------- | ------------------------------------------------------------ |
| case       | case_number(unique), disease_type, disease_name, pet_name, pet_species, owner_name, owner_phone, expense, symptom, diagnosis_result, treatment |
| checkup    | case_number(unique), checkup_item, checkup_result            |

**Testing management**

| Table name             | Table items                                                     |
|------------------------|-----------------------------------------------------------------|
| quiz                   | id, duration, questions, students                               |
| single_choice_question | id, description, option_a, option_b answer, disease_type, score |

---

