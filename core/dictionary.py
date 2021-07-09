#key value pair

books={'isbn':254678, 'name':'Mastering Python','author':'xyz', 'cost':567,'active':True}

#get the values
for _ in books.keys():
    print(_,'=>',books[_])


 # get the values
for _ in books.values():
    print(_)


#key and value
for (key,value) in books.items():
    print(key,'->',value)