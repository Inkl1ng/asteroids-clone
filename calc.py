'''
module of commmon calculations and formulas
'''

def opposite_angle(angle: int) -> int:
    return 360 - abs(angle - 180)

def pythagorean(side_1, side_2) -> float:
    return ((side_1 ** 2) + (side_2 ** 2)) ** 0.5

def distance_to(point_1: tuple, point_2: tuple) -> tuple:
    x_diff = point_2[0] - point_1[0]
    y_diff = point_2[1] - point_1[1]
    return ((x_diff ** 2) + (y_diff ** 2)) ** 0.5
