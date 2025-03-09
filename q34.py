dict={}
while True:
    print('''
1. add
2. delete
3. search
4. display
    ''')
    ask = int(input())
    if ask == 1:
        name = input('Enter name: ')
        num = int(input('Enter number: '))
        dict[name] = num
    elif ask == 2:
        name = input('Enter name: ')
        del dict[name]
    elif ask == 3:
        name = input('Enter name: ')
        print(dict[name])
    elif ask == 4:
        print(dict)
    else:
        break