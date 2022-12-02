from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import *
from workers.models import *
from .forms import*
from database_to_pdf import *
import sqlite3
from fpdf import FPDF

# Create your views here.


def index(response, userID):
    customer = Customer.objects.get(customer_id=userID)
    global customerID
    customerID = customer.id  # used to pass info to customers in workers
    if response.method == "POST":
        if response.POST.get("logout"):
            punch_out = str(datetime.now())
            print(punch_out)
            Customers.objects.filter(
                Customer_id=userID).update(Punch_out=punch_out)
            # now i want to take the punch in punch out times and turn them to datetime objects so i can find the difference between them
            p_in = datetime.strptime(Customers.objects.get(
                Customer_id=customerID).Punch_in, '%Y-%m-%d %H:%M:%S.%f')
            p_out = datetime.strptime(Customers.objects.get(
                Customer_id=customerID).Punch_out, '%Y-%m-%d %H:%M:%S.%f')
            hours = ((p_out-p_in).total_seconds())/3600
            print(hours)
            actual_bill = customer.bill * hours + \
                Customers.objects.get(Customer_id=customer.id).bill
            print(actual_bill)
            Customers.objects.filter(
                Customer_id=customer.id).update(bill=actual_bill)
            return HttpResponseRedirect("/")
        if response.POST.get("sign-in"):
            return HttpResponseRedirect("/sign-in")
    return render(response, "gymbros/index.html", {"userID": userID})


def login(response):
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("login"):
            global n
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
                    print("Password input", p, "is valid")
                    global userID
                    userID = user.id
                    # now we have the id in the user sql table in userID
                    customer = Customer.objects.get(customer_id=userID)
                    print(customer)
                    print("before login:")
                    global customerID
                    customerID = customer.id
                    # now we have the id in customer sql table in customerID
                    print(Customers.objects.get(
                        Customer_id=customerID).Punch_in)
                    Customers.objects.filter(
                        Customer_id=customerID).update(Punch_in=punch_in)
                    print("after login:")
                    print(Customers.objects.get(
                        Customer_id=customerID).Punch_in)
                    return HttpResponseRedirect("/index/%i" % userID)
                else:
                    print("invalid password")
    return render(response, "gymbros/login.html", {})


def signin(response):
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("sign-in"):
            global n
            n = response.POST.get("username")
            # now we have the username in the user sql table in n
            p = response.POST.get("password")
            e = response.POST.get("email")
            user = User(username=n, password=p, email=e)
            user.save()
            global userID
            userID = user.id
            u = response.POST.get("name")
            g = response.POST.get("gender")
            w = int(response.POST.get("weight"))
            h = int(response.POST.get("height"))
            customer = Customer(customer=user, name=u, gender=g,
                                weight=w, height=h, bmi=10000*w/(h**2), Programs='', bill=0)
            customer.save()
            global customerID
            customerID = customer.id
            customers = Customers(Customer=customer, name=customer.name, gender=customer.gender,
                                  email=user.email, password=user.password, bill=0, Punch_in=str(datetime.now()), Punch_out='')
            customers.save()
            return HttpResponseRedirect("/index/%i" % userID)
    return render(response, "gymbros/sign-in.html", {})


