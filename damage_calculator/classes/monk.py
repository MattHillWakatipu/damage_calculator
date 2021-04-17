from util.formulae import calculate_average_roll, calculate_accuracy


class Monk:
    def __init__(self, dexterity, proficiency_bonus, equipment_bonus):
        self.to_hit_modifier = dexterity + proficiency_bonus + equipment_bonus
        self.damage_modifier = dexterity + equipment_bonus

    def weapon_attack(self, target_ac):
        """
        Single weapon attack.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy(target_ac, self.to_hit_modifier)
        average_damage = calculate_average_roll(8) + self.damage_modifier
        return probability * average_damage

    def unarmed_attack(self, target_ac):
        """
        Single unarmed attack.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy(target_ac, self.to_hit_modifier)
        average_damage = calculate_average_roll(6) + self.damage_modifier
        return probability * average_damage
