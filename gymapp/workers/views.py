from django.shortcuts import render, HttpResponseRedirect
from .models import Schedule, Workers, Customers, Cams, Stock

# Create your views here.
def index(response):
    return render(response, "workers/index.html", {})

def customers(response):
    pass

def schedule(response):
    pass

def personal(response):
    pass

def create(response):
    return render(response, "workers/login.html", {})

def cams(response):
    pass

def stock(response):
    pass
