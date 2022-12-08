import random, time, sys

print("Please input your name:")
playerinput = input()
command2 = input("Press [Enter] to continue.")
print("-----")
player_gold = 12
ResourceAmount = (0, 0, 0)
SwordAmount = (1)
ArmorAmount =(1)

class player:
    player_level = 0
    self_xp = 0
    self_name = playerinput
    def __init__(self, player_level, self_xp):
        self.xp = self_xp
        self.level = player_level
        self.name = playerinput
    def display(self):
        print("Name: " + self.name)
        print("Level: " + str(self.level))
        print("XP: " + str(self.xp))

class resources:
    gold = 0
    def __init__(self, Resources, gold):
        self.resource = Resources
        self.gold = gold
    def display(self):
        print("Name: " + self.resource)
        print("Sell Value: " + str(self.gold))
        
class wood(resources):
    def __init__(self):
        super().__init__("Wood", 2)
    def display(self):
        super().display()
        print("Just a log.")
    def canBuy(self):
        if(player.gold >= 2):
            return
        return super().canBuy()
        
class Iron(resources):
    def __init__(self):
        super().__init__("Iron", 4)
    def display(self):
        super().display()
        print("Metal forged by the blacksmiths...but it's just an ore.")

class Leather(resources):
    def __init__(self):
        super().__init__("Leather", 3)
    def display(self):
        super().display()
        print("The finest leather skinned from various animals with the help of hunters and butchers.")
        

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
        print("A weapon fit for a warrior.")

class gem(item):
    def __init__(self):
        super().__init__("Gem", 10)

class Armor(item):                 
    protection = 0
    def __init__(self, protection):
        super().__init__("Armor", 5)
        self.protection = protection

    def display(self):
        super().display()
        print("Protection " + str(self.protection))
        print("Keeps a warrior alive in the heat of battle.")

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
playerstats = [player(0, 0)]
materials  = [wood(), Leather(), Iron()]

command = ""
while(command != "Quit" or "Exit"):
    while(player_gold > 0):  
        print("-----")
        for player in playerstats:
            player.display()
            print("-----") 
            
        print("Your company's gold: " + str(player_gold) + "\n" "-----")
        
        for item in inventory:
            item.display()
            print("-----")
        
        for resources in materials:
            resources.display()
            print("-----")
        
        print("Press 1 to Sell Items or Resources")
        print("Press 2 to Buy Resources")
        print("Press 3 to Craft Items")
        print("Type Quit to exit")
        
        PlayerChoice = input()
        if PlayerChoice == "1":
            print("Sell 1 -Wood- for 2 gold.\n" "Sell 1 -Iron- for 4 gold.\n" "Sell 1 -Leather- for 3 gold.\n" "Sell 1 -Sword- for 12 gold\n" "Sell 1 -Armor- for 36 gold")
            if input() == "Wood":
                player_gold = player_gold + 2
                print("Processing...")
                time.sleep(0.5)
            elif input() == "Iron":
                player_gold = player_gold + 4
                print("Processing...")
                time.sleep(0.5)
            elif input() == "Leather":
                player_gold = player_gold + 3
                print("Processing...")
                time.sleep(0.5)
            elif input() == "Sword":
                player_gold = player_gold + 12
                print("Processing...")
                time.sleep(0.5)
            elif input() == "Armor":
                player_gold = player_gold + 36
                print("Processing...")
                time.sleep(0.5)           
        if PlayerChoice == "2":
            print("Buy 1 -Wood- for 2 gold.\n" "Buy 1 -Iron- for 4 gold.\n" "Buy 1 -Leather- for 3 gold.")
            if input() == "Wood":
                player_gold = player_gold - 2
                print("Processing...")
                time.sleep(0.5)
            elif input() == "Iron":
                player_gold = player_gold - 4
                print("Processing...")
                time.sleep(0.5)
            elif input() == "Leather":
                player_gold = player_gold - 3
                print("Processing...")
                time.sleep(0.5)      
        if PlayerChoice == "3":
            print("-Sword- = 1 Wood, 1 Iron.\n -Armor- = 2 leather 2 Iron.\n 1 -Gem- = 1 Iron.")
            if input() == "Sword":
                ResourceAmount = ResourceAmount - (1, 1, 0)
                print("Forging...")
                time.sleep(0.5)
            elif input() == "Armor":
                ResourceAmount = ResourceAmount - (0, 2, 2)
                print("Forging...")
                time.sleep(0.5)
            elif input() == "Gem":
                ResourceAmount = ResourceAmount - (0, 1, 0)
                print("Forging...")
                time.sleep(0.5)     
        if PlayerChoice == "Quit":
            PlayerQuit = input("After pressing [Enter], type -Quit- to exit. Note: This process will remove all progress.\nIf you don't wish to quit then type anything else.") 
            if input() == "Quit":
                quit()
            else:
                break                
    
    else:
        time.sleep(0.5)
        print("Oh no...You went bankrupt...")
        gameRestart = input("Press [enter] to restart game: ")
        
if player_gold == 10000:
    print("You  won the game! :)")



