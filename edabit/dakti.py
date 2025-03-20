"""
Very hard
First, organize the words based on the numbers they have, then delete the numbers once they are organized.
"""

class Dakiti:
    def dakiti(self, chorus):
        orginized_chorus = []
        split_chorus = chorus.split(" ")
        for i in range(0, len(split_chorus) - 1):
            orginized_chorus.append("")
        print("orginized_chorus", orginized_chorus)
        #  organize the words based on the numbers they have
        for i in range(1, len(split_chorus)):
            for word in split_chorus:
                if str(i) in word:
                    orginized_chorus[i - 1] = word

        return orginized_chorus


if __name__ == "__main__":
    obj = Dakiti()
    print(obj.dakiti("worl2d hell1o "))  # note that trailing space is missing
    print(obj.dakiti("i2s th1s a3 t4est    "))
