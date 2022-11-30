from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import *
from workers.models import *
from .forms import*

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
            actual_bill = Customer.objects.get(customer_id=userID).bill * hours
            Customers.objects.filter(
                Customer_id=userID).update(bill=actual_bill)
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
                                weight=w, height=h, bmi=w**2/h, Programs='', bill=0)
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
    add, add_bill = Customer.objects.get(
        customer_id=userID).Programs, Customer.objects.get(customer_id=userID).bill
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
            actual_bill = Customer.objects.get(customer_id=userID).bill * hours
            Customers.objects.filter(
                Customer_id=userID).update(bill=actual_bill)
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
            actual_bill = Customer.objects.get(customer_id=userID).bill * hours
            Customers.objects.filter(
                Customer_id=userID).update(bill=actual_bill)
            return HttpResponseRedirect("/")
        if response.POST.get("sign-in"):
            return HttpResponseRedirect("/sign-in")
        if response.POST.get("remove"):
            print(response.POST)
            remove = response.POST.get("program")
            print(remove)
            old_programs = customer.Programs
            new_programs = str(old_programs).replace(remove+" ", "")
            print(old_programs)
            print(new_programs)
            Customer.objects.filter(customer_id=userID).update(Programs=new_programs)
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
    return render(response, "gymbros/dashboard.html", {"userID": userID, "name": customer.name, "programs": customer.Programs.replace(" ", " | "), "bill":customer.bill})


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
            actual_bill = Customer.objects.get(customer_id=userID).bill * hours
            Customers.objects.filter(
                Customer_id=userID).update(bill=actual_bill)
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
