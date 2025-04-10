
lst =[0, 1, 7, 2, 4, 8, ]
if len(lst)== 0:
    print(0)
a=0
for i in range(len(lst)):
    if i % 2 == 0:
        a += lst[i]
print(a * lst[-1])
