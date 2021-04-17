def calculate_average_damage(die_size):
    """
    Calculate average damage, including the amount contributed by critical hits.

    :param die_size:    Size of the die.
    :return:            Average damage of the attack.
    """
    return calculate_average_roll(die_size) + calculate_critical_contribution(die_size)


def calculate_average_roll(die_size):
    """
    Calculate the average roll of the die.

    :param die_size:    Size of the die.
    :return:            Average roll of the die.
    """
    return die_size / 2 + 0.5


def calculate_critical_contribution(die_size):
    """
    Calculate the damage contributed by critical hits.

    :param die_size:    Size of the die.
    :return:            Damage contributed by critical hits.
    """
    return 1 / 20 * calculate_average_roll(die_size)


def calculate_accuracy(target_ac, to_hit_modifier):
    """
    Calculate the accuracy to hit a given target.

    :param target_ac:           The armour class of the target.
    :param to_hit_modifier:     The to-hit modifier of the attacker.
    :return:                    Probability to hit the target.
    """
    return (21 - (target_ac - to_hit_modifier)) / 20


def calculate_accuracy_advantage(target_ac, to_hit_modifier):
    """
    Calculate the accuracy to hit a given target.

    :param target_ac:           The armour class of the target.
    :param to_hit_modifier:     The to-hit modifier of the attacker.
    :return:                    Probability to hit the target.
    """
    return 1 - ((target_ac - to_hit_modifier - 1) ** 2 / 400)
