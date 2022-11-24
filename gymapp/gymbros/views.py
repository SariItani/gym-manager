from django.shortcuts import render
from datetime import datetime

current_dateTime = str(datetime.now())

# Create your views here.
def index(response):
    return render(response, "gymbros/index.html", {})

def login(response):
    pass

def signin(response):
    pass

def create(response):
    pass

def programs(response):
    pass

def dashboard(response):
    pass

def ux(response):
    pass
