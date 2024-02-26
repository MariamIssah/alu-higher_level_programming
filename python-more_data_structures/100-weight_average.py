#!/usr/bin/python3



def weight_average(my_list=[]):
    if not my_list:  # Check if the list is empty
        return 0


    total_weighted_sum = 0
    total_weight = 0


    for score, weight in my_list:
        total_weighted_sum += score * weight
        total_weight += weight


    return total_weighted_sum / total_weight



# Test the function
if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
