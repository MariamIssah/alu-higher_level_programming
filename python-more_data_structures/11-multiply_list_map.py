#!/usr/bin/python3

def multiply_list(lst, multiplier):
    return list(map(lambda x: x * multiplier, lst))

# Test the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    multiplier = 10
    result = multiply_list(my_list, multiplier)
    print(result)
