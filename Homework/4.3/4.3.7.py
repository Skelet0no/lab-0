def same_type(func):
    def wrapper(*args, **kwargs):
        test = type(args[0])
        for i in args:
            if type(i) is not test:
                print("Обнаружены различные типы данных")
                return False
        return func(*args, *kwargs)
    return wrapper


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')
