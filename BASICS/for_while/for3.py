expense=[100,200,300,400,500,1200]
total=0
for i in range(len(expense)):
    print("Month :",i+1,"Expense :",expense[i])
    total=total+expense[i]
print("Total espense is : ",total)