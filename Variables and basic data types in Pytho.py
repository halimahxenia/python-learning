#Variables and basic data types in Python
x = 1         # assign variable x the value 1
y = x + 5     # assign variable y the value of x plus 5
z = y         # assign variable z the value of y

x = True
print(type(x)) # outputs: <class 'bool'>

x = 'This is a string'
print(x) # outputs: This is a string
print(type(x)) # outputs: <class 'str'>
y = "This is also a string"

name = input('Enter your name:') #input lets you read from the command line
print(name)