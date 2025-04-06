number1 = float(input("Введіть число: "))
operation = input("Введіть знак (-, +, /, *): ")
number2 = float(input("Введіть число: "))
if (operation == "/"
        and number2 == 0):
    print("Не можна на 0")
else:
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        result = number1 / number2
    else:
        result = "Невірно операція!"
    print(result)
