while True:
    match ask:=int(input('''
    '1. Add new file'
    '2. Read file'
    '3. Check file exists'
    '4. Write in file'
    '5. Copy file'
    '6. Delete'
    ''')):
        case 1:
            with open('indianflag.txt','a+') as f1:
                para = input('Enter you want to write in the file: ')
                f1.write(para)
        case 2:
            with open('indianflag.txt','r') as f1:
                print(f1.readlines())
        case 3:
            import os
            f1 = input('Enter file name: ')
            if os.path.exists(f1):
                print('File exists')
            else:
                print('File does not exist')
        case 4:
            with open('indianflag.txt','a+') as f1:
                para = input('Enter you want to write in the file: ')
                f1.write(para)
        case 5:
            import shutil
            shutil.copy('indianflag.txt','indianflagsong.txt')
            print('copied')
        case 6:
            import os
            f1 = input('Enter file name: ')
            if os.path.exists(f1):
                os.remove(f1)
                print('deleted')
            else:
                print('File does not exist')
        case _:
            break