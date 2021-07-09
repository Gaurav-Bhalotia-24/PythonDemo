import requests

findData=requests.get("https://jsonplaceholder.typicode.com/users",verify=False)
#print(findData)

for _ in findData.json():
    print(_)