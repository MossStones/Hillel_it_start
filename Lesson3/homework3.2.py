lst = []
if len(lst) >= 2:
    a = lst.pop()
    lst.insert(0, a)
elif len(lst) == 1 or lst == []:
    print()
else:
    print("False")
print(lst)