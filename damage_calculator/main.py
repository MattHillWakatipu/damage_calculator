import matplotlib.pyplot as plt
import numpy as np

from classes.monk import Monk
from classes.nomad import Nomad

if __name__ == '__main__':
    monk = Monk(dexterity=4, proficiency_bonus=3, equipment_bonus=0)
    monk_rested = []
    monk_spent = []

    nomad = Nomad(dexterity=3, proficiency_bonus=3, equipment_bonus=0, fighting_style=2, favoured_bonus=4)
    nomad_rested = []
    nomad_spent = []
    nomad_rested_favoured = []
    nomad_spent_favoured = []

    for i in range(10, 25):
        monk_rested.append(monk.rested_turn(i))
        monk_spent.append(monk.spent_turn(i))

        nomad_rested.append(nomad.rested_turn(i))
        nomad_spent.append(nomad.spent_turn(i))
        nomad_rested_favoured.append(nomad.rested_favoured_turn(i))
        nomad_spent_favoured.append(nomad.spent_favoured_turn(i))

    # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(monk_rested, label='Monk Rested')
    ax.plot(monk_spent, label='Monk Spent')
    ax.plot(nomad_rested_favoured, label='Nomad Rested (f)')
    ax.plot(nomad_spent_favoured, label='Nomad Spent (f)')
    ax.plot(nomad_rested, label='Nomad Rested')
    ax.plot(nomad_spent, label='Nomad Spent')
    # ax.plot(x, x, label='linear')  # Plot some data on the axes.
    # ax.plot(x, x ** 2, label='quadratic')  # Plot more data on the axes...
    # ax.plot(x, x ** 3, label='cubic')  # ... and some more.
    ax.set_xlabel('x label')  # Add an x-label to the axes.
    ax.set_ylabel('y label')  # Add a y-label to the axes.
    ax.set_title("Simple Plot")  # Add a title to the axes.
    ax.legend()  # Add a legend.
    plt.show()
