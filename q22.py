#22.Create a menu driven program for all the arithmetic operations.
while True:
    print('''
    1.add
    2.sub
    3.mul
    4.divide
    5.power
    ''')
    ask = int(input())
    match ask:
        case 1:
            a = int(input('Enter number 1: '))
            b = int(input('Enter number 2: '))
            print(a+b)
        case 2:
            a = int(input('Enter number 1: '))
            b = int(input('Enter number 2: '))
            print(a-b)
        case 3:
            a = int(input('Enter number 1: '))
            b = int(input('Enter number 2: '))
            print(a*b)
        case 4:
            a = int(input('Enter number 1: '))
            b = int(input('Enter number 2: '))
            print(a/b)
        case 5:
            a = int(input('Enter number 1: '))
            print(a**2)
        case _:
            exit()
        