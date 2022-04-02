total=0
def sum(a,b=0):

    """
                    the way to add the documentation strings in the functions
    :param a:
    :param b:
    :return:

    """
    print("a:",a)
    print("b:", b)
    total=a+b
    print("total inside the function :", total)
    return total

x=2
y=6
n=sum(b=x,a=y)
print("sum from the function :",n)
print("total outside the function :",total)