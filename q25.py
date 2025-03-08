# 25.Create a menu driven program to show Basic Dictionary Operations like
# Create, access, update, and delete dictionary entries.

while True:
    print('''
    1. create
    2. access
    3. update
    4. delete
    ''')
    ask = int(input())
    match ask:
        case 1:
            name = input('Enter name: ')
            sem = input('Enter sem: ')
            enroll = input('Enter enrollment number: ')
            dict={
                'name':name,
                'sem':sem,
                'enrollment':enroll
            }
            print('Dictionary created')
        case 2:
            access = input('Enter key: ')
            print(dict[access])
        case 3:
            #update
            key = input('Enter key: ')
            value = input('Enter new value: ')
            dict[key] = value
            print('Dictionary updated')
        case 4:
            key = input('Enter key to delete: ')
            del dict[key]
            print('Dictionary deleted')
        case _:
            exit()