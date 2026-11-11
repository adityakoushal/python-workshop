Given Data
a = ['a', 'b', 'c', 'd', 'e']



1. Positive Index Slicing
print(a[0:3])print(a[1:4])print(a[0:5])print(a[2:5])



Output:
['a', 'b', 'c']
['b', 'c', 'd']
['a', 'b', 'c', 'd', 'e']
['c', 'd', 'e']


2. Negative Index Slicing
print(a[-1])print(a[-3:])print(a[:-2])print(a[-4:-1])



Output:
e
['c', 'd', 'e']
['a', 'b', 'c']
['b', 'c', 'd']


3. Slicing with Step
print(a[::1])print(a[::2])print(a[::-1])print(a[::-2])



Output:
['a', 'b', 'c', 'd', 'e']
['a', 'c', 'e']
['e', 'd', 'c', 'b', 'a']
['e', 'c', 'a']


4. Slicing Syntax
list[start : stop : step]
