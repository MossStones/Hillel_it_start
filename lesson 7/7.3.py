def second_index(text: str, some_str:str) -> str:
    first = text.find(some_str)
    if first == -1:
        return None
    second = text.find(some_str, first + 1)
    return second if second != -1 else None

text =input("Введіть текст з макс 3 слів:")
some_str=input("Введіть значення яке шукаєте:")

result = second_index(text, some_str)
print("Другий індекс:", result)