"""
In Very Hard.
Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if
it is strictly greater than the number before it
"""


class ConcertSeats:
    def can_see_stage(self, seats_list) -> bool:
        can_see = False
        seats_rows = len(seats_list)
        seats_in_each = len(seats_list[0])
        if (
            seats_list[seats_rows - 1][seats_in_each - 1]
            > seats_list[seats_rows - 2][seats_in_each - 1]
            > seats_list[seats_rows - 3][seats_in_each - 1]
            and seats_list[seats_rows - 1][seats_in_each - 1]
            > seats_list[seats_rows - 3][seats_in_each - 1]
        ):

            if (
                seats_list[seats_rows - 1][seats_in_each - 2]
                > seats_list[seats_rows - 2][seats_in_each - 2]
                > seats_list[seats_rows - 3][seats_in_each - 2]
                and seats_list[seats_rows - 1][seats_in_each - 2]
                > seats_list[seats_rows - 3][seats_in_each - 2]
            ):

                if (
                    seats_list[seats_rows - 1][seats_in_each - 3]
                    > seats_list[seats_rows - 2][seats_in_each - 3]
                    > seats_list[seats_rows - 3][seats_in_each - 3]
                    and seats_list[seats_rows - 1][seats_in_each - 3]
                    > seats_list[seats_rows - 3][seats_in_each - 3]
                ):
                    can_see = True

        return can_see


if __name__ == "__main__":
    obj = ConcertSeats()
    print(obj.can_see_stage([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(obj.can_see_stage([[0, 0, 0], [1, 1, 1], [2, 2, 2]]))
    print(obj.can_see_stage([[2, 0, 0], [1, 1, 1], [2, 2, 2]]))
    print(obj.can_see_stage([[1, 0, 0], [1, 1, 1], [2, 2, 2]]))
