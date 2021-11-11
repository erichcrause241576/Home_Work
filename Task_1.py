duration = int(input('Введите число в секундах: '))

day = duration // (60 * 60 * 24)
hour = duration // (60 * 60) - day * 24
minute = duration // 60 - hour * 60 - day * 24 * 60
second = duration % 60

if day:
    print(f'{day} дн, {hour} час, {minute} мин, {second} сек')

elif hour:
    print(f'{hour} час, {minute} мин, {second} секунд')
elif minute:
    print(f'{minute} мин, {second} секунд')
elif second:
    print(f'{second} секунд')


