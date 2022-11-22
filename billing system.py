options = {1:4, 2:20, 3:200}

# general gym subscription
if (input("Do you want to join the gym membership? (Y/N)").lower()) == 'n':
    option = 3
    print("Your daily subscription is : $4")
else:
    if (input("Do you want a monthly or a yearly subscription ? (Y/M)").lower() == 'm'):
        option = 2
        print("your ")
    else:
        option = 1

# trainer
if (input("Do you want a personal trainer? (Y/N)").lower()=='n'):
    pass
else:
    add = 10
    print("$10 will be added to each session")

# classes


