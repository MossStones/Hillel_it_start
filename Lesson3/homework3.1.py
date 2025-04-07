number1 = float(input("Введіть число: "))
operation = input("Введіть знак (-, +, /, *): ")
number2 = float(input("Введіть число: "))
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 == 0:
        print(" не ділити на 0 ")
    else:
        result = number1 / number2
else:
    result = "Невірна операція!"
print()
