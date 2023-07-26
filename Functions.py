def add(a,b):
    return a+b
def fac(x):
    fact = 1
    if x == 0:
        return 1
    while x < 0:
        x = int(input("Enter a proper number"))
    while x > 1:
        fact *=x
        x-=1
    return fact
print(fac(add(3,2)))
def add_n(*infinite):
    sum =0;
    for i in infinite:
        sum+=i
    return sum
print(fac(add_n(1,2,2)))