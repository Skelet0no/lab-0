def answer(commands):
    i = 0
    while i < len(commands):
        if isinstance(commands[i], str):
            commands_next = commands[:i - 2]
            if commands[i] == "+":
                commands_next.append(commands[i - 2] + commands[i - 1])
            elif commands[i] == "-":
                commands_next.append(commands[i - 2] - commands[i - 1])
            elif commands[i] == "*":
                commands_next.append(commands[i - 2] * commands[i - 1])
            commands_next += commands[i + 1:]
            commands = commands_next.copy()
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
