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

    if attack_roll >= 28:
        return roll_die(8) + roll_die(8) + 5

    if attack_roll >= ac:
        return roll_die(8) + 5

    return 0


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


def abika_dpr(ac):
    normal = sharpshooter_attack(ac) + sharpshooter_attack(ac)
    burst = sharpshooter_attack(ac) + sharpshooter_attack(ac) + snipe_attack(ac)

    return normal, burst


def syra_dpr(ac):
    normal = longsword_attack(ac) + longsword_attack(ac) + longsword_attack(ac)
    burst = longsword_attack(ac) + longsword_attack(ac) + longsword_attack(ac) + longsword_attack(ac) + longsword_attack(ac)

    return normal, burst


def hazel_dpr(ac):
    normal = emei_attack(ac) + emei_attack(ac) + unarmed_attack(ac)
    burst = emei_attack(ac) + emei_attack(ac) + unarmed_attack(ac) + unarmed_attack(ac)

    return normal, burst


if __name__ == '__main__':

    abika_normal, abika_burst, syra_normal, syra_burst, hazel_normal, hazel_burst = 0, 0, 0, 0, 0, 0
    trials = 100000

    for ac in range(10, 25):
        for n in range(trials):

            a_normal, a_burst = abika_dpr(ac)
            s_normal, s_burst = syra_dpr(ac)
            h_normal, h_burst = hazel_dpr(ac)

            abika_normal += a_normal
            abika_burst += a_burst
            syra_normal += s_normal
            syra_burst += s_burst
            hazel_normal += h_normal
            hazel_burst += h_burst

        abika_normal /= trials
        abika_burst /= trials
        syra_normal /= trials
        syra_burst /= trials
        hazel_normal /= trials
        hazel_burst /= trials

        print("AC:", ac)
        print("Abika, Normal: % .2f, Burst: % .2f" % (abika_normal, abika_burst))
        print("Syra,  Normal: % .2f, Burst: % .2f" % (syra_normal, syra_burst))
        print("Hazel, Normal: % .2f, Burst: % .2f" % (hazel_normal, hazel_burst))
