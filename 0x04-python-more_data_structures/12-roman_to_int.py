#!/usr/bin/python3
def roman_to_int(roman_string):
    rd = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    elif not roman_string or not all(char in rd for char in roman_string):
        # raise ValueError("Invalid Roman numeral")
        return 0
    elif roman_string:
        num = 0
        prev = 0
        for ch in roman_string:
            value = rd[ch]
            if value > prev:
                # num = (num - prev) + (value - prev)
                num += value - 2 * prev
            else:
                num += value
            prev = value
    if num < 0 or num > 3999:
        return 0
    else:
        return num
