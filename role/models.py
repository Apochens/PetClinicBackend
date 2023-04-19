from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    jobs = models.CharField(max_length=100)


class Workflow(models.Model):
    name = models.CharField(max_length=20)
    video = models.CharField(max_length=100)
    process = models.JSONField()  # An array of steps

