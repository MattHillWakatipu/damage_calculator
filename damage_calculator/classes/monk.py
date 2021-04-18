from util.formulae import calculate_accuracy, calculate_average_damage


class Monk:
    """
    A representation of the Monk class for 5th edition Dungeons and Dragons.
    """

    def __init__(self, dexterity, proficiency_bonus, equipment_bonus):
        """
        Create a new Monk instance.

        :param dexterity:           The dexterity score.
        :param proficiency_bonus:   The proficiency bonus.
        :param equipment_bonus:     The equipment bonus.
        """
        self.to_hit_modifier = dexterity + proficiency_bonus + equipment_bonus
        self.damage_modifier = dexterity + equipment_bonus

    def weapon_attack(self, target_ac):
        """
        Single weapon attack.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy(target_ac, self.to_hit_modifier)
        average_damage = calculate_average_damage(8) + self.damage_modifier
        return probability * average_damage

    def unarmed_attack(self, target_ac):
        """
        Single unarmed attack.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy(target_ac, self.to_hit_modifier)
        average_damage = calculate_average_damage(6) + self.damage_modifier
        return probability * average_damage

    def rested_turn(self, target_ac):
        """
        Calculate the average damage dealt during a turn with all abilities available.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by turn.
        """
        return (self.weapon_attack(target_ac) + self.unarmed_attack(target_ac)) * 2

    def spent_turn(self, target_ac):
        """
        Calculate the average damage dealt during a turn with no resources expended.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by turn.
        """
        return self.weapon_attack(target_ac) + self.unarmed_attack(target_ac) * 2

    def calculate_ten_turn_average(self, target_ac):
        """
        Calculate the average damage dealt over ten turns.

        :param target_ac:   AC of target creature.
        :return:            Damage caused over 10 turns.
        """
        return self.rested_turn(target_ac) * 3 + self.spent_turn(target_ac) * 7
