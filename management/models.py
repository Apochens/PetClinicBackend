from django.db import models

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

# class Role(models.Model):
#     id = models.UUIDField(primary_key = True)
#     name = models.CharField(max_length=200)
#     department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
#     description = models.TextField(max_length=1000)