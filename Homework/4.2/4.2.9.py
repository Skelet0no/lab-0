
print(*filter(lambda x: sum([int(i) for i in str(x)]) % 2 == 0, (32, 64, 128, 256, 512)))