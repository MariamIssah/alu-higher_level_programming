#!/usr/bin/python3

number = -5

if isinstance(number, int) or isinstance(number, float):
    if number > 0:
        print(f"Positive: {number}")
    elif number < 0:
        print(f"Negative: {number}")
    else:
        print("Zero")
else:
