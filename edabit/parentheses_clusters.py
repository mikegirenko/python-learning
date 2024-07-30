"""
Very Hard
Write a function that groups a string into parentheses clusters. Each cluster should be balanced.
"""


class ParenthesesClusters:

    def split(self, str_in) -> list:
        list_out = []
        list_length = len(str_in)
        i = 0
        ii = -1
        while i < list_length:
            if str_in[i] == "(":
                if str_in[ii] == ")":
                    p_to_append = str_in[i] + str_in[ii]
                    list_out.append(p_to_append)
            i += 1
            ii -= 1

        return list_out


if __name__ == "__main__":
    obj = ParenthesesClusters()
    print(obj.split("()()()"))
    print(obj.split("((()))"))
    print(obj.split("((()))(())()()(()())"))