def programs(response, userID):
    customer = Customer.objects.get(customer_id=userID)
    global customerID
    customerID = customer.id
    add, add_bill = customer.Programs, customer.bill
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("logout"):
            punch_out = str(datetime.now())
            print(punch_out)
            Customers.objects.filter(
                Customer_id=customerID).update(Punch_out=punch_out)
            p_in = datetime.strptime(Customers.objects.get(
                Customer_id=customerID).Punch_in, '%Y-%m-%d %H:%M:%S.%f')
            p_out = datetime.strptime(Customers.objects.get(
                Customer_id=customerID).Punch_out, '%Y-%m-%d %H:%M:%S.%f')
            hours = ((p_out-p_in).total_seconds())/3600
            print(hours)
            actual_bill = customer.bill * hours + \
                Customers.objects.get(Customer_id=customer.id).bill
            print(actual_bill)
            Customers.objects.filter(
                Customer_id=customer.id).update(bill=actual_bill)
            return HttpResponseRedirect("/")
        if response.POST.get("sign-in"):
            return HttpResponseRedirect("/sign-in")
        if response.POST.get("yoga"):
            if "yoga" not in add:
                add = "".join((add, "yoga "))
                Customer.objects.filter(
                    customer_id=userID).update(Programs=add)
                add_bill += 15
        if response.POST.get("circuit"):
            if "circuit" not in add:
                add = "".join((add, "circuit "))
                Customer.objects.filter(
                    customer_id=userID).update(Programs=add)
                add_bill += 30
        if response.POST.get("hiit"):
            if "hiit" not in add:
                add = "".join((add, "hiit "))
                Customer.objects.filter(
                    customer_id=userID).update(Programs=add)
                add_bill += 34
        if response.POST.get("bootcamp"):
            if "bootcamp" not in add:
                add = "".join((add, "bootcamp "))
                Customer.objects.filter(
                    customer_id=userID).update(Programs=add)
                add_bill += 40
        if response.POST.get("zumba"):
            if "zumba" not in add:
                add = "".join((add, "zumba "))
                Customer.objects.filter(
                    customer_id=userID).update(Programs=add)
                add_bill += 25
        if response.POST.get("boxing"):
            if "boxing" not in add:
                add = "".join((add, "boxing "))
                Customer.objects.filter(
                    customer_id=userID).update(Programs=add)
                add_bill += 25
        if response.POST.get("member"):
            if "membership" not in add:
                add = "".join((add, "membership "))
                Customer.objects.filter(
                    customer_id=userID).update(Programs=add)
                add_bill += 2
        if response.POST.get("trainer"):
            if "trainer" not in add:
                add = "".join((add, "trainer "))
                Customer.objects.filter(
                    customer_id=userID).update(Programs=add)
                add_bill += 10
        Customer.objects.filter(customer_id=userID).update(bill=add_bill)
    return render(response, "gymbros/programs.html", {"userID": userID})


