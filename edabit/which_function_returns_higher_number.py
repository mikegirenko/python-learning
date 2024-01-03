"""
Your function will be passed two functions, f and g, that don't take any parameters. Your function has to call them,
and return a string which indicates which function returned the larger number.
"""


def f(this_number) -> int:
    return this_number


def g(this_number) -> int:
    return this_number


def which_is_larger(f, g):
    # The problem: func1 is a function (and so is func2). In order to call it, you have to say func1().
    if f() > g():
        return "f"
    if g() > f():
        return "g"
    if f() == g():
        return "neither"


print(which_is_larger(lambda: f(5), lambda: g(10)))
print(which_is_larger(lambda: f(25), lambda: g(25)))
print(which_is_larger(lambda: f(10), lambda: g(5)))
