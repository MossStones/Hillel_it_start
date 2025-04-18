
while True:
    person = input("Введіть число: ")
    if not person.isdigit():
        print("Будь ласка, введіть лише цифри.")
        continue

    number = int(person)

    while number > 9:
        product = 1
        for digit in str(number):
            product *= int(digit)
        number = product

    print("Результат:", number)
    break