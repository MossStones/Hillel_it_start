text = str(input("Введіть якесь речення:"))

def correct_sentence(text: str) -> str:

    if not text.endswith("."):
        text += "."
    text = text[0].upper() + text[1:]
    return text

print(correct_sentence(text))
