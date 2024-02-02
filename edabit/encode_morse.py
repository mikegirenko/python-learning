"""
Create a function that takes a string as an argument and returns the Morse code equivalent.
"""


class EncodeMorse:
    def __init__(self):
        self.char_to_dots = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            " ": " ",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "&": ".-...",
            "'": ".----.",
            "@": ".--.-.",
            ")": "-.--.-",
            "(": "-.--.",
            ":": "---...",
            ",": "--..--",
            "=": "-...-",
            "!": "-.-.--",
            ".": ".-.-.-",
            "-": "-....-",
            "+": ".-.-.",
            '"': ".-..-.",
            "?": "..--..",
            "/": "-..-.",
        }

    def convert_string_to_morse_code(self, string_to_convert) -> str:
        morse_code = ""
        counter = 0
        for character in string_to_convert:
            for k, v in self.char_to_dots.items():
                if character == k:
                    if counter == 0:
                        morse_code = morse_code + v
                    else:
                        morse_code = morse_code + " " + v
                    counter += 1

        return morse_code


if __name__ == "__main__":
    encode_morse_object = EncodeMorse()

    assert (
        encode_morse_object.convert_string_to_morse_code("HELP ME !")
        == ".... . .-.. .--.   -- .   -.-.--"
    )
    assert (
        encode_morse_object.convert_string_to_morse_code("EDABBIT CHALLENGE")
        == ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
    )
