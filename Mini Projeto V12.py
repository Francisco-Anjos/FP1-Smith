import random, time
#GameStart
print("Please input your name:")
playerinput = input()
command2 = input("Press [Enter] to continue.")
print("-----")
SwordAmount = 0
HammerAmmount = 0
BowAmmount = 0
ArmorAmmount = 0
ChestplateAmmount = 0
BootsAmmount = 0


#player class(name,level,gold,xp)
class player:
    gold = 16
    player_level = 1
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

#resource class(Wood,Leather,Iron,String)
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

#Woodclass(descripition ,quantity ,price)       
class Wood(resources):
    def __init__(self):
        super().__init__("Wood", 2, 0)
    def display(self):
        super().display()
        print("Just a log.")
    def canBuy(self):
        if(player.gold >= 2):
            return
        return super().canBuy()

#Ironclass(descripition ,quantity ,price)            
class Iron(resources):
    def __init__(self):
        super().__init__("Iron", 4, 0)
    def display(self):
        super().display()
        print("Metal forged by the blacksmiths...but it's just an ore.")
#Leatherclass(descripition ,quantity ,price)    
class Leather(resources):
    def __init__(self):
        super().__init__("Leather", 3, 0)
    def display(self):
        super().display()
        print("The finest leather skinned from various animals with the help of hunters and butchers.")
#Stringsclass(descripition ,quantity ,price)            
class Strings(resources):
    def __init__(self):
        super().__init__("String", 1, 0)
    def display(self):
        super().display()
        print("A bundle of strings.")
#Bronzeclass(descripition ,quantity ,price)            
class Bronze(resources):
    def __init__(self):
        super().__init__("Bronze", 2, 0)
    def display(self):
        super().display()
        print("A metal cheaper than Iron.")
        
#ItemClass(gold,name)
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

#SwordClass(damage,sell value)
class Sword(item):
    damage = 0
    def __init__(self, damage):
        super().__init__("Sword", 1)
        self.damage = damage
        
    def display(self):
        super().display()
        print("Damage " + str(self.damage))
        print("A weapon fit for a warrior.")

#GemClass(price)
class Gem(item):
    def __init__(self):
        super().__init__("Gem", 10)

#BronzeGemClass(price)
class BronzeGem(item):
    def __init__(self):
        super().__init__("BronzeGem", 8)

#BowClass(damage,accuracy,sell price)
class Bow(item):
    def __init__(self, damage, accuracy):
        super().__init__("Bow", 3)
        self.damage = damage
        self.accuracy = accuracy

    def display(self):
        super().display()
        print("Damage" + str(self.damage))
        print("Accuracy" + str(self.accuracy))
        print("A hunters weapon.")

#HammerClass(damage,sell)
class Hammer(item):
    def __init__(self, damage):
       super().__init__("Hammer", 3)
       self.damage = damage
        
    def display(self):
        super().display()
        print("Damage " + str(self.damage))
        print("An unusual weapon.")

class Armor(item):                 
    protection = 0
    def __init__(self, protection, ArmorAmount):
        super().__init__("Armor", 40)
        self.protection = protection
        self.ArmorAmount = ArmorAmount

    def display(self):
        super().display()
        print("Protection " + str(self.protection))
        print("Armor Amount: " + str(self.ArmorAmount))
        print("Keeps a warrior alive in the heat of battle.")

class Chestplate(Armor):
    def __init__(self):
        super().__init__("Chestplate", 0)
    def display(self):
        super().display()
        print("Chestplate")
        
class Helmet(Armor):
    def __init__(self):
        super().__init__("Helmet", 0)
    def display(self):
        super().display()
        print("Helmet")

class Boots(Armor):
    def __init__(self):
        super().__init__("Boots", 0)
    def display(self):
        super().display()
        print("Boots")
        
class BronzeChestplate(Armor):
    def __init__(self):
        super().__init__("Bronze Chestplate", 0)
    def display(self):
        super().display()
        print("Bronze Chestplate")
        
class BronzeHelmet(Armor):
    def __init__(self):
        super().__init__("Bronze Helmet", 0)
    def display(self):
        super().display()
        print("Bronze Helmet")
        
