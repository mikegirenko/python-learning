"""
Create a function that returns an integer representing the number of matching pairs of socks that are available.
"""


def sock_merchant(list_of_socks) -> int:
    matching_pairs = 0
    counts = {}

    for item in list_of_socks:
        counts[item] = list_of_socks.count(item)

    pairs = []

    for k, v in counts.items():
        if v >= 2:
            pairs.append(k)

    for pair in pairs:
        for k, v in counts.items():
            if pair == k:
                div = v // 2  # floor division
                matching_pairs = matching_pairs + div

    return matching_pairs


assert sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3
assert sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) == 4
assert sock_merchant([]) == 0
