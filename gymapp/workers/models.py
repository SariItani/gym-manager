from django.db import models
from gymbros.models import Customer


# Create your models here.
class Schedule(models.Model):
    name = models.CharField(max_length=20, unique=True)
    Mon = models.CharField(max_length=10)
    Tues = models.CharField(max_length=10)
    Wed = models.CharField(max_length=10)
    Thu = models.CharField(max_length=10)
    Fri = models.CharField(max_length=10)
    Sat = models.CharField(max_length=10)
    Sun = models.CharField(max_length=10)
    Punch_in = models.CharField(max_length=50)
    Punch_out = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Workers(models.Model):
    name = models.CharField(max_length=20, unique=True)
    nb = models.IntegerField()
    jobtitle = models.CharField(max_length=30)
    legal = models.BooleanField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name


class Customers(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=160)
    bill = models.IntegerField()
    Punch_in = models.CharField(max_length=50)
    Punch_out = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cams(models.Model):
    cam = models.IntegerField(unique=True)

    def __str__(self):
        return self.cam


class Stock(models.Model):
    item = models.CharField(max_length=20, unique=True)
    inuse = models.IntegerField()
    out = models.IntegerField()

    def __str__(self):
        return self.item
