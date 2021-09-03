class Nature:

    # stats: 'hp' 'attack' 'defense' 'special-attack' 'special-defense' 'speed'

    def __init__(self):
        self.increased_stat = 1.1
        self.decreased_stat = 0.9
        self.neutral_stat = 1


class Hardy(Nature):

    def multiplier(self, stat):
        return self.neutral_stat


class Lonely(Nature):

    def multiplier(self, stat):
        if stat == 'attack':
            return self.increased_stat
        elif stat == 'defense':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Brave(Nature):

    def multiplier(self, stat):
        if stat == 'attack':
            return self.increased_stat
        elif stat == 'speed':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Adamant(Nature):

    def multiplier(self, stat):
        if stat == 'attack':
            return self.increased_stat
        elif stat == 'special-attack':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Naughty(Nature):

    def multiplier(self, stat):
        if stat == 'attack':
            return self.increased_stat
        elif stat == 'special-defense':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Bold(Nature):

    def multiplier(self, stat):
        if stat == 'defense':
            return self.increased_stat
        elif stat == 'attack':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Docile(Nature):

    def multiplier(self, stat):
        return self.neutral_stat


class Relaxed(Nature):

    def multiplier(self, stat):
        if stat == 'defense':
            return self.increased_stat
        elif stat == 'speed':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Impish(Nature):

    def multiplier(self, stat):
        if stat == 'defense':
            return self.increased_stat
        elif stat == 'special-attack':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Lax(Nature):

    def multiplier(self, stat):
        if stat == 'defense':
            return self.increased_stat
        elif stat == 'special-defense':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Timid(Nature):

    def multiplier(self, stat):
        if stat == 'speed':
            return self.increased_stat
        elif stat == 'attack':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Hasty(Nature):

    def multiplier(self, stat):
        if stat == 'speed':
            return self.increased_stat
        elif stat == 'defense':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Serious(Nature):

    def multiplier(self, stat):
        return self.neutral_stat


class Jolly(Nature):

    def multiplier(self, stat):
        if stat == 'speed':
            return self.increased_stat
        elif stat == 'special-attack':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Naive(Nature):

    def multiplier(self, stat):
        if stat == 'speed':
            return self.increased_stat
        elif stat == 'special-defense':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Modest(Nature):

    def multiplier(self, stat):
        if stat == 'special-attack':
            return self.increased_stat
        elif stat == 'attack':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Mild(Nature):

    def multiplier(self, stat):
        if stat == 'special-attack':
            return self.increased_stat
        elif stat == 'defense':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Quiet(Nature):

    def multiplier(self, stat):
        if stat == 'special-attack':
            return self.increased_stat
        elif stat == 'speed':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Bashful(Nature):

    def multiplier(self, stat):
        return self.neutral_stat


class Rash(Nature):

    def multiplier(self, stat):
        if stat == 'special-attack':
            return self.increased_stat
        elif stat == 'special-defense':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Calm(Nature):

    def multiplier(self, stat):
        if stat == 'special-defense':
            return self.increased_stat
        elif stat == 'attack':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Gentle(Nature):

    def multiplier(self, stat):
        if stat == 'special-defense':
            return self.increased_stat
        elif stat == 'defense':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Sassy(Nature):

    def multiplier(self, stat):
        if stat == 'special-defense':
            return self.increased_stat
        elif stat == 'speed':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Careful(Nature):

    def multiplier(self, stat):
        if stat == 'special-defense':
            return self.increased_stat
        elif stat == 'special-attack':
            return self.decreased_stat
        else:
            return self.neutral_stat


class Quirky(Nature):

    def multiplier(self, stat):
        return self.neutral_stat
