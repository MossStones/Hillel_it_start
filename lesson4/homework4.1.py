lst = [0, 1, 0, 12, 3]
a = 0
for i in range(len(lst)):
    if lst[i] != 0:
        lst[a] = lst[i]
        a += 1
for i in range(a, len(lst)):
    lst[i] = 0
print(lst)
