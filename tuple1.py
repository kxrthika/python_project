"""Write a program to perform the following
 operations: 1. Create a tuple with different 
 datatypes 2. Create another tuple of integers 
 3. Create a new tuple by adding 9 to the previous
   tuple 
 4. Count the occurrences of an element in the tuple 
5. Perform slicing on the tuple"""

a = (1,2,2,4.5,True,"mango")
b = (2,3,5,6)
c = b+(9,)
print (a.count(2))
print (a[2:6])
