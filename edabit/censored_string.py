"""
Given a censored string and a string of the censored vowels, return the original uncensored string.
"""


def uncensor(censored_string, censored_vowels) -> str:
    censored_string_list = list(censored_string)
    counter = 0
    for character in censored_string_list:
        if character == "*":
            index = censored_string_list.index(character)
            censored_string_list[index] = censored_vowels[counter]
            counter += 1

    unsensored_string = "".join(censored_string_list)

    return unsensored_string


assert uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") == "Where did my vowels go?"
assert uncensor("abcd", "") == "abcd"
assert uncensor("*PP*RC*S*", "UEAE") == "UPPERCASE"
