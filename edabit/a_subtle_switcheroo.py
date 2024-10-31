"""
Very Hard
Create a function which replaces all instances of "nts" with "nce" and vice versa if they are at the end of a word.
"""


class ASubtleSwitcheroo:
    def switcheroo(self, string_in) -> str:
        string_in_as_list = string_in.split(" ")
        i = 0
        index_counter_nts = []
        index_counter_nce = []
        # TODO implement "if they are at the end of a word."
        for item in string_in_as_list:
            if "nts" in item: #  and item[-1].isalpha() ??
                index_counter_nts.append(i)
            if "nce" in item:  #  and item[-1] == "e" ??
                index_counter_nce.append(i)
            i += 1

        for i in range(len(index_counter_nts)):
            temp = string_in_as_list[index_counter_nts[i]]
            temp_temp = temp.replace("nts", "nce")
            string_in_as_list[index_counter_nts[i]] = temp_temp

        for i in range(len(index_counter_nce)):
            temp = string_in_as_list[index_counter_nce[i]]
            temp_temp = temp.replace("nce", "nts")
            string_in_as_list[index_counter_nce[i]] = temp_temp

        list_as_string_out = " ".join(string_in_as_list)

        return list_as_string_out


if __name__ == "__main__":
    obj = ASubtleSwitcheroo()
    assert obj.switcheroo("The elephants in France were chased by ants!") == "The elephance in Frants were chased by ance!"
    assert obj.switcheroo("While he rants, I fall into a trance...") == "While he rance, I fall into a trants..."
    assert obj.switcheroo("Bounced over the fence!") == "Bounced over the fents!"
