def answer(a_km, b_km, c_km_h):
    print('%.2f' % round((b_km - a_km) / c_km_h, 2))


def main():
    a_km = int(input())
    b_km = int(input())
    c_km_h = int(input())
    answer(a_km, b_km, c_km_h)


if __name__ == "__main__":
    main()
