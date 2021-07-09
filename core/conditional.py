import random

data=random.randint(1,10000)

if data<=1027:
    print("System port")
elif(data>1027)and(data<5000):
    print("Application port")
else:
    print("custom port")
    