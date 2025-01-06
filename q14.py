import array
arr1 = array.array('i')
arr2 = array.array('i')
size = int(input("Enter size of array: "))
print('array 1')
for i in range(size):
    data = int(input('Enter element: '))
    arr1.insert(i,data)

print('array 2')
for i in range(size):
    data = int(input('Enter element: '))
    arr2.insert(i,data)

for i in range(size):
    print(arr1[i],end=" ")
print()
for i in range(size):
    print(arr2[i],end=" ")

arr3 = array.array('i')
for i in range(size):
    data2 = arr1[i] + arr2[i]
    arr3.insert(i,data2)

print('\nafter addition')
for i in range(size):
    print(arr3[i],end=" ")