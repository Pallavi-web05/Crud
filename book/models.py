import email
from django.db import models
from django.forms import CharField

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=200)
    tittle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    edition = models.IntegerField()
    publication = models.CharField(max_length=100)

    def __str__(self):
        return self.tittle


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LoginUser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    