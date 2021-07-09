import datetime

print(datetime.datetime.today())
print(datetime.datetime.today().strftime("%d/%m/%Y"))
# calculate the experience

doj=datetime.date(1991,6,2)
exp=datetime.date.today()-doj
print(int(exp.days/365))