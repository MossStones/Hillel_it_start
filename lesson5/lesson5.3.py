import string

a = input("Введіть рядок: ")


for b in string.punctuation:
    a = a.replace(b, "")
word = a.split()

title_words = [word[0].upper() + word[1:].lower() for word in word]

hashtag = "#" + "".join(title_words)
hashtag = hashtag[:140]
print("Ваш хештег:", hashtag)
