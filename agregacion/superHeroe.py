class SuperHeroe:

    def __init__(self, name, health, stroke, shield, weapon):
        self.name = name
        self.health = health
        self.stroke = stroke
        self.shield = shield
        self.weapon = weapon

    def __str__(self):
        return self.name

    def attack(self, other):
        other.health -= self.stroke + self.weapon.destruction
        self.weapon.endurance -= 1

    def find_improvement(self, type_weapon):
        if self.weapon.name_weapon == type_weapon:
            self.weapon.raise_category()
