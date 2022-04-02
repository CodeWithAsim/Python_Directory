Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("now learn about dictionaries")
now learn about dictionaries
>>> d={"asim":42367,"afzal":374617,"adeel":772315}
>>> d
{'asim': 42367, 'afzal': 374617, 'adeel': 772315}
>>> d["asim"]
42367
>>> d["afzal"]
374617
>>> d["aqib bhai"]=73278184
>>> d
{'asim': 42367, 'afzal': 374617, 'adeel': 772315, 'aqib bhai': 73278184}
>>> del d["asim"]
>>> d
{'afzal': 374617, 'adeel': 772315, 'aqib bhai': 73278184}
>>> "asim" in d
False
>>> "afzal" in d
True
>>> for i in d:
	print("key is :",i,"and valueis :",d[i])

key is : afzal and valueis : 374617
key is : adeel and valueis : 772315
key is : aqib bhai and valueis : 73278184
>>> for i in d:
	print("key is :",i,"and value is :",d[i])

	
key is : afzal and value is : 374617
key is : adeel and value is : 772315
key is : aqib bhai and value is : 73278184
>>> for v,k in d.items()
SyntaxError: invalid syntax
>>>  for v,k in d.items():
	 
SyntaxError: unexpected indent
>>> for v,k in d.items():
	print("key is :",v,"and value is :",k)

	
key is : afzal and value is : 374617
key is : adeel and value is : 772315
key is : aqib bhai and value is : 73278184
>>> d["afzal"]=123
>>> d
{'afzal': 123, 'adeel': 772315, 'aqib bhai': 73278184}
>>> 
>>> 
>>> print("now learn tuples")
now learn tuples
>>> point=(2,3)
>>> point
(2, 3)
>>> point[0]
2
>>> point[1]=4
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    point[1]=4
TypeError: 'tuple' object does not support item assignment
>>> point=("h2 block","johar town lahore",445)
>>> point
('h2 block', 'johar town lahore', 445)
>>> 
