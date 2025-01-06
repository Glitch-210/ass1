li = [1,2,3,4,5]
print(sum(li))

#baki
def fun(li):
    for i in range(len(li)):
        if li[i] > li[i+1]:
            return li[i]
            
k = fun(li)
print(k)