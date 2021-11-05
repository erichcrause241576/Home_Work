numbers = list(range(1, 101))

for i in numbers:
    if i == 1 or (i > 20 and (i % 10) == 1) and (i % 100) != 11:
        print(i, 'процент')
    elif (i > 1 and i < 5) or (i > 20 and (i % 10) > 1 and (i % 10) < 5):
        print(i, 'процента')
    elif i == 0 or (i > 1 and i < 20) or (i % 10) == 0 or (i % 100) >= 11 or (i % 10) >= 5 or (i % 100) >= 10:
        print(i, 'процентов')
