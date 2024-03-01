from collections import Counter

"""
Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times
in a list (where N is the length of the list).
"""


def majority_vote(votes_list):
    calculated_majority_vote = ""
    if len(votes_list) == 0:
        calculated_majority_vote = "None"
    else:
        counted_elements = dict(Counter(votes_list))
        for k, v in counted_elements.items():
            if v > len(votes_list) / 2:
                calculated_majority_vote = k
                break
            else:
                calculated_majority_vote = "None"

    return calculated_majority_vote


print(majority_vote([]))  # -> None
print(majority_vote(["A", "A", "B"]))  # ➞ "A"
print(majority_vote(["A", "A", "B", "B", "B"]))  # ➞ "B"
print(majority_vote(["A", "B", "B", "A", "C", "C"]))  # -> None
