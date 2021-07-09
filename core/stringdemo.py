org=" Rps consulting Servives"

print(org.capitalize())
print(org.center(len(org)+40, "*"))
print(org.ljust(len(org)+40, "*"))
print(org.rjust(len(org)+40, "*"))
print(org.upper())

import random
import base64
seqNo=random.randint(1,700)
encodedData=base64.b64encode(str(seqNo).
                             encode(encoding='utf-8',errors='strict'))

#print(encodedData)
for _ in encodedData[0:]:
    print(chr(_),end="")

#decode the data
decodedData=base64.b64decode(encodedData.decode(encoding='utf-8', errors='strict'))
print(decodedData)

# print(encodedData)
for _ in encodedData[0:]:
    print(chr(_), end="")
