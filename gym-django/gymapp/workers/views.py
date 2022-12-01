from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from database_to_pdf import *

# Create your views here.


def index(response):
    return render(response, "workers/index.html", {})


def customers(response):
    data = Customers.objects.all()
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("remove"):
            n = response.POST.get("name")
            entry = Customers.objects.get(name=n)
            entry.delete()
        if response.POST.get("print"):
            gymbros_user()
            gymbros_customer()
            workers_customers()
    return render(response, "workers/customers.html", {"data": data})


def schedule(response):
    data = Schedule.objects.all()
    print(data)
    if response.method == "POST":
        if response.POST.get("print"):
            workers_schedule()
        if response.POST.get("save"):
            for e in data:
                mon = response.POST.get("mon"+str(e.id))
                tues = response.POST.get("tues"+str(e.id))
                wed = response.POST.get("wed"+str(e.id))
                thu = response.POST.get("thu"+str(e.id))
                fri = response.POST.get("fri"+str(e.id))
                sat = response.POST.get("sat"+str(e.id))
                sun = response.POST.get("sun"+str(e.id))
                Schedule.objects.filter(name=e.name).update(
                    Mon=mon, Tues=tues, Wed=wed, Thu=thu, Fri=fri, Sat=sat, Sun=sun)
    return render(response, "workers/schedule.html", {"data": data})


def personal(response):
    data = Workers.objects.all()
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("remove"):
            n = response.POST.get("name")
            entry = Workers.objects.get(name=n)
            entry.delete()
        if response.POST.get("print"):
            workers_workers()
    return render(response, "workers/personal.html", {"data": data})


def create(response):
    if response.method == "POST":
        form = Create(response.POST)
        print(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            e = form.cleaned_data["email"]
            p = form.cleaned_data["password"]
            nb = form.cleaned_data["nb"]
            j = form.cleaned_data["jobtitle"]
            l = form.cleaned_data["legal"]
            s = form.cleaned_data["salary"]
            employee = Workers(name=n, email=e, password=p,
                               nb=nb, jobtitle=j, legal=l, salary=s)
            schedule = Schedule(name=n, Mon="", Tues="",
                                Wed="", Thu="", Fri="", Sat="", Sun="")
            schedule.save()
            employee.save()
            return HttpResponseRedirect("/work/personal/")
    else:
        form = Create()
    return render(response, "workers/login.html", {"form": form})


def cams(response):
    return render(response, "workers/cams.html", {})


def stock(response):
    return render(response, "workers/stock.html", {})
