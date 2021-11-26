products = [57.8, 46.51, 97, 160.10, 130.25, 80.15, 45.3, 182.14, 32, 55]
products.sort()
for product in products:
    rub = int(product)
    kk = (product - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')


products = [57.8, 46.51, 97, 160.10, 130.25, 80.15, 45.3, 182.14, 32, 55]
for product in sorted(products):
    rub = int(product)
    kk = (product - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')
