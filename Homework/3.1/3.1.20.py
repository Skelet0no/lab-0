def factorial(num):
    if num == 0:
        return 1
    return factorial(num - 1) * num


def answer(commands):
    i = 0
    while i < len(commands):
        count = 0
        for j in commands:
            if isinstance(j, int):
                count += 1
        if isinstance(commands[i], str):
            if commands[i] == "+":
                commands[i] = commands[i - 2] + commands[i - 1]
                del commands[i - 1]
                del commands[i - 2]
            elif commands[i] == "-":
                commands[i] = commands[i - 2] - commands[i - 1]
                del commands[i - 1]
                del commands[i - 2]
            elif commands[i] == "*":
                commands[i] = commands[i - 2] * commands[i - 1]
                del commands[i - 1]
                del commands[i - 2]
            elif commands[i] == "/":
                commands[i] = commands[i - 2] // commands[i - 1]
                del commands[i - 1]
                del commands[i - 2]
            elif commands[i] == "~":
                commands[i] = -commands[i - 1]
                del commands[i - 1]
            elif commands[i] == "!":
                commands[i] = factorial(commands[i - 1])
                del commands[i - 1]
            elif commands[i] == "#":
                commands[i] = commands[i - 1]
            elif commands[i] == "@":
                commands[i - 3], commands[i - 2], commands[i - 1] = commands[i - 2], commands[i - 1], commands[i - 3]
                del commands[i]
            i = 0
            continue
        i += 1
    print(*commands)


def main():
    commands = list(map(str, input().split(" ")))
    for i in range(len(commands)):
        try:
            commands[i] = int(commands[i])
        except ValueError:
            continue
    answer(commands)


if __name__ == "__main__":
    main()
