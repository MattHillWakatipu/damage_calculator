import matplotlib.pyplot as plt
import numpy as np

from classes.fighter import Fighter
from classes.monk import Monk
from classes.nomad import Nomad

min_ac = 10
max_ac = 24

if __name__ == '__main__':
    monk = Monk(dexterity=4, proficiency_bonus=3, equipment_bonus=0)
    fighter = Fighter(strength=5, proficiency_bonus=3, equipment_bonus=1)
    nomad = Nomad(dexterity=3, proficiency_bonus=3, equipment_bonus=0, fighting_style=2, favoured_bonus=4)

    monk_average = np.zeros(30)
    nomad_average = np.zeros(30)
    nomad_favoured_average = np.zeros(30)
    fighter_average = np.zeros(30)

    for ac in range(min_ac, max_ac + 1):
        monk_average[ac] = monk.calculate_ten_turn_average(ac)
        nomad_average[ac] = nomad.calculate_ten_turn_average(ac, False)
        nomad_favoured_average[ac] = nomad.calculate_ten_turn_average(ac, True)
        fighter_average[ac] = fighter.calculate_ten_turn_average(ac)

    fig, ax = plt.subplots()
    ax.set_xlim(min_ac, max_ac)

    ax.plot(monk_average, label='Monk')
    ax.plot(nomad_average, label='Nomad')
    ax.plot(nomad_favoured_average, label='Nomad (FE)')
    ax.plot(fighter_average, label='Fighter')

    ax.set_xlabel('Target Armour Class')
    ax.set_ylabel('Average Damage Per Turn')
    ax.set_title("10-Turn Average Damage")
    ax.legend()
    plt.show()
