#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    sum1 = 0
    i = 0
    if isinstance(roman_string, str):
        while i < len(roman_string) - 1:
            if roman[roman_string[i]] >= roman[roman_string[i + 1]]:
                sum1 += roman[roman_string[i]]
            else:
                sum1 -= roman[roman_string[i]]
            i += 1
        sum1 += roman[roman_string[i]]
        return sum1
    else:
        return None
