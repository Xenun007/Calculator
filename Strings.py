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
position = string2.find("hate")  #prints the index of the searched element
print(position)
# isnumeric()  function checks if the entire string consists of just numbers
ages = [2,4,5,2,5,7,3,7,3,6,3,73,6,63,35,6,7,7,3,2,5]
tage = set()  # it could also be initialised as tage = {}
for age in ages:
    tage.add(age)
print(tage)
print(min(ages))