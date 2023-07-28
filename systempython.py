import os
here = os.getcwd()
os.chdir("C:\\Users\\Xenun-Makuzi\\Documents")
new_here = os.getcwd()
print(here)
print(new_here)
alls = os.listdir()
print(alls)
print("women.txt" in alls)
with open("women.txt") as f:
    content =  f.read()
    print(content)