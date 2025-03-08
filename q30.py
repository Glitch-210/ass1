import re
txt = input('Enter string: ')
pattern = r'\d'
print(re.findall(pattern, txt))
pattern = r'\D'
print(re.findall(pattern, txt))
pattern = r''
print(re.findall(pattern, txt))
