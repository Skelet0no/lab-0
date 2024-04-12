def make_equation(*spi):
    spi = list(spi)
    if len(spi) == 1:
        return spi[0]
    return f'({make_equation(*spi[:len(spi) - 1:])}) * x + {spi[-1]}'
