import re

re_pattern=r"[A-Za-z]{5,25}"
userName=input("Enter Name")
result=re.search(re_pattern,userName)
if(result):
    print("Match Found")
else:
    print("Match not found")


re_pattern = r"(?=.[A-Z])(?=.[0-9])(?=.[!@#\$%\^&\])(?=.{4,})"
password = input("Enter Password")
result = re.search(re_pattern, password)
if (result):
  print("Match Found")
else:
  print("Match not found")