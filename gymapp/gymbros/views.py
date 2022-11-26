from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime

current_dateTime = str(datetime.now())

# Create your views here.
def index(response):
    return render(response, "gymbros/index.html", {})

def login(response):
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("login"):
            n = response.POST.get("username")
            p = response.POST.get("password")
            # validate
            return HttpResponseRedirect("/index")
    return render(response, "gymbros/login.html", {})

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
