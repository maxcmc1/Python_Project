# create a function that takes a height as a parameter and prints out a Christmas tree using *

# height = 4

def print_christmas_tree(height):
    for k in range(height):
        print(" " * (height - 1 - k) + "*" * (1 + 2*k))
    print(" " * (height-1) + "|")


print_christmas_tree(4)