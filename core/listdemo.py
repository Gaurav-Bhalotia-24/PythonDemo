from pylibrary import customersort
projectList=['P1','P2','P3']
companyList=['C1','C2','C3']

#output p1,c1 p2,c2 p3,c3
#zip is used to get cross product

for(x,y) in zip(projectList,companyList):
    print(x,'=>',y)

import random
import datetime

customers=[]
for _ in range(100):
    customer=[random.randint(1,10000),'customer'+str(_),
              datetime.date(random.randint(1970,2021),
                            random.randint(1,11),random.randint(1,26))
                  #.strftime('%d-%m-%Y')
              ]
    customers.append(customer)

#print customers
for _ in customers:
      print(_)
print("****************************************************************")

customers.sort(key=customersort.sort,reverse=False)
#reverse is used to sort in asc and disc order(true is desc, false is asc)

for _ in customers:
    print(_)
