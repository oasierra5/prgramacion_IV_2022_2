from superHeroe import SuperHeroe
from army import Weapon

hammer = Weapon("hammer", 6, 4)
axe = Weapon("axe", 4, 5)

thor = SuperHeroe("Thor", 20, 3, True, axe)
hulk = SuperHeroe("Hulk", 20, 5, False, hammer)

print("1. Salud de hulk", hulk.health)
print("2. Resistencia del hacha: ", axe.endurance)
thor.attack(hulk)
print("3. Salud de Hulk: ",hulk.health)
print("4. Resistencia del hacha: ", axe.endurance)

thor.find_improvement("axe")
print("5. Categoria del hacha: ", axe.category)
print("6. Resistencia del hacha: ", axe.endurance)
print("7. Destruccion del hacha: ", axe.destruction)

thor.attack(hulk)
print("8. Salud de Hulk: ", hulk.health)
