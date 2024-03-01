"""
Write a function that takes the coordinates of three points in the form of a 2d array and returns the perimeter of
the triangle. The given points are the vertices of a triangle on a two-dimensional plane.
"""


def perimeter(coordinates):
    calculated_perimeter = 0
    for coordinate in coordinates:
        # TODO: the below formula is not correct, need to find correct one
        calculated_perimeter = calculated_perimeter + (coordinate[0] + coordinate[1])

    return round(calculated_perimeter, 2)


assert perimeter([[15, 7], [5, 22], [11, 1]]) == 47.08
