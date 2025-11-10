# Write a Python function to choose a random item from a list using the random module.

import random

def choose_random_item():
    items = ["apple", "banana", "cherry", "mango", "orange"]
    choice = random.choice(items)
    print("Randomly selected item:", choice)

choose_random_item()

