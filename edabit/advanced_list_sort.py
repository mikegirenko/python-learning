"""
Very Hard
Create a function that takes a list of numbers or strings and returns a list with the items from the original list
stored into sublists. Items of the same value should be in the same sublist.
"""


class AdvancedListSort:
    def __init__(self, list_in):
        self.list_in = list_in

    def advanced_sort(self) -> list:
        list_out = []
        list_in_to_set = set(self.list_in)
        unique_items = list(list_in_to_set)

        repeated_items_as_groups = []
        for unique in unique_items:
            for item in self.list_in:
                if unique == item:
                    repeated_items_as_groups.append(unique)

        temp_list = []
        for unique in unique_items:
            counter = repeated_items_as_groups.count(unique)
            i = 0
            while i < counter:
                temp_list.append(unique)
                i += 1
            list_out.append(temp_list)
            temp_list = []
        if len(temp_list) != 0:
            list_out.append(temp_list)

        return list_out


if __name__ == "__main__":
    obj = AdvancedListSort(["b", "a", "b", "a", "c"])  # [["b", "b"], ["a", "a"], ["c"]]
    print(obj.advanced_sort())

    obj = AdvancedListSort([2, 1, 2, 1])  # [[2, 2], [1, 1]]
    print(obj.advanced_sort())

    obj = AdvancedListSort([5, 4, 5, 5, 4, 3])  # [[5, 5, 5], [4, 4], [3]]
    print(obj.advanced_sort())
