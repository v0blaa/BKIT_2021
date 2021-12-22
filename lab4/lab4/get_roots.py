
import math

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
