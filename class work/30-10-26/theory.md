=> for loop:-

syntax:-
1. for reference in collection:
        #logic or statement
    
2. for reference in range(start, stop-1, step):
        #logic or statement

=> range() is a predefined function in python.
1. start default value is 0
2. stop runs n-1
3. step default value is increment by 1

=====================================================================

=> break:-
- break statement is used to terminate a process when the given condition is satisfied.


=> continue:-
- continue only skip the value from the process when the given condition is satisfied and rest of the loop process will run as it is.


=> exit() :-
- it is a pre defined function of python which terminate a program with or without passing condition. for using this function first import sys module.


=> ord():-
- ord function returns ascii value of given character(number/symbols)


=> char():-
- this function returns char value of given ascii code


=> pass statement :-
- if you dont want to write any logic then use pass as a null statement inside the indentant block 

=> nested for in loop :-
- a loop within a loop is called nested for in loop.

syntax:-
#inner loop for rows
for i in range(start, stop-1, step):
        logic or statement

        #outer loop for columns:
        for i in range(start, stop-1, step):
            logic or statement

* *
* *
i=1 i<3 yes
loop goes to j
  j = 1 j<3 yes
  j=2 j<3 yes
  j=3 j<3 terminate 

i=2 i<3 yes
  j=1 j<3 yes
  j=2 j<3 yes
  j=3 j<3 terminate

i=3 i<3 terminate

1. 
a
a b
a b c

2. 
A
A B
A B C

3. 
1
2 3
4 5 6

4. 
1
1 3
1 3 5