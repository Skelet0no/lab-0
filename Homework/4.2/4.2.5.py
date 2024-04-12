def to_string(*args, **kwargs):
    return kwargs.get("set", " ").join([str(i) for i in args]) + kwargs.get("end", "\n")

result = to_string(1, 2, 3)
print(result)
