import re

txt = input('Enter txt on INDIAN NATIONAL FLAG: ')
print(txt.replace('flag' or 'Flag','Song'))
if txt.startswith('India'):
    print('Yes it starts with india')
else:
    print('No it does not start with india')

pattern = r'[aeiouAEIOU]'
print(re.findall(pattern,txt))