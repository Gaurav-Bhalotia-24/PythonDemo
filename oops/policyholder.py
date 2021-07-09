#class
import datetime

class PolicyHolder:
    companyName="PwC"

    @staticmethod
    def PolicyInfo():
        print("Jeevan Dhara")

    def __init__(self):
       pass

    def __init__(self,adharCardNo,name,dob):
        self.__adharCardNo=adharCardNo
        self.__name=name
        self.__dob=dob

    def showValues(self):
        print(self.__adharCardNo)

    def setAdharCardNo(self,value):
        self.__adharCardNo=value


    def getAdharCardNo(self):
         return self.__adharCardNo

policyHolder=PolicyHolder('A2835872','Gaurav',datetime.date(1070,12,2))

print(policyHolder.getAdharCardNo())
policyHolder.setAdharCardNo("A47578")
print(policyHolder.getAdharCardNo())
print(policyHolder.companyName)
policyHolder.PolicyInfo()

