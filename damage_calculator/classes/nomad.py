from util.formulae import calculate_accuracy, calculate_accuracy_advantage, calculate_average_damage


# TODO refactor to clean up this class
class Nomad:
    """
    A representation of the custom Nomad class for 5th edition Dungeons and Dragons.
    """

    def __init__(self, dexterity, proficiency_bonus, equipment_bonus, fighting_style, favoured_bonus):
        """
        Create a new Nomad instance.

        :param dexterity:           The dexterity score.
        :param proficiency_bonus:   The proficiency bonus.
        :param equipment_bonus:     The equipment bonus.
        :param fighting_style:      Accuracy bonus conferred from a fighting style.
        :param favoured_bonus:      Damage bonus conferred from favoured enemy.
        """
        self.to_hit_modifier = dexterity + proficiency_bonus + equipment_bonus + fighting_style
        self.damage_modifier = dexterity + equipment_bonus
        self.favoured_bonus = favoured_bonus

    def weapon_attack(self, target_ac):
        """
        Single weapon attack.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy(target_ac, self.to_hit_modifier)
        average_damage = calculate_average_damage(8) + self.damage_modifier
        return probability * average_damage

    def weapon_attack_favoured(self, target_ac):
        """
        Single weapon attack with favoured bonus.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy(target_ac, self.to_hit_modifier)
        average_damage = calculate_average_damage(8) + self.damage_modifier + self.favoured_bonus
        return probability * average_damage

    def weapon_attack_resolve(self, target_ac):
        """
        Single weapon attack.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy_advantage(target_ac, self.to_hit_modifier)
        average_damage = calculate_average_damage(8) + self.damage_modifier
        return probability * average_damage

    def weapon_attack_favoured_resolve(self, target_ac):
        """
        Single weapon attack with favoured bonus.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy_advantage(target_ac, self.to_hit_modifier)
        average_damage = calculate_average_damage(8) + self.damage_modifier + self.favoured_bonus
        return probability * average_damage

    def sharpshooter_attack(self, target_ac):
        """
        Single sharpshooter attack.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy(target_ac, self.to_hit_modifier - 5)
        average_damage = calculate_average_damage(8) + self.damage_modifier + 10
        return probability * average_damage

    def sharpshooter_attack_favoured(self, target_ac):
        """
        Single sharpshooter attack.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy(target_ac, self.to_hit_modifier - 5)
        average_damage = calculate_average_damage(8) + self.damage_modifier + 10 + self.favoured_bonus
        return probability * average_damage

    def sharpshooter_attack_resolve(self, target_ac):
        """
        Single sharpshooter attack.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy_advantage(target_ac, self.to_hit_modifier - 5)
        average_damage = calculate_average_damage(8) + self.damage_modifier + 10
        return probability * average_damage

    def sharpshooter_attack_favoured_resolve(self, target_ac):
        """
        Single sharpshooter attack.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by attack.
        """
        probability = calculate_accuracy_advantage(target_ac, self.to_hit_modifier - 5)
        average_damage = calculate_average_damage(8) + self.damage_modifier + 10 + self.favoured_bonus
        return probability * average_damage

    def rested_turn(self, target_ac):
        """
        Calculate the average damage dealt during a turn with all abilities available.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by turn.
        """
        return self.sharpshooter_attack_resolve(target_ac) * 2

    def rested_favoured_turn(self, target_ac):
        """
        Calculate the average damage dealt during a turn with all abilities available.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by turn.
        """
        return self.sharpshooter_attack_favoured_resolve(target_ac) * 2

    def spent_turn(self, target_ac):
        """
        Calculate the average damage dealt during a turn with no resources expended.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by turn.
        """
        return self.sharpshooter_attack(target_ac) * 2

    def spent_favoured_turn(self, target_ac):
        """
        Calculate the average damage dealt during a turn with no resources expended.

        :param target_ac:   AC of target creature.
        :return:            Damage caused by turn.
        """
        return self.sharpshooter_attack_favoured(target_ac) * 2

    def no_ss_rested_turn(self, target_ac):
        return self.weapon_attack_resolve(target_ac) * 2

    def no_ss_rested_favoured_turn(self, target_ac):
        return self.weapon_attack_favoured_resolve(target_ac) * 2

    def no_ss_spent_turn(self, target_ac):
        return self.weapon_attack(target_ac) * 2

    def no_ss_spent_favoured_turn(self, target_ac):
        return self.weapon_attack_favoured(target_ac) * 2

    def calculate_ten_turn_average(self, target_ac, favoured):
        """
        Calculate the average damage dealt over ten turns.

        :param target_ac:   AC of target creature.
        :param favoured:    Boolean value of whether the target is a favoured enemy.
        :return:            Damage caused over 10 turns.
        """
        if favoured:
            rested_damage = self.rested_favoured_turn(target_ac)
            spent_damage = self.spent_favoured_turn(target_ac)
        else:
            rested_damage = self.rested_turn(target_ac)
            spent_damage = self.spent_turn(target_ac)
        return rested_damage * 3 + spent_damage * 7
