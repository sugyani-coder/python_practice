# Write a Python function to shuffle a list randomly using the random module.

import random


def import_random():
    items = [1,2,3,4,5,6,7,8,9,10]
    random.shuffle(items)
    print("Shuffled list:", items)

import_random()


