def answer(func):
    def wrapper(*args, **kwargs):
        return f"Результат функции: {func(*args, **kwargs)}"
    return wrapper


@answer
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
