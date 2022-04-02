Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
a=np.arange(10).reshape(2,5)
a
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
b=np.arange(10,20).reshape(2,5)
b
array([[10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
a[1]
array([5, 6, 7, 8, 9])
c=np.arange(10)
c
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
c[2]
2
c[2:4]
array([2, 3])
a[1,3]
8
a[-1]
array([5, 6, 7, 8, 9])
a[-1,1:5]
array([6, 7, 8, 9])


print("Now iterating the numpy array")
Now iterating the numpy array
a.reshape(5,2)
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])
a
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
a=a.reshape(5,2)
a
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])
for row in a:
    print(row)

[0 1]
[2 3]
[4 5]
[6 7]
[8 9]
for cell in a.ravel():
    print(cell)

    
0
1
2
3
4
5
6
7
8
9
for cell in a.flat:
    print(cell)

    
0
1
2
3
4
5
6
7
8
9
a.flat
<numpy.flatiter object at 0x000002AE526DFBD0>
a.ravel()
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




print("Now stacking of arrays")
Now stacking of arrays
a
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])
b.reshape(5,2)
array([[10, 11],
       [12, 13],
       [14, 15],
       [16, 17],
       [18, 19]])
a
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])
b
array([[10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
b=b.reshape(5,2)
b
array([[10, 11],
       [12, 13],
       [14, 15],
       [16, 17],
       [18, 19]])
a
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])
b
array([[10, 11],
       [12, 13],
       [14, 15],
       [16, 17],
       [18, 19]])
np.hstack((a,b))
array([[ 0,  1, 10, 11],
       [ 2,  3, 12, 13],
       [ 4,  5, 14, 15],
       [ 6,  7, 16, 17],
       [ 8,  9, 18, 19]])
np.vstack((a,b))
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15],
       [16, 17],
       [18, 19]])
a
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])
b
array([[10, 11],
       [12, 13],
       [14, 15],
       [16, 17],
       [18, 19]])
np.hsplit(a,2)
[array([[0],
       [2],
       [4],
       [6],
       [8]]), array([[1],
       [3],
       [5],
       [7],
       [9]])]
d=np.hsplit(a,2)
d[0]
array([[0],
       [2],
       [4],
       [6],
       [8]])
d[1]
array([[1],
       [3],
       [5],
       [7],
       [9]])
a.vsplit(a,5)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.vsplit(a,5)
AttributeError: 'numpy.ndarray' object has no attribute 'vsplit'
np.vsplit(a,5)
[array([[0, 1]]), array([[2, 3]]), array([[4, 5]]), array([[6, 7]]), array([[8, 9]])]
e=np.vsplit(a,5)
for row in e:
    prnt(row)

    
Traceback (most recent call last):
  File "<pyshell#57>", line 2, in <module>
    prnt(row)
NameError: name 'prnt' is not defined. Did you mean: 'print'?
for row in e:
    print(row)

    
[[0 1]]
[[2 3]]
[[4 5]]
[[6 7]]
[[8 9]]

print("Thats all about indexing and slicing and stacking")
Thats all about indexing and slicing and stacking
Print("Now indexing of boolean arrays")
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    Print("Now indexing of boolean arrays")
NameError: name 'Print' is not defined. Did you mean: 'print'?
print("Now indexing of boolean arrays")
Now indexing of boolean arrays
a
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])
b=a>4
b
array([[False, False],
       [False, False],
       [False,  True],
       [ True,  True],
       [ True,  True]])
a[b]
array([5, 6, 7, 8, 9])
a[b]=0
a
array([[0, 1],
       [2, 3],
       [4, 0],
       [0, 0],
       [0, 0]])
print("I have replaced the numbers greater than 4 with zero(0)")
I have replaced the numbers greater than 4 with zero(0)
