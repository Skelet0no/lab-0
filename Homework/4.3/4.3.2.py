def recursive_digit_sum(spi):
    if spi // 10 == 0:
        return spi
    return spi % 10 + recursive_digit_sum(spi // 10)
