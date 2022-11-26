from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import *
from workers.models import *
from .forms import*

# Create your views here.
def index(response):
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("logout"):
            punch_out = str(datetime.now())
            print(punch_out)
            # Customers.objects.filter(name=n).update(Punch_out=punch_out)
            return HttpResponseRedirect("/")
        if response.POST.get("sign-in"):
            return HttpResponseRedirect("/sign-in")
    return render(response, "gymbros/index.html", {})

def login(response):
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("login"):
            n = response.POST.get("username")
            p = response.POST.get("password")
            punch_in = str(datetime.now())
            print(punch_in)

            # validate
            if response.POST.get("nb"):
                nb = int(response.POST.get("nb"))
                employee = Workers.objects.get(nb=nb)
                if employee.password == p:
                    return HttpResponseRedirect("/work")
            if User.objects.filter(username=n).exists():
                user = User.objects.get(username=n)
                print(user)
                if user.password == p:
                    print("Password input",p, "is valid")
                    customer = Customer.objects.get(customer_id=user.id)
                    print(customer)
                    print("before login:")
                    print(Customers.objects.get(Customer_id=customer.id).Punch_in)
                    Customers.objects.filter(Customer_id=customer.id).update(Punch_in=punch_in)
                    print("after login:")
                    print(Customers.objects.get(Customer_id=customer.id).Punch_in)
                    return HttpResponseRedirect("/index")
                else:
                    print("invalid password")
    return render(response, "gymbros/login.html", {})

def signin(response):
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("sign-in"):
            u = response.POST.get("username")
            p = response.POST.get("password")
            e = response.POST.get("email")
            user = User(username=u, password=p, email=e)
            user.save()
            n = response.POST.get("name")
            g = response.POST.get("gender")
            w = int(response.POST.get("weight"))
            h = int(response.POST.get("height"))
            customer = Customer(customer=user, name=n, gender=g, weight=w, height=h, bmi=w**2/h, Programs='', bill=0)
            customer.save()
            customers = Customers(Customer=customer, name=customer.name, gender=customer.gender, email=user.email, password=user.password, bill=0, Punch_in = str(datetime.now()), Punch_out='')
            customers.save()
            return HttpResponseRedirect("/index")
    return render(response, "gymbros/sign-in.html", {})

def create(response):
    pass

def programs(response):
    pass

def dashboard(response):
    pass

def ux(response):
    pass
