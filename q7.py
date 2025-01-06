a=int(input("Enter number: "))
b=int(input("Enter number: "))
c=int(input("Enter number: "))

if (a>b and a>c):
    print(f'{a} is greatest')
elif (b>a and b>c):
    print(f'{b} is greatest')
else:
    print(f'{c} is greatest')