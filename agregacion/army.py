class Weapon:

    def __init__(self, name_weapon, endurance, destruction, category=1):
        self.name_weapon = name_weapon
        self.endurance = endurance
        self.destruction = destruction
        self.category = category

    def __str__(self):
        return self.name_weapon

    def raise_category(self):
        self.category += 1
        self.endurance += 2
        self.destruction += 1
