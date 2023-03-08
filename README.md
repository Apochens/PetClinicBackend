# Pet Clinic Backend
This is a course project.

---

## Preparation 
- Database: MariaDB 10.11.2 (port: 3366, password: 123456, database name: "clinic")
- PL: Python 3.11
- Backend Framework: Django 4.1.7
### Dependencies
- PyMySQL 1.0.2
- opencv-python
- djangorestframework 3.14.0

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

