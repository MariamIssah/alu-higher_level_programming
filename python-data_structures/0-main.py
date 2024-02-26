#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        return len(sentence), sentence[0]
    else:
        return 0, None

# Uncomment the following lines to test the function
# print(multiple_returns("Holberton is so cool"))
# print(multiple_returns("H"))
# print(multiple_returns(""))

