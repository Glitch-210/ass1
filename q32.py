import pprint

txt = input('Enter input: ')
letter_cnt = {}

for char in txt.replace(" ",""):
    if char in letter_cnt:
        letter_cnt[char] += 1 
    else:
        letter_cnt[char]= 1

pprint.pprint(letter_cnt)