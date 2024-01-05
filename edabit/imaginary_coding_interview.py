"""
Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.
"""


def interview(list_of_times, total_time):
    candidate_is_qualified = "qualified"
    # The candidate should have complete all the questions.
    if len(list_of_times) < 8:
        candidate_is_qualified = "disqualified"
    # The maximum time given to complete the interview is 120 minutes.
    elif total_time > 120:
        candidate_is_qualified = "disqualified"
    # The maximum time given for very easy questions is 5 minutes each
    elif list_of_times[0] > 5 or list_of_times[1] > 5:
        candidate_is_qualified = "disqualified"
    # The maximum time given for easy questions is 10 minutes each
    elif list_of_times[2] > 10 or list_of_times[3] > 10:
        candidate_is_qualified = "disqualified"
    # The maximum time given for medium questions is 15 minutes each
    elif list_of_times[4] > 15 or list_of_times[5] > 15:
        candidate_is_qualified = "disqualified"
    # The maximum time given for hard questions is 20 minutes each.
    elif list_of_times[6] > 20 or list_of_times[7] > 20:
        candidate_is_qualified = "disqualified"

    return candidate_is_qualified


print(interview([5, 5, 10, 10, 15, 15, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))
print(interview([5, 9, 10, 10, 15, 15, 20, 20], 120))
print(interview([5, 5, 11, 10, 15, 15, 20, 20], 120))
print(interview([5, 5, 10, 10, 16, 15, 20, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20, 21], 120))
print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
