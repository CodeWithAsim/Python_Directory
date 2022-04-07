def tot_expense(exp):
    total=0
    for i in exp:
        total=total+i
    return total

Asim_exp=[100,200,300,500]
total=tot_expense(Asim_exp)
print("Total Expense of Asim is :",total)