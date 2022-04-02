x=input("Enter first number : ")
y=input("Enter second number : ")

try :
    z=x/int(y)
except ZeroDivisionError as e:
    print("Division by zero occurred")
    z= None
except Exception as e:
    print("Exception occurred :", type(e).__name__)
    z=None

print("Division result is : ",z)