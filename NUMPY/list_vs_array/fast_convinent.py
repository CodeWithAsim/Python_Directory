import sys
import numpy as np
import time

l1 = range(1000000)
l2 = range(1000000)

a1 = np.arange(1000000)
a2 = np.arange(1000000)

print("For list processing")
# capturing the time
start = time.time()
# help of list comprehension
result = [(x+y) for x, y in zip(l1, l2)]
# bcz by default time is in seconds
print("Total time taken for addition in lists : ", (time.time()-start)*1000)

print("For array processing")
start = time.time()
result = a1 + a2
print("Total time taken for addition in arrays : ", (time.time()-start)*1000)

print("-------------------------------------")
print("So arrays are fast and convient by syntax vise")
