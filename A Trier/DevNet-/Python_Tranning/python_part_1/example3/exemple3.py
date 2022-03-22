#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 1
Author: AZIZI Sajjad <sajjaad.azizi@yahoo.com>

example3.py
Illustrate the following concepts:
- Creating and using dictionaries
- Creating and using lists
- Working with for loops
- Conditional statements
"""

__author__ = "AZIZI Sajjad"
__author_email__ = "sajjaad.azizi@yahoo.com"
__copyright__ = "Copyright (c) 2020 SDACO, Inc."
__license__ = "CCNA"

# Example Dictionary
#{author = {"name": "Sajjad", "color": "red", "shape": "circle"}
author = {"name": __author__, "color": "red", "shape": "circle"}

# A list of colors
colors = ["yellow", "blue", "green", "red", "black"]
students = ["Mary","John","Jimmy"]

# A list of dictionaries
favorite_colors = [
                      {
                          "student": "Mary",
                          "color": "yellow"
                      },
                      {
                          "student": "John",
                          "color": "blue"
                      },
                      {
                          "student": "Jimmy",
                          "color": "black"
                      }
                  ]


def color_compare():
    #print("new_color", new_color)
    for std_color in favorite_colors:
        #print('-----------------------------')
        #print("std_color:", std_color)
        if std_color['color'] == new_color:
            #print('*******************************')
            print("You have the same favorite as", std_color['student'])

# Entry point for program
if __name__ == '__main__':
    print("The author's name is {}.".format(author["name"]))
    print("His favorite color is {}.".format(author["color"]))
    print("")
    print("The current colors are:")
    for n in colors:
        print(n)
    print("")
    # Ask user for favorite color and compare to author's color
    new_color = input("What is your favorite color? ")
    if new_color == author["color"]:
        print("You have the same favorite as {}.".format(author["name"]))
        print("")
    # See if this is a new color for the list
    if new_color not in colors:
        print("That's a new color, adding it to the list!")
        colors.append(new_color)
        print('-----------------------------')
        print('New colors Liste :')
        for i in colors:
            print(i)
        print('-----------------------------')
        # Print update message about the new colors list
        message = ("There are now {} colors in the list. ".format(len(colors)))
        # format(colors[-1]) => -1 : Dernier element de la liste
        #            [-5        -4      -3       -2      -1]
        #   colors = ["yellow", "blue", "green", "red", "black"]
        #            [0          1       2        3      4]
        message += "The color you added was {}.".format(colors[-1])
        print(message)
    else:
        pass
    color_compare()

    for i in range(1, 10):
        print('1*******', i)
        color_compare()

    print('###########################################' * 2);

    n = 1
    while n < 10:
        color_compare()
        print('########', n)
        n = n+1