#create dynamic employee list with id, name and age
import random
employeeList=[]

for _ in range(50):
    employee=(random.randint(1,100000),'employee'+str(_),random.randint(1,100))
    employeeList.append(employee)

print(employeeList)