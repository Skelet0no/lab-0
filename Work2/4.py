def counter(text):
    letters = sorted(set(''.join(text.split())))
    for i in letters:
        if i.isalpha():
            yield tuple([i, text.count(i)])


text = "Мама мыла раму"
for letter, count in counter(text):
    print(f"{letter}: {count}")
