age = int(input("What's your age?: "))
name = str(input("What's your name?: "))

def say_hi(name: str, age: int) -> str:
    return f"Hi, my name is {name} and I'm {age} years old"

print(say_hi(name, age))

assert say_hi(name, age) == f"Hi, my name is {name} and I'm {age} years old"

print(f"ok ,{name}")

# Або такий варіант->>>>>>>>>>>>>>>

def say_hi(name: str, age: int) -> str:
    return f"Hi. My name is {name} and I'm {age} years old"
assert say_hi("Alex", 32)
assert say_hi("Frank", 68)
print('ОК')