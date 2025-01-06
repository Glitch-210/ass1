def prime(a):
    if a>1:
        for i in range(1,a):
            if a%i==0:
                print(f'{a} is not a prime')
                break
            else:
                print(f'{a} is a prime number')
                break

a = int(input("Enter number: "))
prime(a)
#baki