#Criação de um instance
inventory = [Chestplate(20), Helmet(10), Boots(10), Gem(8), Sword(3), Hammer(2), Bow(3, 2), item("Trash", 2), BronzeChestplate(15), BronzeHelmet(8), BronzeGem(8)]
playerstats = [player(1, 0, 16, 50)]
materials  = [Wood(), Iron(), Leather(), Strings(), Bronze()]

command = ""
while(command != "Quit" or "Exit"):
    while(player.gold >= 0):  
        time.sleep(0.5)
        for p in playerstats:
            p.display()
            print("-----") 
            
        time.sleep(1)    
        
        for i in inventory:
            i.display()
            print("-----")
            
        time.sleep(2) 
        
        for mat in materials:
            mat.display()
            print("-----")
            
        time.sleep(3) 
        
        print("Press -1- to Sell Equipment")
        print("Press -2- to Buy Resources")
        print("Press -3- to Craft Equipment")
        print("Type -Quit- to exit")
        print("Type -Inventory- to show what you have")
        #Sell    
        PlayerChoice = input()
        if PlayerChoice == "Inventory":
            print("Chestplate: " + str(inventory[0].ArmorAmount))
            print("Bronze Chestplate: " + str(inventory[8].ArmorAmount))
            print("Helmet: " + str(inventory[1].ArmorAmount))
            print("Bronze Helmet: " + str(inventory[9].ArmorAmount))
            print("Boots: " + str(inventory[2].ArmorAmount))
            print("Gem: " + str(inventory[3].ArmorAmount))
            print("Bronze Gem: " + str(inventory[10].ArmorAmount))
            print("Sword: " + str(SwordAmount))
            print("Hammer: " + str(HammerAmmount))
            print("Bow: " + str(BowAmmount))
            playercontinue = input()
            time.sleep(0.5)
        if PlayerChoice == "1":
            print("Sell 1 -Sword- for 12 gold\nSell 1 -Armor- for up to 40 gold\nSell 1 -Gem- for 8 gold")
            PlayerChoice2 = input()
            if PlayerChoice2 == "Sword":
                if SwordAmount >= 1:
                    player.gold += 12
                    print("Processing...")
                    time.sleep(0.5)
                else:
                    print("You don't have any swords.")      
            elif PlayerChoice2 == "Armor":
                print("-----\nSell 1 -Chestplate- for 20 gold\nSell 1 -Helmet- for 10 gold.\nSell 1 -Boots- for 10 gold.\nSell 1 -BronzeChestplate- for 15 gold \nSell 1 -BronzeHelmet- for 8 gold.\nSell 1 -BronzeGem- for 8 gold-----")
                PlayerChoiceArmor = input()  
                #Sell Chestplate 
                if PlayerChoiceArmor == "Chestplate":
                    if inventory[0].ArmorAmount >= 1:
                        player.gold += 20
                        inventory[0].ArmorAmount -= 1
                        print("Processing...")
                        time.sleep(0.5)    
                    else:
                        print("You don't have any Iron Chestplates")
                #Sell Bronze Chestplate 
                elif PlayerChoiceArmor == "BronzeChestplate":
                    if inventory[8].ArmorAmount >= 1:
                        player.gold += 15
                        inventory[8].ArmorAmount -= 1
                        print("Processing...")
                        time.sleep(0.5)    
                    else:
                        print("You don't have any Bronze Chestplates")
                #Sell Helmet  
                elif PlayerChoiceArmor == "Helmet":
                    if inventory[1].ArmorAmount >= 1:
                        player.gold += 10
                        inventory[1].ArmorAmount -= 1
                        print("Processing...")
                        time.sleep(0.5) 
                    else:
                        print("You don't have any Iron Helmets")  
                #Sell Bronze Helmet  
                elif PlayerChoiceArmor == "BronzeHelmet":
                    if inventory[9].ArmorAmount >= 1:
                        player.gold += 8
                        inventory[9].ArmorAmount -= 1
                        print("Processing...")
                        time.sleep(0.5) 
                    else:
                        print("You don't have any Bronze Helmets")  
                #Sell Boots
                elif PlayerChoiceArmor == "Boots":
                    if inventory[2].ArmorAmount >= 1:
                        player.gold += 10
                        inventory[2].ArmorAmount -= 1
                        print("Processing...")
                        time.sleep(0.5)    
                    else:
                        print("You don't have any Boots")       
            elif PlayerChoice2 == "Gem":
                if inventory[3].ArmorAmount >= 1:
                    player.gold += 8
                    inventory[3].ArmorAmount -1
                    print("Processing...")
                    time.sleep(0.5) 
            elif PlayerChoice2 == "BronzeGem":
                if inventory[11].ArmorAmount >= 1:
                    player.gold += 8
                    inventory[11].ArmorAmount -= 1
                    print("Processing...")
                    time.sleep(0.5) 
        #Buy                
        if PlayerChoice == "2":
            print("Buy 1 -Wood- for 2 gold.\nBuy 1 -Iron- for 4 gold.\nBuy 1 -Leather- for 3 gold.\nBuy 3 -String- for 1 gold.\nBuy -Bronze- for 2 gold.")
            PlayerChoice3 = input()
            #Buy Wood
            if PlayerChoice3 == "Wood":
                if player.gold >= 2:
                    player.gold -= 2
                    materials[0].resourceamount += 1
                    print("Processing payment...")
                    time.sleep(1)      
            #Buy Iron
            elif PlayerChoice3 == "Iron":
                if player.gold >= 4:
                    player.gold -= 4
                    materials[1].resourceamount += 1
                    print("Processing payment...")
                    time.sleep(1)      
            #Buy Leather
            elif PlayerChoice3 == "Leather":
                if player.gold >= 3:
                    player.gold -= 3
                    materials[2].resourceamount += 1
                    print("Processing payment...")
                    time.sleep(1)   
            #Buy String
            elif PlayerChoice3 == "String":
                if player.gold >= 3:
                    player.gold -= 1
                    materials[3].resourceamount += 3
                    print("Processing payment...")
                    time.sleep(1)     
            #Buy Bronze
            elif PlayerChoice3 == "Bronze":
                if player.gold >= 2:
                    player.gold -= 2
                    materials[4].resourceamount += 1
                    print("Processing payment...")
                    time.sleep(1)            
        #Craft 
        if PlayerChoice == "3":
            print("Crafting a -Sword- = 1 Wood, 1 Iron.\nCrafting a -Hammer- = 2 Wood, 1 Iron\nCrafting a -Bow- = 2 Wood 1 String\nCrafting -Armor- = 2 leather 2 Iron.\nCrafting a -Gem- = 1 Iron.")
            PlayerChoice4 = input()
            #Craft Sword
            if PlayerChoice4 == "Sword":
                if  materials[0].resourceamount >= 1:
                    if  materials[1].resourceamount >= 1:
                        print("Forging...")
                        player.self_xp += 4
                        materials[0].resourceamount -= 1
                        materials[1].resourceamount -= 1
                        time.sleep(0.5)
                    else:
                        print("Not enough Iron")
                else:
                    print("Not enough Wood")
            #Craft Hammer
            if PlayerChoice4 == "Hammer":
                if materials[0].resourceamount >= 2:
                    if materials[1].resourceamount >= 1:
                        print("Forging...")
                        player.self_xp += 5
                        materials[0].resourceamount -= 2
                        materials[1].resourceamount -= 1
                        HammerAmmount = HammerAmmount + 1
                        time.sleep(0.5)
                    else:
                        print("Not enough Iron")
                else:
                    print("Not enough Wood")
            #Craft Bow
            if PlayerChoice4 == "Bow":
                if materials[0].resourceamount >= 2:
                    if materials[3].resourceamount >= 1:
                        print("Forging...")
                        player.self_xp += 5
                        materials[3].resourceamount -= 1
                        materials[0].resourceamount -= 2
                        BowAmmount = BowAmmount + 1
                        time.sleep(0.5)
                    else:
                        print("Not enough String")
                else:
                    print("Not enough Wood")
            #Craft Armor           
            elif PlayerChoice4 == "Armor":
                print("Craft -Armor- for 2 Iron and 2 Leather\nCraft -Chestplate- for 1 Iron and 1 leather\nCraft -Helmet- for 1 Iron\nCraft -Boots- for 1 Leather\nCraft Armor, Chestplate, Helmet, Bronze by putting Bronze before the name.\n")
                PlayerChoiceCraftArmor = input()
                #Craft all Iron Armor Pieces + Boots
                if PlayerChoiceCraftArmor == "Armor":
                    if  materials[1, 2].resourceamount >= 2:
                        materials[1, 2].resourceamount -= 2
                        inventory[0, 1, 2].ArmorAmount += 1
                        print("Forging...")
                        player.self_xp += 20
                        time.sleep(0.5)
                    else:
                        print("Not enough resources")
                #Craft all Bronze Armor Pieces + Boots
                elif PlayerChoiceCraftArmor == "BronzeArmor":
                    if  materials[4, 2].resourceamount >= 2:
                        materials[4, 2].resourceamount -= 2
                        inventory[2, 8, 9].ArmorAmount += 1
                        print("Forging...")
                        player.self_xp += 15
                        time.sleep(0.5)
                    else:
                        print("Not enough resources")
                #Craft Chestplate
                elif PlayerChoiceCraftArmor == "Chestplate":
                    if  materials[1].resourceamount >= 1:
                        if  materials[2].resourceamount >= 1:
                            print("Forging...")
                            player.self_xp += 10
                            materials[1].resourceamount -= 1
                            materials[2].resourceamount -= 1
                            inventory[0].ArmorAmount += 1
                            time.sleep(0.5)
                        else:
                            print("Not enough Iron")
                    else:
                        print("Not enough Leather")  
                #Craft Bronze Chestplate
                elif PlayerChoiceCraftArmor == "BronzeChesplate":
                    if  materials[4].resourceamount >= 1:
                        if materials[2].resourceamount >= 1:
                            inventory[8].ArmorAmount += 1
                            print("Forging...")
                            player.self_xp += 15
                            materials[4].resourceamount -= 1
                            materials[2].resourceamount -= 1
                            time.sleep(0.5)
                        else:
                            print("Not enough Leather")
                    else:
                        print("Not enough Bronze")
                #Craft Helmet 
                elif PlayerChoiceCraftArmor == "Helmet":
                    if  materials[1].resourceamount >= 1:
                        print("Forging...")
                        player.self_xp += 5
                        materials[1].resourceamount -= 1
                        inventory[2].ArmorAmount += 1
                    else:
                        print("Not enough Iron") 
                #Craft Helmet 
                elif PlayerChoiceCraftArmor == "BronzeHelmet":
                    if  materials[4].resourceamount >= 1:
                        print("Forging...")
                        player.self_xp += 5
                        materials[4].resourceamount -= 1
                        inventory[2].ArmorAmount += 1
                    else:
                        print("Not enough Bronze") 
                #Craft Boots
                elif PlayerChoiceCraftArmor == "Boots":
                    if  materials[2].resourceamount >= 1:
                        print("Forging...")
                        player.self_xp += 5
                        materials[2].resourceamount -= 1
                        inventory[2].ArmorAmount += 1
                    else:
                        print("Not enough Leather")           
            #Craft Gem       
            elif PlayerChoice4 == "Gem":
                if  materials[1].resourceamount >= 1:
                    materials[1].resourceamount -= 1
                    inventory[3].ArmorAmount += 1
                    print("Forging...")
                    player.self_xp += 1
                    time.sleep(0.5)     
                else:
                    print("Not enough Iron")   
            #Craft Gem       
            elif PlayerChoice4 == "BronzeGem":
                if  materials[4].resourceamount >= 1:
                    materials[4].resourceamount -= 1
                    inventory[11].ArmorAmount += 1
                    print("Forging...")
                    player.self_xp += 1
                    time.sleep(0.5)     
                else:
                    print("Not enough Bronze")  
        #Quit
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