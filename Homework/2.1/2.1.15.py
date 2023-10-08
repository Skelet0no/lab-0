def answer(hours, minutes, delivery_time):
    hours_result = str((hours + (delivery_time + minutes) // 60) % 24)
    minutes_result = str((minutes + delivery_time) % 60)
    print(f"{hours_result:0>2}:{minutes_result:0>2}")


def main():
    hours = int(input())
    minutes = int(input())
    delivery_time = int(input())
    answer(hours, minutes, delivery_time)


if __name__ == "__main__":
    main()
