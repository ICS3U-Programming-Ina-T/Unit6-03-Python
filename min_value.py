#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 31, 2022
# This program uses a for loop to generate and
# print random numbers in a list, then
# displays the smallest value

import constants
import random


# function calculates the min value in the list of elements
def find_min_value(ran_nums):

    min = ran_nums[0]

    # calculate the min value
    for counter in ran_nums:
        if min > counter:
            min = counter

    return min


def main():
    # initializing counter
    counter = 0

    # declaring variable
    ran_nums_user = []

    # display opening message to console
    print("This program generates a list of random "
          "numbers between 0 and 100, then determines the smallest number.")
    print("")

    # displays random numbers and calculates average
    for counter in range(constants.MAX_ARRAY_SIZE):
        ran_nums_user.append(random.randint(constants.MIN_NUM,
                                            constants.MAX_NUM))
        print("{} added to the list at "
              "position {}" .format(ran_nums_user[counter], counter))

    min_user = find_min_value(ran_nums_user)
    print("")
    print("The min value is: {}" .format(min_user))


if __name__ == "__main__":
    main()
