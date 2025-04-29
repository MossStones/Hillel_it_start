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