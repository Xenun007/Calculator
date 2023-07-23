num = 5
print (f'{num} is of the type {type(num)}')  #prints the data type of what it is holding
num = str(num)
print (f'{num} is of the type {type(num)}')  #prints the data type of what it is holding after type casting
age = int(input("How old are you\t"))
name = input("What is your name\t")
print(f'{name} is {age} years old')
count = 0
if age > 18:
    print("you are old")
elif age < 18:
    print("U are young")
else:
    print("You are 18")
print(name)
for x in name:
    print(x)
    if x == "y":
        count+=1        
print(f'There are {count} ys in your name')
number =  int(input("Enter max number"))
while number < 10:
    number =  int(input("Enter max number"))
for x in range(0,11,2):
    print(x)