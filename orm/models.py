from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    company = models.CharField(max_length=50)
    salary = models.IntegerField()

