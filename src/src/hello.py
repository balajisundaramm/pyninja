import sys

print("Hello world")
print(sys.version)

#Indentation
if(5>2):
    print("5 is greater than 2")

#Variable
#Type of
x="JOHN"
print(x)
print(type(x))

#Assign Multiple values
x,y,z="orange","Apple","Banana"
print(x)
print(y)
print(z)

#Spacing
print(x,y,z) #orange Apple Banana
print(x+y+z) # orangeAppleBanana


#Unpack a collection
fruits = ['apple', 'banana', 'orange']; x,y,z = fruits
print(x)
print(y)
print(z)

fruits = ['apple', 'banana', 'orange', 'mango']
x, y, *z = fruits;
print(x)
print(y)
print(z)

#Global Variable
x = "awesome"

def myFunc():
    print("Python is", x)

myFunc()

def myFunc():
    x = "Fantastic"
    print("Python is "+x)

myFunc()
print("Python Global variable value is", x)

#Change local variable to global

def myFunc():
    global x
    x = "local variable converted into global"

myFunc()

print(x)