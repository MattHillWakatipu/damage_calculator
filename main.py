import random


def roll_die(max_roll):
    """
    Roll die of passed size.
    :param max_roll: Maximum possible roll.
    :return: Result of the die.
    """
    return random.randint(1, max_roll)


def sharpshooter_attack(ac):
    """
    Single attack with sharpshooter at level 5.
    :param ac: AC of target creature.
    :return: Damage caused by attack.
    """
    attack_roll = roll_die(20) + 3

    if attack_roll == 23:
        return roll_die(8) + roll_die(8) + 13

    if attack_roll >= ac:
        return roll_die(8) + 13

    return 0


def snipe_attack(ac):
    """
    Snipe attack with sharpshooter at level 5.
    :param ac: AC of target creature.
    :return: Damage caused by attack.
    """
    attack_roll = roll_die(20) + 3

    if attack_roll == 23:
        return roll_die(8) + roll_die(8) + roll_die(8) + roll_die(8) + 13

    if attack_roll >= ac:
        return roll_die(8) + roll_die(8) + 13

    return 0


def longsword_attack(ac):
    """
    Single longsword attack at level 5.
    :param ac: AC of target creature.
    :return: Damage caused by attack.
    """
    attack_roll = roll_die(20) + 8

    if attack_roll == 28:
        return roll_die(8) + roll_die(8) + 5

    if attack_roll >= ac:
        return roll_die(8) + 5

    return 0


def expend_superiority_dice():
    """
    Expend all superiority dice for level 5 fighter.
    :return: Total damage caused by superiority dice.
    """
    total_damage = 0
    for x in range(4):
        total_damage += roll_die(8)

    return total_damage


def emei_attack(ac):
    """
    Single emei attack at level 5.
    :param ac: AC of target creature.
    :return: Damage caused by attack.
    """
    attack_roll = roll_die(20) + 7

    if attack_roll == 27:
        return roll_die(8) + roll_die(8) + 4

    if attack_roll >= ac:
        return roll_die(8) + 4

    return 0


def unarmed_attack(ac):
    """
    Single unarmed attack at level 5.
    :param ac: AC of target creature.
    :return: Damage caused by attack.
    """
    attack_roll = roll_die(20) + 7

    if attack_roll == 27:
        return roll_die(6) + roll_die(6) + 4

    if attack_roll >= ac:
        return roll_die(6) + 4

    return 0


def abika_normal(ac):
    """
    Full turn of Abika at level 5.
    :param ac: AC of target creature.
    :return: Damage caused by full turn.
    """
    return sharpshooter_attack(ac) + sharpshooter_attack(ac)


def abika_burst(ac):
    """
    Full burst turn of Abika at level 5.
    :param ac: AC of target creature.
    :return: Damage caused by full turn.
    """
    return sharpshooter_attack(ac) + sharpshooter_attack(ac) + snipe_attack(ac)


def abika_fresh(ac):
    """
    Calculate damage caused over 5 rounds of combat, starting from fresh.
    :param ac: AC of target creature.
    :return: Damage caused during combat.
    """
    total_damage = 0

    for x in range(4):
        total_damage += abika_burst(ac)

    total_damage += abika_normal(ac)

    return total_damage


def abika_spent(ac):
    """
    Calculate damage caused over 5 rounds of combat, starting from spent.
    :param ac: AC of target creature.
    :return: Damage caused during combat.
    """
    total_damage = 0

    for x in range(5):
        total_damage += abika_normal(ac)

    return total_damage


def syra_normal(ac):
    """
    Full turn of Syra at level 5.
    :param ac: AC of target creature.
    :return: Damage caused by full turn.
    """
    return longsword_attack(ac) + longsword_attack(ac) + longsword_attack(ac)


def syra_burst(ac):
    """
    Full burst turn of Syra at level 5.
    :param ac: AC of target creature.
    :return: Damage caused by full turn.
    """
    return longsword_attack(ac) + longsword_attack(ac) + longsword_attack(ac) + longsword_attack(ac) + longsword_attack(ac)


def syra_fresh(ac):
    """
    Calculate damage caused over 5 rounds of combat, starting from fresh.
    :param ac: AC of target creature.
    :return: Damage caused during combat.
    """
    total_damage = syra_burst(ac)

    for x in range(4):
        total_damage += syra_normal(ac)

    total_damage + expend_superiority_dice()

    return total_damage


def syra_spent(ac):
    """
    Calculate damage caused over 5 rounds of combat, starting from spent.
    :param ac: AC of target creature.
    :return: Damage caused during combat.
    """
    total_damage = 0

    for x in range(5):
        total_damage += syra_normal(ac)

    return total_damage


def hazel_normal(ac):
    """
    Full turn of Hazel at level 5.
    :param ac: AC of target creature.
    :return: Damage caused by full turn.
    """
    return emei_attack(ac) + emei_attack(ac) + unarmed_attack(ac)


def hazel_burst(ac):
    """
    Full burst turn of Hazel at level 5.
    :param ac: AC of target creature.
    :return: Damage caused by full turn.
    """
    return emei_attack(ac) + emei_attack(ac) + unarmed_attack(ac) + unarmed_attack(ac)


def hazel_fresh(ac):
    """
    Calculate damage caused over 5 rounds of combat, starting from fresh.
    :param ac: AC of target creature.
    :return: Damage caused during combat.
    """
    total_damage = 0

    for x in range(5):
        total_damage += hazel_burst(ac)

    return total_damage


def hazel_spent(ac):
    """
    Calculate damage caused over 5 rounds of combat, starting from spent.
    :param ac: AC of target creature.
    :return: Damage caused during combat.
    """
    total_damage = 0

    for x in range(5):
        total_damage += hazel_normal(ac)

    return total_damage


if __name__ == '__main__':

    a_fresh, a_spent, s_fresh, s_spent, h_fresh, h_spent = 0, 0, 0, 0, 0, 0
    trials = 10000

    for ac in range(10, 26):
        for n in range(trials):

            a_fresh += abika_fresh(ac)
            a_spent += abika_spent(ac)
            h_fresh += hazel_fresh(ac)
            h_spent += hazel_spent(ac)
            s_fresh += syra_fresh(ac)
            s_spent += syra_spent(ac)

        a_fresh /= trials
        a_spent /= trials
        h_fresh /= trials
        h_spent /= trials
        s_fresh /= trials
        s_spent /= trials

        print("AC:", ac)
        print("Abika, Fresh: %.2f, Spent: %.2f, Combined: %.2f" %
              (a_fresh, a_spent, a_fresh + a_spent))
        print("Syra,  Fresh: %.2f, Spent: %.2f, Combined: %.2f" %
              (s_fresh, s_spent, s_fresh + s_spent))
        print("Hazel, Fresh: %.2f, Spent: %.2f, Combined: %.2f" %
              (h_fresh, h_spent, h_fresh + h_spent))
