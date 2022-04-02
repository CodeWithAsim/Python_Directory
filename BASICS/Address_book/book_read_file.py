f=open("D:\\Python_Code\\Address_book\\address.txt","r")
address=f.read()
f.close()
print(address)

import json
address=json.loads(address)

print(address)

print(address["asim"])

print(address["asim"]["ph number"])

for item in address:
    print(address[item])