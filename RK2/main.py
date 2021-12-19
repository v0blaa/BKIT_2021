"""
1. «Улица» и «Дом» связаны соотношением один-ко-многим. Выведите список всех домов, у которых названия заканчивается на «ка», и названия их улиц.
2. «Улица» и «Дом» связаны соотношением один-ко-многим. Выведите список улиц со средней стоимостью дома на каждой улице, отсортированный по средней стоимости (отдельной функции вычисления среднего значения в Python нет, нужно использовать комбинацию функций вычисления суммы и количества значений).
3. «Улица» и «Дом» связаны соотношением многие-ко-многим. Выведите список всех улиц, у которых название начинается с буквы «А», и список находящихся на них домов.

Дом   Улица

"""

# используется для сортировки
from operator import itemgetter


class House:
    """Дом"""

    def __init__(self, id, name, cost, streetID):
        self.id = id
        self.name = name
        self.cost = cost
        self.streetID = streetID


class Str:
    """Улица"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class StrHouse:
    """
    'Дома улицы' для реализации
    связи многие-ко-многим
    """

    def __init__(self, streetID, houseID):
        self.streetID = streetID
        self.houseID = houseID


# Улицы
streets = [
    Str(1, 'Пушкинская улица'),
    Str(2, 'Авангардная улица'),
    Str(3, 'Алтайская улица'),

    # для связи многие-ко-многим:
    Str(11, 'Авиационная улица'),
    Str(22, 'Новорязанская улица'),
    Str(33, 'Парковая улица'),
]

# Сотрудники
houses = [
    House(1, 'Малосемейка', 7000000, 1),
    House(2, 'Сталинка', 20000000, 2),
    House(3, 'Хрущевка', 12000000, 2),
    House(4, 'Брежневка', 18000000, 3),
    House(5, 'Студия', 10000000, 3),
]

strsHouses = [
    StrHouse(1, 1),
    StrHouse(2, 2),
    StrHouse(2, 3),
    StrHouse(3, 4),
    StrHouse(3, 5),

    StrHouse(11, 1),
    StrHouse(22, 2),
    StrHouse(22, 3),
    StrHouse(33, 4),
    StrHouse(33, 5),

]

def task1(one_to_many):
    print('Задание D1')
    res1 = list(filter(lambda x: x[0].endswith("ка"), one_to_many))
    return res1

def task2(one_to_many):
    print('\nЗадание D2')
    res2unsorted = []
    # Перебираем все улицы
    for s in streets:
        # Список домов на улице
        houses1 = list(filter(lambda i: i[2] == s.name, one_to_many))
        # Если на улице есть дома
        if len(houses1) > 0:
            # Dсе цены домов на улице
            allCosts = [sal for _, sal, _ in houses1]
            # Cредняя цена дома на улице
            averageCosts = round(sum(allCosts) / len(allCosts), 1)
            res2unsorted.append((s.name, averageCosts))

    # Cортировка по средней стоимости
    res2 = sorted(res2unsorted, key=itemgetter(1), reverse=True)
    return res2

def task3(many_to_many):
    print('\nЗадание D3')
    res3 = {}
    # Цикл по всем улицам
    for s in streets:
        if s.name.startswith("А"):
            # Список домов на улице
            houses1 = list(filter(lambda i: i[2] == s.name, many_to_many))
            # Только имя дома
            housesNames = [x for x, _, _ in houses1]
            # Добавляем результат в словарь
            # ключ - улица, значение - список названий домов
            res3[s.name] = housesNames

    return res3


def relations_creation():

    # Соединение данных один-ко-многим с помощью кортежа
    one_to_many = [(h.name, h.cost, s.name)
                   for s in streets
                   for h in houses
                   if h.streetID == s.id]

    # Соединение данных многие-ко-многим с помощью кортежа
    many_to_many_temp = [(s.name, sh.streetID, sh.houseID)
                         for s in streets
                         for sh in strsHouses
                         if s.id == sh.streetID]

    many_to_many = [(h.name, h.cost, streetName)
                    for streetName, streetID, houseID in many_to_many_temp
                    for h in houses if h.id == houseID]

    return (one_to_many, many_to_many)


if __name__ == '__main__':
    relations = relations_creation()
    print(task1(relations[0]))
    print(task2(relations[0]))
    print(task3(relations[1]))
