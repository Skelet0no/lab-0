def order(*args):
    global in_stock
    for coffe in args:
        if coffe == "Эспрессо":
            if in_stock["coffee"] >= 1:
                in_stock["coffee"] -= 1
                return coffe
        elif coffe == "Капучино":
            if in_stock["coffee"] >= 1 and in_stock["milk"] >= 3:
                in_stock["coffee"] -= 1
                in_stock["milk"] -= 3
                return coffe
        elif coffe == "Макиато":
            if in_stock["coffee"] >= 2 and in_stock["milk"] >= 1:
                in_stock["coffee"] -= 2
                in_stock["milk"] -= 1
                return coffe
        elif coffe == "Кофе по-венски":
            if in_stock["coffee"] >= 1 and in_stock["cream"] >= 2:
                in_stock["coffee"] -= 1
                in_stock["cream"] -= 2
                return coffe
        elif coffe == "Латте Макиато":
            if in_stock["coffee"] >= 1 and in_stock["milk"] >= 2 and in_stock["cream"] >= 1:
                in_stock["coffee"] -= 1
                in_stock["milk"] -= 2
                in_stock["cream"] -= 1
                return coffe
        elif coffe == "Кон Панна":
            if in_stock["coffee"] >= 1 and in_stock["cream"] >= 1:
                in_stock["coffee"] -= 1
                in_stock["cream"] -= 1
                return coffe
    return "К сожалению, не можем предложить Вам напиток"
