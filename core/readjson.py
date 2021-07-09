import json
import os

#file=open("user.json")
if(os.path.exists("user.json")):
    print("File Available")
    file=open("user.json")
    data=json.load(file)
    for _ in data["users"]:
        for (key,value) in _.items():
            if(key=='username'):
                print(_[key],end="\t")
            if(key=='email'):
                print(_[key],end="\n")

else:
     print("File not Available")