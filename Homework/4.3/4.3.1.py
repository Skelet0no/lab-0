def recursive_sum(*spi):
    spi = list(spi)
    if len(spi) == 1:
        return spi[0]
    return spi[len(spi) - 1] + recursive_sum(*spi[:len(spi) - 1:])
