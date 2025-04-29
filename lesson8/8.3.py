# Вам необхідно написати функцію find_unique_value, яка приймає список із чисел, знаходить серед них унікальне число та повертати його. Унікальне число - це число, яке зустрічається в списку один раз. Випадок, коли в одному списку буде кілька унікальних чисел, перевіряти не потрібно.
# def find_unique_value (*args):
def find_unique_value(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num
list1 = [1,1, 2, 3, 3]
print(find_unique_value(list1))