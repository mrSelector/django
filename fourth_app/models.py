
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField

    def __str__(self):
        return self.name + ' ' + self.surname


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.TextField()
    genre = models.CharField(max_length=15)

    def __str__(self):
        return self.title


