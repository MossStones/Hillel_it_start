while True:
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
            result = "Помилка! Не можна ділити на 0"
        else:
            result = number1 / number2
    else:
        result = "ТАК НІЗЯ!"

    print("Результат:", result)

    cont = input("Do you want to try again? (yes or no): ")
    if cont != "yes" and cont!= "y":
        print("Goodbye!")
        break
