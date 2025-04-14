
import string
import keyword
name = input("Введіть потенційне ім’я змінної: ")
if name[0].isdigit():
    print(" Ім’я не може починатися з цифри.")
elif any(char.isupper() for char in name):
    print("Ім’я не може містити великі літери.")
elif any(char in string.punctuation.replace("_", "") or char == " " for char in name):
    print(" Ім’я не може містити пробіли або знаки пунктуації.")
elif name.count("_") > 1:
    print( " не може містити більше одного підкреслення.")
elif name in keyword.kwlist:
    print(" Ім’я є зареєстрованим словом у Python.")
else:
    print(" Це валідне ім’я змінної!")
