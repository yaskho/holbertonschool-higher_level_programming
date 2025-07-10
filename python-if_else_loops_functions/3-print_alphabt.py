#!/usr/bin/python3
print("{}".format("".join(chr(letter) for letter in range(97, 123) if chr(letter) not in ['q', 'e'])), end="")
