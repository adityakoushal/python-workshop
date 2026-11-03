1. Python lists:- 
 python lists are just like dynamically sized arrays, declared in other language, In simple language, a python list is a collection of data enclosed in [ ] and seperated by commas.

 1. list is a collecyion of similar + different - different data type values
 2. python list define in [ ] brackets 
 3. list is mutable(changeable) in nature.
 4. list is oredered(default index start with 0).
 5. it allow duplicate elements.
 6. list is also a constructor in python.
 7. it is dynamic in nature. no need to define size in prior.

  syntax:- 
    ref_var_name = [value1, value2 , ....]

    exp, a =[1,2,3]


# list methods
1. append():- to add new data in list at the end
# syntax:- listname.append(value)

2. pop():- this method remove the element from the list at the end/last position.
its use with or without passing arguments.
# syntax:- listname.pop() or listname.pop(index)

3. remove():- for remove an element from the list.
# syntax:- listname.remove(value)

4. sort():- arrange list element in ascending order.
# syntax:- listname.sort()

for descendng order write
# syntax:- listname.sort(reverse=true)

5. reverse():- arrange list in reverse order.
# syntax:- listname.reverse()

6. insert():- this method insert a new element at specified index position.
# syntax:- listname.insert(index, value)
note: if the given index is not found it will not generate exceptio. it will add the element at the end of the list.

7. count():- this function count duplicate element in a given list.
return informat = listname.count(value)

8. clear():- for clear an existing list data.after clear list structure will be exists.
# syntax:- listname.clear()

9. copy():- it will create a new list from the existing  list data.
# syntax:- varname = listname.copy()

10. index():- return index of specified value.
# syntax:- return index = listname.index(value)

11. extend():- add elements from another list.
# syntax:- listname1.extend(listname2)

=====================================================================

* del:- del is a reserve word or keyword for delete any reference(or de-allocate an existing reference from memory permanently).
# syntax:- ref_var_name