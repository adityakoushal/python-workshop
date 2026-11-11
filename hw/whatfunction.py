What is id() function in Python?
The id() function is a built-in Python function that returns the unique identity (integer ID) of an object during its lifetime.
1. Syntax
id(object)



2. Example
a = 10b = 20c = 10print(id(a))print(id(b))print(id(c))



Output: (Example IDs)
140721234
140721567
140721234


Here:
- a and c have the same value, so they may refer to the same object.
- b has a different value and usually has a different ID.
3. Example with List
a = [10, 20, 30]print(id(a))a.append(40)print(id(a))



The ID remains the same because we modified the existing list object.
Exam Definition
The id() function in Python is used to return the unique identity of an object. It helps identify whether two variables refer to the same object.

Remember:
- type() → Finds data type.
- id() → Finds object identity.
- len() → Finds length.