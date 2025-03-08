dict = {
    'name': 'Rohan',
    'sem': '3',
    'enrollment': '123456',
    'password': 'password',
    'email': 'rohan@gmail.com'
}
while True:
    print('''
    1. key
    2. values
    3. items
    4. count
    ''')
    ask = int(input())
    match ask:
        case 1:
            for keys in dict.keys():
                print(keys)
        case 2: 
            for values in dict.values():
                print(values)
        case 3:
            for keys, values in dict.items():
                print(keys, values)
        case 4:     
            sentence = input('Enter sentence: ')
            letter_cnt = {}
            for char in sentence.replace(" ",""):
                if char in letter_cnt:
                    letter_cnt[char] += 1 
                else:
                    letter_cnt[char]= 1
            print(letter_cnt)
        case _: 
            exit()