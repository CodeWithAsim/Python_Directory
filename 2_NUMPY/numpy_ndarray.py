Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
a1=np.array([1,2,3,4,5])
a1
array([1, 2, 3, 4, 5])
a=np.array([1,2,3,4,5])
a
array([1, 2, 3, 4, 5])
a.size
5
a.itemsize
4
a.dtype
dtype('int32')
a.ndim
1
a2=np.array([[1,2],[2,3],[4,5]])
a2
array([[1, 2],
       [2, 3],
       [4, 5]])
a2.ndim
2
a2.size
6
a.shape
(5,)
a2.shape
(3, 2)
a=np.zeros((3,2))
a
array([[0., 0.],
       [0., 0.],
       [0., 0.]])
a.shape
(3, 2)
a.reshape(2,3)
array([[0., 0., 0.],
       [0., 0., 0.]])
a.reshape(6,)
array([0., 0., 0., 0., 0., 0.])
a.ravel
<built-in method ravel of numpy.ndarray object at 0x000002AC5DBE8630>
a.ravel()
array([0., 0., 0., 0., 0., 0.])
np.arange(20)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])
np.linspace(1,10,2)
array([ 1., 10.])
np.linspace(1,7)
array([1.        , 1.12244898, 1.24489796, 1.36734694, 1.48979592,
       1.6122449 , 1.73469388, 1.85714286, 1.97959184, 2.10204082,
       2.2244898 , 2.34693878, 2.46938776, 2.59183673, 2.71428571,
       2.83673469, 2.95918367, 3.08163265, 3.20408163, 3.32653061,
       3.44897959, 3.57142857, 3.69387755, 3.81632653, 3.93877551,
       4.06122449, 4.18367347, 4.30612245, 4.42857143, 4.55102041,
       4.67346939, 4.79591837, 4.91836735, 5.04081633, 5.16326531,
       5.28571429, 5.40816327, 5.53061224, 5.65306122, 5.7755102 ,
       5.89795918, 6.02040816, 6.14285714, 6.26530612, 6.3877551 ,
       6.51020408, 6.63265306, 6.75510204, 6.87755102, 7.        ])
np.linspace(1,5,1)
array([1.])
np.linspace(1,5,5)
array([1., 2., 3., 4., 5.])
np.arange(1,6,2)
array([1, 3, 5])
np.arange(1,6)
array([1, 2, 3, 4, 5])
a
array([[0., 0.],
       [0., 0.],
       [0., 0.]])
a2=np.array([[1,2],[2,3],[4,5]])
a2
array([[1, 2],
       [2, 3],
       [4, 5]])
a2.min()
1
a2.max()
5
a2.sum()
17
a2.sum(axis=1)
array([3, 5, 9])
a2.sum(axis=0)
array([ 7, 10])
np.std(a2)
1.3437096247164249
np.sqrt(a2)
array([[1.        , 1.41421356],
       [1.41421356, 1.73205081],
       [2.        , 2.23606798]])
a.sqrt()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.sqrt()
AttributeError: 'numpy.ndarray' object has no attribute 'sqrt'. Did you mean: 'sort'?
a=np.arange(1,10)
a
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b=np.arange(10,20)
b
array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
type(a)
<class 'numpy.ndarray'>
a.dtype
dtype('int32')
a+b
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a+b
ValueError: operands could not be broadcast together with shapes (9,) (10,) 
b=np.arange(1,10)
a+b
array([ 2,  4,  6,  8, 10, 12, 14, 16, 18])
a*b
array([ 1,  4,  9, 16, 25, 36, 49, 64, 81])
a-b
array([0, 0, 0, 0, 0, 0, 0, 0, 0])
b-a
array([0, 0, 0, 0, 0, 0, 0, 0, 0])
a/b
array([1., 1., 1., 1., 1., 1., 1., 1., 1.])
a.dot(b)
285
