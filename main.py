# import json
from prettytable import PrettyTable


milky = {'молоко': [54.0, 2.9, 2.5, 4.8], 'йогурт': [57.0, 4.1, 1.5, 5.9], 'сметана': [206.0, 2.5, 20.0, 3.4],
         'творог': [169.0, 18.0, 9.0, 3.0], 'сыр': [364.0, 23.2, 29.5, 0.0]}
sweet = {'мед': (328.0, 0.8, 0, 80.3), 'шоколад': (580.0, 6.0, 35.0, 49.0), 'мороженое': (232.0, 3.7, 15.0, 20.4),
         'зефир': (300.0, 1.5, 0.1, 80), 'халва': (516.2, 11.6, 29.7, 54)}
vegetables = {'морковь': (41.0, 0.93, 0.24, 6.78), 'картофель': (77.0, 2.0, 0.4, 16.3), 'капуста': (28.0, 1.8, 0.2, 4.7),
              'томат': (24.0, 1.1, 0.2, 3.8), 'огурец': (14.0, 0.8, 0.1, 2.5)}
fruit = {'яблоко': (47.0, 0.4, 0.4, 9.8), 'груша': (47.0, 0.4, 0.3, 10.3), 'банан': (96.0, 1.5, 0.5, 21.0),
         'ананас': (552.0, 0.3, 0.1, 11.8), 'киви': (47.0, 0.8, 0.4, 8.1)}
meat = {'курица': (238.0, 18.2, 18.4, 0), 'говядина': (158.0, 22.2, 7.1, 0.0), 'свинина': (155.0, 21.55, 6.94, 0.0),
        'индейка': (100.0, 19.0, 7.0, 0.0), 'баранина': (288.0, 14, 25.8, 0.0)}


products = {}
a=[milky, sweet, vegetables, fruit, meat]

products.update(milky)
products.update(sweet)
products.update(vegetables)
products.update(fruit)
products.update(meat)
pr_new = {}
def print_all(products_new):
    th = ['Название', 'Калории', 'Белки', 'Жиры', 'Углеводы']
    table = PrettyTable(th)
    for i in products_new.keys():
        td = (i, products_new[i][0], products_new[i][1], products_new[i][2], products_new[i][3])
        table.add_row(td)
    print(table)

def filtr(parametr, numb):
    b = dict(filter(lambda x: x[1][parametr] <=numb, products.items()))
    return b


def calculate():
    product_and_cpfc = []
    calories_total: float = 0
    proteins_total: float = 0
    fats_total: float = 0
    carbohydrates_total: float = 0
    m = {}
    print("Приветствую!")
    filt = input("Вы хотите отфильтровать продукты?: да, нет: ")
    if filt.lower() == "да":
        filt_by = int(input("Выберите параметр для фильтрации: 0 - калории, 1 - белки, 2 - жиры, 3 - углеводы: "))
        filt_numb = float(input("Введите значение для фильтра: "))
        pr_new = filtr(filt_by,filt_numb)
        print_all(pr_new)
    else:
        print_all(products)
    while True:
        key_value_pair = input("Введите название и массу в граммах, "
                               "если Вы указали все продукты, введите 1: ")
        if key_value_pair == "1":
            break
        m[key_value_pair.partition(' ')[0]] = key_value_pair.partition(' ')[2]
    for i in m.keys():
        for j in products.keys():
            if i.lower() == j.lower():
                product_and_cpfc.append((j, float(m[i]) * float(products[j][0]) / 100,
                                          float(m[i]) * float(products[j][1]) / 100,
                                          float(m[i]) * float(products[j][2]) / 100,
                                          float(m[i]) * float(products[j][3]) / 100,))
                calories_total += float(m[i]) * float(products[j][0]) / 100
                proteins_total += float(m[i]) * float(products[j][1]) / 100
                fats_total += float(m[i]) * float(products[j][2]) / 100
                carbohydrates_total += float(m[i]) * float(products[j][3]) / 100
    sort_by = input("Выберите параметр для сортировки: калории, белки, жиры, углеводы: ")
    print()
    if sort_by.lower() == "калории":
        product_and_cpfc.sort(key=lambda x: (x[1], x[0]))
    elif sort_by.lower() == "белки":
        product_and_cpfc.sort(key=lambda x: (x[2], x[0]))
    elif sort_by.lower() == "жиры":
        product_and_cpfc.sort(key=lambda x: (x[3], x[0]))
    elif sort_by.lower() == "углеводы":
        product_and_cpfc.sort(key=lambda x: (x[4], x[0]))
    for i in product_and_cpfc:
        for j in m.keys():
            if str(i[0]).lower() == str(j).lower():
                string = """{} {}г - калории: {}, белки: {}, жиры: {}, углеводы: {}""".format(
                    str(i[0]).capitalize(), m[j], i[1], i[2], i[3], i[4])
                print(string)
                # write_json(string)
                break
    string = "Всего - калории: {}, белки:{}, жиры:{}, углеводы:{}".format(
        round(calories_total,1), round(proteins_total,1), round(fats_total,1), round(carbohydrates_total,1))
    print(string)
    # write_json(string)

# def write_json(meal):
#     try:
#         data = json.load(open('meals.json'))
#     except:
#         data = []
#     data.append(meal)
#     with open('meals.json', 'w') as file:
#         json.dump(data, file, indent=2, ensure_ascii=False)

calculate()