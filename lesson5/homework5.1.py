
# import string
# import keyword
# name = input("Введіть потенційне ім’я змінної: ")
# if name[0].isdigit():
#     print(" false")
# elif any(char.isupper() for char in name):
#     print("false.")
# elif any(char in string.punctuation.replace("_", "") or char == " " for char in name):
#     print(" false.")
# elif name.count("_") > 1:
#     print( "false")
# elif name in keyword.kwlist:
#     print("false")
# else:
#     print("true")

import string
import keyword

name = input("Введіть ім'я змінної: ")

valid = True

if not name:
    valid = False

if name[0].isdigit():
    valid = False

for char in name:
    if char.isupper():
        valid = False

for char in name:
    if char in string.punctuation and char != "_":
        valid = False

for char in name:
    if char.isspace():
        valid = False

if name in keyword.kwlist:
    valid = False

if not valid:
    if name.count("_") > 1:
        valid = False
    else:
        valid = True

print(valid)
