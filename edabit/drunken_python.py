"""
You need to create two functions to substitute str() and int(). A function called int_to_str() that converts
integers into strings and a function called str_to_int() that converts strings into integers.
"""

def int_to_str(int_in):
    str_out = "%s" % int_in

    return str_out


assert type(int_to_str(5)) == str


def str_to_int(str_in):
    int_out = eval(str_in)

    return int_out


assert type(str_to_int("77")) == int
