import datetime
#create customer list
customer=[28458,'gaurav',560000]
currentTime=datetime.datetime.now().hour
def fundTransfer(fromAccountNo,toAccountNo,amount):
    if(fromAccountNo==customer[0]):
        if(amount<customer[2]):
            if(currentTime<18):
                print("Fund Transfer Initiated")
            else:
                print("Money will transfer in next working Day")
        else:
            print("Limit exceeded")