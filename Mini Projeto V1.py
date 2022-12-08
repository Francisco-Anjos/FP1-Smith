class item:                 
    gold = 1                    
    def __init__(self, name, gold):
        self.name = name
        self.gold = gold
    def canSell(self):
        return (self.gold > 0)   
    def display(self):
        print("Name: " + self.name)
        print("Sell Value " + str(self.gold))

class sword(item):
    damage = 0
    def __init__(self, damage):
        super().__init__("Sword", 1)
        self.damage = damage
        
    def display(self):
        super().display()
        print("Damage " + str(self.damage))

class gem(item):
    def __init__(self):
        super().__init__("Gem", 10)

class Armor(item):                 
    protection = 0
    def __init__(self, protection):
        super().__init__("Armor", 5)

class VorpalSword(sword):
    cursed = False
    def canSell(self):
        if (self.cursed):
            return False   
        return super().canSell()

class ChestPiece(Armor):
  pass

class Helmet(Armor):
  pass

inventory = [ sword(3), Armor(4), gem(), item("Trash", 2)]

for item in inventory:
  item.display()
  print("-----")