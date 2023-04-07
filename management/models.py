from django.db import models

from case.models import Case


class Department(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

class Medicine(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)

class Instrumentation(models.Model):
    id = models.IntegerField(primary_key=True)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    method = models.TextField(max_length=1000)

class Checkup(models.Model):
    id = models.IntegerField(primary_key=True)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)

class Hospitalization(models.Model):
    id = models.IntegerField(primary_key=True)
    case_id = models.IntegerField()
    price = models.IntegerField()
    bg_time = models.DateTimeField()
    ed_time = models.DateTimeField()

# class Role(models.Model):
#     id = models.UUIDField(primary_key = True)
#     name = models.CharField(max_length=200)
#     department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
#     description = models.TextField(max_length=1000)