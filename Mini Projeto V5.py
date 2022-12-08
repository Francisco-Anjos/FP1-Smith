import random, time

print("Please input your name:")
playerinput = input()
command2 = input("Press [Enter] to continue.")
print("-----")
SwordAmount = 0
ArmorAmount = 0
GemAmount = 0

class player:
    player_level = 0
    self_xp = 0
    Next_Level = 50
    if self_xp >= 50:
        self_xp = self_xp - Next_Level
        player_level = player_level + 1
        print("You Leveled up!\nYour new level is: " + str(player_level))
    self_name = playerinput
    def __init__(self, player_level, self_xp, player_gold, Next_Level):
        self.xp = self_xp
        self.level = player_level
        self.name = playerinput
        self.gold = player_gold
        self.nextlevel = Next_Level
    def display(self):
        print("Name: " + self.name)
        print("Level: " + str(self.level))
        print("XP: " + str(self.xp))
        print("Gold: " + str(self.gold))
        print("XP needed for next level: " + str(self.nextlevel))

class resources:
    gold = 0
    def __init__(self, Resources, gold, resource_amount):
        self.resource = Resources
        self.gold = gold
        self.resourceamount = resource_amount
    def display(self):
        print("Resource: " + self.resource)
        print("Sell Value: " + str(self.gold))
        print("Resource Amount: " + str(self.resourceamount))
        
class Wood(resources):
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
        print("Item: " + self.name)
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
materials  = [Wood(), Leather(), Iron()]

command = ""
while(command != "Quit" or "Exit"):
    while player.gold >= 0:  
        time.sleep(0.5)
        for player in playerstats:
            player.display()
            print("-----") 
            
        time.sleep(1)    
        
        for item in inventory:
            item.display()
            print("-----")
            
        time.sleep(2) 
        
        print("Wood, Iron, Leather: " + resources.resourceamount(Wood) + "," + resources.resourceamount(Iron) + "," + resources.resourceamount(Leather))
        
        for resources in materials:
            resources.display()
            print("-----")
            
        time.sleep(3) 
        
        print("Press -1- to Sell Items")
        print("Press -2- to Buy Resources")
        print("Press -3- to Craft Items")
        print("Type -Quit- to exit")
        
        PlayerChoice = input()
        if PlayerChoice == "1":
            print("Sell 1 -Sword- for 12 gold\n" "Sell 1 -Armor- for 36 gold\n" "Sell 1 -Gem- for 8 gold")
            PlayerChoice2 = input()
            if PlayerChoice2 == "Sword":
                if SwordAmount >= 1:
                    player.gold = player.gold + 12
                    print("Processing...")
                    time.sleep(0.5)
                else:
                    print("You don't have any swords.")
            elif PlayerChoice2 == "Armor":
                if ArmorAmount >= 1:
                    player.gold = player.gold + 36
                    print("Processing...")
                    time.sleep(0.5)      
            elif PlayerChoice2 == "Gem":
                if GemAmount >= 1:
                    player.gold = player.gold + 8
                    print("Processing...")
                    time.sleep(0.5)       
        if PlayerChoice == "2":
            print("Buy 1 -Wood- for 2 gold.\n" "Buy 1 -Iron- for 4 gold.\n" "Buy 1 -Leather- for 3 gold.")
            PlayerChoice3 = input()
            if PlayerChoice3 == "Wood":
                if player.gold >= 2:
                    player.gold = player.gold - 2
                    resources.resourceamount(Wood) + 1
                    print("Processing payment...")
                    time.sleep(1)      
            elif PlayerChoice3 == "Iron":
                if player.gold >= 4:
                    player.gold = player.gold - 4
                    resources.resourceamount(Iron) + 1
                    print("Processing payment...")
                    time.sleep(1)      
            elif PlayerChoice3 == "Leather":
                if player.gold >= 3:
                    player.gold = player.gold - 3
                    resources.resourceamount(Leather) + 1
                    print("Processing payment...")
                    time.sleep(1)      
        if PlayerChoice == "3":
            print("-Sword- = 1 Wood, 1 Iron.\n-Armor- = 2 leather 2 Iron.\n-Gem- = 1 Iron.")
            PlayerChoice4 = input()
            if PlayerChoice4 == "Sword":
                if  resources.resourceamount(Wood, Iron) == 1:
                        print("Forging...")
                        player.self_xp = player.self_xp + 2
                        time.sleep(0.5)
                else:
                    print("Not enough resources")
            elif PlayerChoice4 == "Armor":
                if  resources.resourceamount(Iron, Leather) == 2:
                    print("Forging...")
                    player.self_xp = player.self_xp + 4
                    time.sleep(0.5)
                else:
                    print("Not enough resources")
            elif PlayerChoice4 == "Gem":
                if  resources.resourceamount(Iron) == 1:
                    print("Forging...")
                    player.self_xp = player.self_xp + 1
                    GemAmount + 1 
                    time.sleep(0.5)     
                else:
                    print("Not enough resources")   
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
        
if player.gold == 1000:
    print("You  won the game! :)")