#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    length = len(roman_string)

    for i in range(length):
        value = roman_map.get(roman_string[i], 0)
        # Lookahead to next char if any
        if i + 1 < length:
            next_value = roman_map.get(roman_string[i + 1], 0)
            if value < next_value:
                total -= value
            else:
                total += value
        else:
            total += value

    return total
