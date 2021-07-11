from util.formulae import calculate_accuracy, calculate_average_damage


class Kara:
    """
    A representation of the Monk class for 5th edition Dungeons and Dragons.
    """

    def __init__(self, strength, proficiency_bonus, equipment_bonus):
        """
        Create a new Fighter instance.

        :param strength:            The strength score.
        :param proficiency_bonus:   The proficiency bonus.
        :param equipment_bonus:     The equipment bonus.
        """
        self.to_hit_modifier = strength + proficiency_bonus + equipment_bonus
        self.damage_modifier = strength + equipment_bonus

    def weapon_attack(self, target_ac):
        """
        Single weapon attack.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy(target_ac, self.to_hit_modifier)
        average_damage = calculate_average_damage(8) + self.damage_modifier
        return probability * average_damage

    def booming_blade(self, target_ac):
        """
        Booming blade cantrip.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy(target_ac, self.to_hit_modifier)
        average_damage = (calculate_average_damage(8) * 4) + self.damage_modifier
        return probability * average_damage

    def spent_turn(self, target_ac):
        """
        Calculate the average damage dealt during a turn with no resources expended.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by turn.
        """
        return self.weapon_attack(target_ac) + self.booming_blade(target_ac)

    def calculate_ten_turn_average(self, target_ac):
        """
        Calculate the average damage dealt over ten turns.

        :param target_ac:   AC of target creature.
        :return:            Damage caused over 10 turns.
        """
        return self.spent_turn(target_ac) * 10
