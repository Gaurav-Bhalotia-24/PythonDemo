# This program is to demonstrate basic IO in python
firstname=input("Enter first name")
# Check for data type
print(type(firstname))
try:
    age=int(input("Enter your age"))
    print(type(age))
except ValueError as err:
    print("Value Exception", err)
print("First Name=%s" %(firstname))
print("Age=%d" %(age))
