
x = 'Hello world'
print(x)
x = "Hello world"
print(x)
x = """This is
    a paragraph"""
print(x)
x = "escaping single quote in father's name"
print(x)
x = 'escaping double quotes of "Mother"'
print(x)
x = "Banana"
#length
print(len(x))
#index
print(x[3])
#loop
for i in x:
    print(i)

txt = "This is a free text"
print("free"in txt)
print("Busy" not in txt)

#Slicing
text = "Hello world"
print(text[2:5]) #llo
print(text[:5]) #Hello
print(text[6:]) # world
print(text[-2:]) # ld
print(text[-5:-2]) #wor
print(text.upper())
print(text.lower())
text = "Hello world   "
print(text.strip()) # Hello world
print(text.replace("H", "B"))
print(text.strip(" ").split(" "))
a = "Hello"
b = "World"
c = a+" "+b
print(c)

age = 33
text = f"My name is Balaji and I am {age}"
print(text)
amount = 32
text = f"I have {amount:.3f} rupees"
print(text) #I have 32.000 rupees
txt = f"The price is {20 * 59} dollars"
print(txt)


