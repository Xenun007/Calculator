file1 = open("testfile.txt")
content = file1.read()
print(content)
file1.close()
with open("testfile.txt") as f:
    whut = f.read()
    print(whut)
with open("new.txt",'r+') as f:
    details = f.read()
    print(details)
    f.writelines("I love you\n")
    f.write("""line1
    line2
    line3""")
    details = f.read()
    print(details)