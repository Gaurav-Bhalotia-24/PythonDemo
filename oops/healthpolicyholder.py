from oops import policyholder
import datetime
class HealthPolicyHolder(policyholder.PolicyHolder):

    def __init__(self,adharCardNo,name,dob,medicalHistory):
        policyholder.PolicyHolder.__init__(self,adharCardNo,name,dob)
        self.__medicalHistory=medicalHistory

    def setMedicalHistory(self,value):
        self.__medicalHistory=value

    def getMedicalHistory(self):
        return self.__medicalHistory


healthPolicyHolder=HealthPolicyHolder("A245378","Gaurav",datetime.date(1970,12,2),"Good")
healthPolicyHolder.getMedicalHistory()