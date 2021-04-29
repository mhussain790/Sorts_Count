"""
Author: Masud Hussain
Course: CS162
Assignment: 4D
"""


def bubble_sort(a_list):
    """
    bubble sort method that takes a unsorted list as a parameter
    and returns a sorted list.

    :param a_list:
    :return: t
    """

    comparison = 0
    exchange = 0
    t = ()

    n = len(a_list)
    for pass_num in range(len(a_list) - 1):

        for j in range(len(a_list) - 1 - pass_num):
            comparison += 1

            if a_list[j] > a_list[j + 1]:
                temp = a_list[j]
                a_list[j] = a_list[j + 1]

                a_list[j + 1] = temp
                exchange += 1

    # Add both variables to the tuple and print tuple
    t = (comparison, exchange)
    print(t)


def insertion_sort(a_list):
    """
    insertion sort method that takes a unsorted list as a parameter
    and returns a sorted list.

    :param a_list:
    :return: t
    """

    comparison = 0
    exchange = 0
    t = ()

    for i in range(1, len(a_list)):
        value = a_list[i]
        position = i - 1

        while position >= 0:
            
            # Split the conditional statements in order to count comparisons
            if value < a_list[position]:

                a_list[position + 1] = a_list[position]
                position -= 1

                comparison += 1
                exchange += 1
            else:
                comparison += 1
                break
        a_list[position + 1] = value

    # Add both variables to the tuple and print tuple
    t = (comparison, exchange)
    print(t)
