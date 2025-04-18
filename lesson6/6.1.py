import string

user_input = input("Введіть 2 літери через дефіс (наприклад, a-C): ")

start, end = user_input.split("-")

letters = string.ascii_letters

start_index = letters.index(start)
end_index = letters.index(end)

if start_index <= end_index:
    result = letters[start_index:end_index + 1]
else:
    result = letters[start_index:end_index - 1:-1]

print(result)
