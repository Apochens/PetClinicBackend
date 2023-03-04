# Pet Clinic Backend
This is a course project.

---

## Preparation 
- Database: MariaDB 10.11.2 (port: 3366, password: 123456, name: "clinic")
- PL: Python 3.11
- Backend Framework: Django 4.1.7
### Dependencies
- PyMySQL 1.0.2
- opencv-python

---

### Table Definitions

**Basic architecture and functionalities management**

| Table name      | Table items                                         |
|-----------------|-----------------------------------------------------|
| section         | name, discription, pic,                             |
| role            | id                                                  |
| medicine        | id, name, effect, cost, discription, picture, video |
| instrumentation | id, name, discription, picture, video               |
 | examination     | id, name, cost, discripton, picture, video          |

**User management**

| Table name | Table items              |
|------------|--------------------------|
| user       | id, name, password, role |

**Disease case management**

| Table name | Table items                                                          |
|------------|----------------------------------------------------------------------|
| case       | disease_name, disease_type, diagnosis, examination, result, solution |

**Testing management**

| Table name | Table items                                  |
|------------|----------------------------------------------|
| quiz       | id, duration, questions, students            |
| question   | id, discription, answer, disease_type, score |