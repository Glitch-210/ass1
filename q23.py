#23.Create a menu driven program for all the comparision operations.
while True:
    print('''
    1. a<b
    2. a>b
    3. a==b
    4. a!=b
    5. a>=b
    6. a<=b
    ''')
    ask = int(input())
    match ask:
        case 1:
            a = int(input('Enter number 1: '))
            b = int(input('Enter number 2: '))
            if a<b:
                print(True)
            else:
                print(False)
        case 2:
            a = int(input('Enter number 1: '))
            b = int(input('Enter number 2: '))
            if a>b:
                print(True)
            else:
                print(False)
        case 3:
            a = int(input('Enter number 1: '))
            b = int(input('Enter number 2: '))
            if a==b:
                print(True)
            else:
                print(False)
        case 4:
            a = int(input('Enter number 1: '))
            b = int(input('Enter number 2: '))
            if a!=b:
                print(True)
            else:
                print(False)
        case 5:
            a = int(input('Enter number 1: '))
            b = int(input('Enter number 2: '))
            if a>=b:
                print(True)
            else:
                print(False)
        case 6:
            a = int(input('Enter number 1: '))
            b = int(input('Enter number 2: '))
            if a<=b:
                print(True)
            else:
                print(False)
        case _:
            exit()
        