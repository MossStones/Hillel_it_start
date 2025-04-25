#
# def common_elements():
#     list1 = [x for x in range(100)]
#     list2 = [x for x in range(50, 150)]
#     if list1 % 3 == 0:
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

def common_elements():
    list1 = [a for a in range(100) if a % 3 == 0]
    list2 = [a for a in range(100) if a % 5 == 0]
    return set(list1) & set(list2)
print(common_elements())
