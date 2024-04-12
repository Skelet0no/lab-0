res = ()


def enter_results(*args):
    global res
    res += args


def get_sum():
    return (round(sum([res[i] for i in range(0, len(res), 2)]), 2),
            round(sum([res[i] for i in range(1, len(res), 2)]), 2))


def get_average():
    return (round(sum([res[i] for i in range(0, len(res), 2)]) / (len(res) // 2), 2),
            round(sum([res[i] for i in range(1, len(res), 2)]) / (len(res) // 2), 2))
