from math import sqrt


def desc(a, b, c):
    descriminant = b * b - 4 * a * c
    if descriminant >= 0:
        return root(a, b, descriminant)
    if descriminant < 0:
        return "Корень не найден, так как дискриминант меньше нуля"


def root(a, b, descriminant):
    if descriminant > 0:
        x1 = (-b + sqrt(descriminant)) / (2 * a)
        x2 = (-b - sqrt(descriminant)) / (2 * a)
        return x1, x2
    else:
        x1 = -b / (2 * a)
        return x1
