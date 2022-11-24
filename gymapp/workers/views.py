from django.shortcuts import render

# Create your views here.
def index(response):
    return render(response, "workers/index.html", {})

def customers(response):
    pass

def schedule(response):
    pass

def personal(response):
    pass

def cams(response):
    pass

def stock(response):
    pass
