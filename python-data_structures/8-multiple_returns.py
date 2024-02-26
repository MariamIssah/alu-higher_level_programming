#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:  # Check if the sentence is not empty
        return len(sentence), sentence[0]
    else:
        return 0, None

# Uncomment the following lines to test the function
# sentence = "At school, I learnt C!"
# length, first = multiple_returns(sentence)
# print("Length: {:d} - First character: {}".format(length, first))
