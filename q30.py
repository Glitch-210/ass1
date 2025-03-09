import re
txt = input('Enter string: ')
pattern = r'\d'
print(re.findall(pattern, txt))
pattern = r'\D'
print(re.findall(pattern, txt))
# c. Words, digits and special characters.
pattern = r'\w'
print(re.findall(pattern, txt))
