import random

#sample change
def method1():
    # shift by alphabet
    shift = random.randint(1, 27)
    ceasar = {}
    cipher=""
    for char in range(33, 126):
        ceasar[chr(char)] = (chr(((char) + shift-33) % 26 + 33) )
    for i in range(len(password)):
        cipher += ceasar[password[i]]
    return cipher

def method2():
    if( text == None)or( text == ''):
        return text
    sel="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;-?! \'()$%&\""
    Region = []
    Region += sel
    encrypted_text = ""
    text = list(text)
#     step 1
    i = 0
    for char in text:
        if i%2:
            text[i]= char.upper()
        i += 1
#         step 2
    encrypted_text += Region[::-1][Region.index(text[0])]
    for i in range(1, len(text) ):
        if text[i]not in Region:
            raise Exception("INVALID PASSWORD : should contain : .,:;-?! \'()$%&\"")
        difference = Region.index(text[i-1]) - Region.index(text[i])
        if difference < 0:
            region_index = difference + 77
        else:
            region_index = difference
        encrypted_text +=  Region[region_index]
    return encrypted_text

def method3():
    # convert to alphabet then do some math then reconvert
    pass

def method4():
    # shift by ascii value
    pass

def method5():
    # modify ascii value by math
    pass


print("welcome to the gym manager app")
print("sign in tab")
print("___________")

name = (input("Enter username:"))
password = input("Enter password:")

# now we need to modify the password

keys={
    1:method1,
    2:method2,
    3:method3,
    4:method4,
    5:method5,
}

method_key = (len(password)-1)%5 + 1
method = keys.get(method_key)()

print(method_key, method)
# after i know what method i will use to modify the pass, i will define each method and change the password accordingly

password = method
print(password)

'''
check username and pass in file database

if admin display some utility page for the gym managers:

Home Customers Employees Facility

if user display some user stuff:

Home Dashboard Programs UserExperience Information
'''
