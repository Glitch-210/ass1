dict={}
while True:
    print('''
1. add
2. delete
3. search
4. display
    ''')
    ask = int(input())
    match ask:
        case 1:
            eid = int(input('Enter employee id: '))
            name = input('Enter employee name: ')
            pos = input('Enter employee position: ')
            salary = int(input('Enter employee salary: '))
            dict[eid] = [name, pos, salary]
        case 2:
            eid = int(input('Enter employee id: '))
            dict.pop(eid)
        case 3:
            eid = int(input('Enter employee id: '))
            print(dict[eid])
        case 4:
            print(dict)
        case _: 
            break