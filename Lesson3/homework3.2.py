lst = [1,2,3, "4", [1,2,"3"]]
if len(lst) >= 2:
    a = lst.pop()
    lst.insert(0, a)
    print(lst)
elif len(lst) == 1:
        print([lst[0]])
elif lst == ([]):
    print (lst)
else:
    print("False")

