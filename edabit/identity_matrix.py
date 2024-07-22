"""
Very Hard
Create a function that takes an integer n and returns the identity matrix of n x n dimensions.
"""


class IdentityMatrix:
    def id_mtrx(self, n) -> list:
        if type(n) != int:
            identity_matrix = "Error"
        else:
            identity_matrix = []
            is_negative = False

            if n < 0:
                n = abs(n)
                is_negative = True
            for i in range(n):
                identity_matrix.append([])

            for item in identity_matrix:
                i = 0
                while i < n:
                    identity_matrix[i].append("0")
                    i = i + 1

            for item in identity_matrix:
                if n == 0:
                    identity_matrix = []
                if is_negative:
                    i = 0
                    while i < n:
                        if i == 0:
                            identity_matrix[i][i - 1] = "1"
                        if i == 1:
                            identity_matrix[i][i - 1] = "1"
                        if i == 2:
                            identity_matrix[i][i - 1] = "1"
                        i = i + 1
                else:
                    i = 0
                    while i < n:
                        identity_matrix[i][i] = "1"
                        i = i + 1

        return identity_matrix


if __name__ == "__main__":
    obj = IdentityMatrix()
    print("Non-integer passed:")
    print(obj.id_mtrx("spam"))
    print("0")
    print(obj.id_mtrx(0))
    print("-2")
    mtrx = obj.id_mtrx(-2)
    for m in mtrx:
        print(m)
    print("2")
    mtrx = obj.id_mtrx(2)
    for m in mtrx:
        print(m)
    print("3")
    mtrx = obj.id_mtrx(3)
    for m in mtrx:
        print(m)
