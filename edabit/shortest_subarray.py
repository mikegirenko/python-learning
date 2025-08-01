"""
Very Hard
Write a function that returns the length of the shortest contiguous sublist whose sum of all elements strictly
exceeds n.
"""


class ShortestSubarrayWhoseSumExceedsN:

    def min_length(self, input_list, n) -> int:
        original_list_len = len(input_list)
        list_of_sublists = []
        this_flag = True
        counter = 0
        sum_counter = 2
        #  find sublists, and it's length, then determine which are longer than n
        while this_flag:
            sublist = input_list[:sum_counter]
            sublist_sum = sum(sublist)
            if sublist_sum > n:
                list_of_sublists.append(sublist)
            if counter == original_list_len - 1:
                this_flag = False
            sum_counter += 1
            counter += 1
        #  find which sublist is the shortest
        list_of_lengths = []
        for sublist in list_of_sublists:
            sublist_len = len(sublist)
            list_of_lengths.append(sublist_len)
        if not list_of_lengths:
            length = -1
        else:
            length = min(list_of_lengths)

        return length


if __name__ == "__main__":
    shortest_subarray_object = ShortestSubarrayWhoseSumExceedsN()
    assert shortest_subarray_object.min_length([5, 8, 2, -1, 3, 4], 9) == 2
    assert shortest_subarray_object.min_length([3, -1, 4, -2, -7, 2], 4) == 3
    assert shortest_subarray_object.min_length([1, 0, 0, 0, 1], 1) == 5
    assert shortest_subarray_object.min_length([0, 1, 1, 0], 2) == -1
