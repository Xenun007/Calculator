string1 = "i love you"
string2 = "I hate you"
long_string = '''
The quick brown
fox jumps over the 
lazy frog
'''
print(string1)
up = string1.upper()
print(string1)
singles = long_string.split(' ') # splits the string where ever it sees what is in the bracket and retrns them as  a list
print(singles)
replaced = string1.replace("love", "fucked")  # replaces what ever with whatever
print(replaced)
position = string2.find("hate")
print(position)