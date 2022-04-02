book={}

book["asim"]={
    "address":"445 johar town lahore",
    "ph number":"387567",
    "zipcode":"52471"
}

book["hassan"]={
    "address":"543 cannal garden town lahore",
    "ph number":"35446567",
    "zipcode":"55471"
}

print(book)

import json
book = json.dumps(book)

with open("D:\\Python_Code\\Address_book\\address.txt","w") as f:
    f.write(book)


