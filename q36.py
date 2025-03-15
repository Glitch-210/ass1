#36.Using Data Structures, model a library book details that stores bookname,
# ISBN number, Author Information and the number of copies in the library.

lib={}
while True:
    print(''''
    '1. Add'
    '2. Delete'
    '3. Search''
    '4. Display'
    ''')
    ask = int(input())
    match ask:
        case 1:
            book = input('Enter book name: ')
            isbn = input('Enter ISBN number: ') 
            author = input('Enter author information: ')
            copies = int(input('Enter number of copies: '))
            lib[book] = [isbn, author, copies]
        case 2:
            book = input('Enter book name: ')
            lib.pop(book)
        case 3:
            book = input('Enter book name: ')
            print(lib[book])
        case 4:
            print(lib)
        case _:
            break
        
