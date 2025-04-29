def is_palindrome(text):
    text = ''.join(c.lower() for c in text if c.isalnum())
    return text == text[::-1]
text = input("Введіть щось:")
print(is_palindrome(text))