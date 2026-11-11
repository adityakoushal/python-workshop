Identity operators are used to compare the memory identity of two objects. They check whether two variables refer to the same object or not.

Python has 2 identity operators:
1. is Operator
It returns True if both variables refer to the same object.
a = [10, 20, 30]b = aprint(a is b)



Output:
True


2. is not Operator
It returns True if both variables do not refer to the same object.
a = [10, 20, 30]b = [10, 20, 30]print(a is not b)



Output:
True


Difference Between is and ==
a = [10, 20, 30]b = [10, 20, 30]print(a == b)print(a is b)



Output:
True
False


Explanation:
- == checks whether values are equal.
- is checks whether both variables refer to the same object.
Summary
Operator	Meaning
is	Same object
is not	Different objects