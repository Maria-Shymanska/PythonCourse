# It is necessary to write a function for the implementation of the following game algorithm.
# The input of the game function is two arguments: a list consisting of lists, and an initial value of power - the player's energy.
# Internal lists are lists with a numerical value of energy that a player can absorb if they are less than or equal to their energy.
# After absorbing an item in the list, it moves on through the list and either absorbs the list completely to the end, or,
# if it finds energy higher than its own, leaves it and transitions to the next list.
# At the end of traversing all lists, the function should return the player's total energy gained.

# Example list:

# [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
# For this list and an initial energy of 1, the player will absorb the first two values from the first list
# and leave it when they meet the value of 5, because they will have an energy of 3 at that point.
# The second list will skip right away, and the third will completely absorb and get the final energy of 6.


def game(terra, power):
    for sublist in terra:
        for element in sublist:
            if element <= power:
                power += element
            else:
                break
    return power


print_game = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
