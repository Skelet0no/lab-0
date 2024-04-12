def result_accumulator(func):
    spi = []

    def wrapper(*args, method="accumulate", **kwargs):
        nonlocal spi
        spi.append(func(*args, **kwargs))
        if method == "drop":
            k = spi.copy()
            spi = []
            return k
    return wrapper


