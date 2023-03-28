'''
File with functions used for commonly used calcultaions
'''

def pythagorean(side_1: int, side_2: int) -> int:
    return ((side_1 ** 2) + (side_2 ** 2)) ** 0.5

def distance(point_1: tuple[int, int], point_2: tuple[int, int]) -> tuple[int, int]:
    x_diff = point_2[0] - point_1[0]
    y_diff = point_2[1] - point_1[1]

    return ((x_diff ** 2) + (y_diff ** 2)) ** 0.5
print()