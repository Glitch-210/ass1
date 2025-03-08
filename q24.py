# 24.Create a menu driven program to show, a) list construction and display, b)
# Array construction and display c) dictionary construction and display d)
# tuple construction and display.

while True:
    print('''
    1. list construction and display
    2. array construction and display
    3. dict construction and display
    4. tuple construction and display
    ''')
    ask = int(input())
    match ask:
        case 1:
            li=[]
            size = int(input('Enter size of list: '))
            for i in range(size):
                data = input('Enter data: ')
                li.append(data)
            print(li)
        case 2:
            import numpy as np
            arr = np.array(input('Enter elements: ').split())
            print(arr)
        case 3:
            name = input('Enter name: ')
            sem = input('Enter sem: ')
            enroll = input('Enter enrollment number: ')
            dict={
                'name:':name,
                'sem:':sem,
                'enrollment:':enroll
            }
            for i,j in dict.items():
                print(f'{i} {j}')
        case 4:
            tu=(1,2,3,4,True)
            print(tu)
        case _:
            exit()