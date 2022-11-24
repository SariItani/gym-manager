from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Customer(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10)
    weight = models.IntegerField()
    height = models.IntegerField()
    bmi = models.IntegerField()
    Programs = models.CharField(max_length=200)
    bill = models.IntegerField()

    def __str__(self):
        return self.name
