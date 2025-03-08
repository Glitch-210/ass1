while True:
    print('''
    1. fname and lname
    2. name in upper and lower case
    3. length of name
    4. greeting msg
    ''')
    ask = int(input())
    match ask:
        case 1:
            txt = input('Enter your name in the format fname lname: ')
            fname, lname = txt.split()
            print(f'First name: {fname}\nLast name: {lname}')
        case 2:
            name = input('Enter your name: ')
            print(f'Upper case: {name.upper()}\nLower case: {name.lower()}')
        case 3:
            name = input('Enter your name: ')
            print(f'Length of name: {len(name)}')
        case 4:
            name = input('Enter your name: ')
            print(f'Hello {name}')
        case _:
            exit()