a=(18,24,37,84,77,42,61,9,4)
b=0
for i in range(a.__len__()):
    b=b+a[i]
b=int(b/a.__len__())
print(b)