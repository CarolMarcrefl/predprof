import csv

with open('products.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=';'))[1:]

    total = {}
    ans1 = 0

# подсчёт итоговой суммы по каталогу Закуски
    for elem in reader:
        total[elem[2]] = total.get(float(elem[-1]) * float(elem[-2]))

    for Category, product, Date, Price_per_unit, Count in reader:
        if 'Закуски' in Category:
            ans1 += float(Count) * float(Price_per_unit)
    print(ans1)

    with open('products_new.csv', 'w', encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimeter=';')
        writer = csv.writer((['Category', 'product', 'Date', 'Price_per_unit', 'Count', 'total']))
        writer.writerows(reader)
