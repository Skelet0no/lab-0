def answer(hours, minutes, delivery_time):
    hours_result = str((hours + (delivery_time + minutes) // 60) % 24)
    minutes_result = str((minutes + delivery_time) % 60)
    if len(hours_result) == 1:
        hours_result = "0" + hours_result
    if len(minutes_result) == 1:
        minutes_result = "0" + minutes_result
    print(f"{hours_result}:{minutes_result}")


def main():
    hours = int(input())
    minutes = int(input())
    delivery_time = int(input())
    answer(hours, minutes, delivery_time)


if __name__ == "__main__":
    main()
