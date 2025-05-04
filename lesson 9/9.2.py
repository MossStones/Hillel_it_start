def difference(*numbers):
    if not numbers:
        return 0
    if None in numbers:
        return 0
    numbers = [round(num, 2) for num in numbers]# НЕ ПЕРЕВОДИТЬ

    return max(numbers) - min(numbers)

print(difference(10.2, -2.2, 0, 1.1, 0.5))
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference() == 0, 'Test4'
print('OK')
