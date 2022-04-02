import numpy as np
import sys

l1 = range(1000)
print("* List takes bytes : ")
print(sys.getsizeof(1)*len(l1))

a1 = np.arange(1000)
print("* Array takes bytes : ")
print(a1.size*a1.itemsize)

print("So array consumes less memory and bcz in python every thing is obj and it takes 14 bytes")




