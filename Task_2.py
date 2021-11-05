numbers = []
for i in range(1, 1000, 2):
    numbers.append(i ** 3)

for i in range(len(numbers)):
    if i % 7 == 0:
        print(numbers)


