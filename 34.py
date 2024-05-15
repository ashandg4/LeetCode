array1=[5,7,7,8,8,10]
target=8

# print("Original array: ",array1)

# for i in range(0,len(array1)):
#     for j in range(i+1,len(array1)):
#         if array1[i] >= array1[j]:
#             array1[i],array1[j]=array1[j],array1[i]
# print(array1)


# Method-1
l=[]
if target in array1:
    i=0
    for j in array1:
        if j==target:
            l.append(i)
        i+=1  
    if len(l)==1:
        l.append(l[0])
elif target not in array1:
    l.extend([-1,-1])
print([l[0],l[-1]])





# Method-2
length=len(array1)-1
if target in array1:
    array2=array1[::-1]
    print([array1.index(target),length-array2.index(target)])
else:
    print([-1,-1])
    