def dashboard(response, userID):
    customer = Customer.objects.get(customer_id=userID)
    global customerID
    customerID = customer.id
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("logout"):
            punch_out = str(datetime.now())
            print(punch_out)
            Customers.objects.filter(
                Customer_id=customerID).update(Punch_out=punch_out)
            p_in = datetime.strptime(Customers.objects.get(
                Customer_id=customerID).Punch_in, '%Y-%m-%d %H:%M:%S.%f')
            p_out = datetime.strptime(Customers.objects.get(
                Customer_id=customerID).Punch_out, '%Y-%m-%d %H:%M:%S.%f')
            hours = ((p_out-p_in).total_seconds())/3600
            print(hours)
            actual_bill = customer.bill * hours + \
                Customers.objects.get(Customer_id=customer.id).bill
            print(actual_bill)
            Customers.objects.filter(
                Customer_id=customer.id).update(bill=actual_bill)
            return HttpResponseRedirect("/")
        if response.POST.get("sign-in"):
            return HttpResponseRedirect("/sign-in")
        if response.POST.get("save"):
            print(customer.weight, customer.height, customer.bmi)
            Customer.objects.filter(customer_id=userID).update(
                weight=response.POST.get("weight"))
            Customer.objects.filter(customer_id=userID).update(
                height=response.POST.get("height"))
            Customer.objects.filter(customer_id=userID).update(
                bmi=int(float(response.POST.get("weight")) / (float(response.POST.get("height")) ** 2) * 10000))
            Customer.objects.filter(customer_id=userID).update(
                name=response.POST.get("username"))
            return HttpResponseRedirect("/dashboard/%i" % userID)
        if response.POST.get("remove"):
            print(response.POST)
            remove = response.POST.get("program")
            print(remove)
            old_programs = customer.Programs
            new_programs = str(old_programs).replace(remove+" ", "")
            print(old_programs)
            print(new_programs)
            Customer.objects.filter(customer_id=userID).update(
                Programs=new_programs)
            add = customer.bill
            if "yoga" in remove:
                add -= 15
            if "hiit" in remove:
                add -= 34
            if "circuit" in remove:
                add -= 30
            if "bootcamp" in remove:
                add -= 40
            if "boxing" in remove:
                add -= 25
            if "zumba" in remove:
                add -= 25
            if "membership" in remove:
                add -= 2
            if "trainer" in remove:
                add -= 10
            Customer.objects.filter(customer_id=userID).update(bill=add)
            return HttpResponseRedirect("/dashboard/%i" % userID)
    if customer.bmi <= 20:
        msg = "You are underweight!"
        training = "BB Deadlift(12-10-8-6-Increase weight each set),Walking Dumbbell Lunge (3 sets of 10-15 reps per leg),T- Pushup(3 sets of 12 reps),T- Pushup (3 sets of 12 reps),Bench Dips (3 sets of 15-20 reps),Close-Grip Chin-ups 3 sets of 10-12 reps (can use machine or band for assistance if needed),Renegade (Row 3 sets of 8 reps per side ),Hanging Leg Raises  (3 sets of 20 reps),Swiss Ball Pass (3 sets of 20 reps)"
    elif customer.bmi <= 25:
        msg = "You are perfectly healthy!"
        training = "Rotating plank (30 secs x 4),Plate thrusters (15 reps x 3 sets),Mountain climbers (20 reps x 3 sets),Box jumps (10 reps x 3 sets),Walk outs (10 reps x 3 sets),Renegade rows (full plank/kneeling) (10 each side x 3 sets),Press ups (full plank/kneeling) (15 reps x 3 sets),Treadmill 10 min run/steep incline brisk walk (no hands),Supermans (full plank/kneeling) (10 reps x 3 sets),Crunches (10 reps x 3 sets)."
    elif customer.bmi <= 30:
        msg = "You are overweight!"
        training = "Barbell push press (6 reps x 4 sets),Goblet squat (6 reps x 4 sets),Dumbbell single arm row (6 reps x 4 sets),Shoulder lateral raise (6 reps x 4 sets),Bench press (6 reps x 4 sets),Pull ups/assisted pull ups (6 reps x 4 sets),Barbell bicep curls (8 reps x 4 sets),Cable overhead tricep extensions (8 reps x 4 sets)"
    elif customer.bmi <= 40:
        msg = "You are obese!"
        training = "Seated chest press (10 reps x 4 sets),Seated rows (10 reps x 4 sets),Wide grip lat pulldown (10 reps x 4 sets),Seated leg press (10 reps x 4 sets),Dumbbell seated shoulder press (10 reps x 4 sets),Dumbbell bicep curls (10 reps x 4 sets),Close grip tricep press ups (10 reps x 4 sets),Cable rotations/twists (10 reps x 4 sets),Reverse crunches (10 reps x 4 sets)"
    return render(response, "gymbros/dashboard.html", {"userID": userID, "name": customer.name, "programs": customer.Programs.replace(" ", " | "), "bill": customer.bill, "bmi": customer.bmi, "msg": msg, "training": training, "payment": Customers.objects.get(Customer_id=customer.id).bill, "weight": customer.weight, "height": customer.height})


def ux(response, userID):
    customer = Customer.objects.get(customer_id=userID)
    global customerID
    customerID = customer.id
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("logout"):
            punch_out = str(datetime.now())
            print(punch_out)
            Customers.objects.filter(
                Customer_id=customerID).update(Punch_out=punch_out)
            p_in = datetime.strptime(Customers.objects.get(
                Customer_id=customerID).Punch_in, '%Y-%m-%d %H:%M:%S.%f')
            p_out = datetime.strptime(Customers.objects.get(
                Customer_id=customerID).Punch_out, '%Y-%m-%d %H:%M:%S.%f')
            hours = ((p_out-p_in).total_seconds())/3600
            print(hours)
            actual_bill = customer.bill * hours + \
                Customers.objects.get(Customer_id=customer.id).bill
            print(actual_bill)
            Customers.objects.filter(
                Customer_id=customer.id).update(bill=actual_bill)
            return HttpResponseRedirect("/")
        if response.POST.get("sign-in"):
            return HttpResponseRedirect("/sign-in")
        if response.POST.get("send"):
            username = response.POST.get("name")
            email = response.POST.get("email")
            comment = response.POST.get("comment")
            with open('ux.txt', 'a') as file:
                user_string = str(User.objects.get(id=userID)) + "\n"
                form_string = "username : " + username + "\nemail : " + \
                    email + "\ncomment : " + comment + "\n\n"
                file.writelines(
                    'User Experience Response from : ' + user_string + form_string)
    return render(response, "gymbros/ux.html", {"userID": userID})
