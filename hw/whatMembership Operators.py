Membership operators are used to check whether a particular element is present in a sequence (list, tuple, string, set, etc.) or not.

Python has 2 membership operators:
1. in Operator
It returns True if an element is present in the sequence.

Example:
a = [10, 20, 30, 40, 50]print(20 in a)print(60 in a)



Output:
True
False


2. not in Operator
It returns True if an element is not present in the sequence.

Example:
a = [10, 20, 30, 40, 50]print(60 not in a)print(20 not in a)



Output:
True
False


3. Membership Operator in String
a = "Python Programming"print("Python" in a)print("Java" in a)print("Java" not in a)



Output:
True
False
True


4. Membership Operator in Tuple
t = (10, 20, 30, 40)print(10 in t)print(50 not in t)



Output:
True
True


Difference Between in and not in
Operator	Meaning
in	Checks whether an element is present.
not in	Checks whether an element is absent.