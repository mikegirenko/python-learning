import math

"""
Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line
segment connecting those two points.
"""


class LengthOfLine:
    def length_of_line(self, coordinate_1, coordinate_2) -> float:
        # d =√(x2– x1)2+(y2 – y1)2
        point_1 = (coordinate_1[1] - coordinate_1[0]) ** 2
        point_2 = (coordinate_2[1] - coordinate_2[0]) ** 2
        point_3 = point_1 + point_2
        length = math.sqrt(point_3)
        length_float = round(length, 2)

        return length_float


if __name__ == "__main__":
    coordinate_1 = [15, 7]
    coordinate_2 = [22, 11]
    obj = LengthOfLine()
    print("Length of Line Segment", obj.length_of_line(coordinate_1, coordinate_2))


def test_length_of_line():
    coordinate_1 = [0, 0]
    coordinate_2 = [0, 0]
    assert obj.length_of_line(coordinate_1, coordinate_2) == 0
    coordinate_1 = [0, 0]
    coordinate_2 = [1, 1]
    assert obj.length_of_line(coordinate_1, coordinate_2) == 1.41
    coordinate_1 = [15, 7]
    coordinate_2 = [22, 11]
    assert obj.length_of_line(coordinate_1, coordinate_2) == 8.06


test_length_of_line()
