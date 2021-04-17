import matplotlib.pyplot as plt
import numpy as np

from classes.monk import Monk

if __name__ == '__main__':
    hazel = Monk(dexterity=4, proficiency_bonus=3, equipment_bonus=0)
    hazel_rested = []
    hazel_spent = []

    for i in range(10, 25):
        hazel_rested.append(hazel.rested_turn(i))
        hazel_spent.append(hazel.spent_turn(i))

    print(hazel_rested)
    print(hazel_spent)

    # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(hazel_rested, label='Hazel Rested')
    ax.plot(hazel_spent, label='Hazel Spent')
    # ax.plot(x, x, label='linear')  # Plot some data on the axes.
    # ax.plot(x, x ** 2, label='quadratic')  # Plot more data on the axes...
    # ax.plot(x, x ** 3, label='cubic')  # ... and some more.
    ax.set_xlabel('x label')  # Add an x-label to the axes.
    ax.set_ylabel('y label')  # Add a y-label to the axes.
    ax.set_title("Simple Plot")  # Add a title to the axes.
    ax.legend()  # Add a legend.
    plt.show()
