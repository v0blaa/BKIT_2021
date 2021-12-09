import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coefStr = sys.argv[index]

        if coefStr == '0' and index == 1:
            raise

        coef = float(coefStr)
        return coef
    except:
        # Вводим с клавиатуры
        while True:
            print(prompt)
            coefStr = input()
            for i in range(len(coefStr)):
                if not(coefStr[i].isdigit() or coefStr[i] == '-'):
                    break
            else:
                break
    # Переводим строку в действительное число
        coef = float(coefStr)
        return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:ƒ
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root1 = -b / (2.0 * a)
        if root1 > 0:
            root1 = math.sqrt(root1)
            root2 = -root1
            result.append(root1)
            result.append(root2)
        if root1 == -0.0:
            root1 = 0.0
            result.append(root1)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        if root1 > 0:
            root1 = math.sqrt(root1)
            root2 = -root1
            result.append(root1)
            result.append(root2)
        if root1 == -0.0:
            root1 = 0.0
            result.append(root1)
        root3 = (-b - sqD) / (2.0 * a)
        if root3 > 0 and math.sqrt(root3) != -root1:
            root3 = math.sqrt(root3)
            root4 = -root3
            result.append(root3)
            result.append(root4)
        if root3 == -0.0:
            root3 = 0.0
            result.append(root3)
    return result


def main():
    print()
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:', )

    while a == 0:
        print('Коэфициент А не может быть равен 0')
        a = get_coef(1, 'Введите коэффициент А:')


    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4