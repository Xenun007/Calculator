ages = [19,18,20,34,"you"]
name = ["Xenun","Eddy","Suprime"]
print(f'{name[1]} is {ages[2]} years old')
last = ages[1:]
last_element = name[-1]
from_first = name[:]
between = ages[1:3]
print(from_first,between,last_element)
even = [0,2,4,6,8]
odd = [1,3,5,7,9]
even.insert(0,"even")       #inserts element at a specified
print(even)
even.append(10)     #adds an element at the last index of the array
complete = even.extend(odd)   #adds an entire iterable data type to current list
del even[0]  # del even[a:b]  same as normal list programming
even.sort()
count = even.count(2)
deletd = even.pop(3)
even.reverse
print(2 in even)  # checks if the number 2 is in the list
print(len(even)) # prints the length of the list
        #list comprehension
squares = [n**2 for n in range(1,5)]  # efecient way of creating defined list
print(squares)
print(even)
#even.extend(odd)  doing this will overwrite the even value to the extended value
print(complete)