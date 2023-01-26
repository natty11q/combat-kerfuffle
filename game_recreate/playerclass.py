import random
import bcolours
import time
import items

class Player:

    def __init__(self, name : str, p_type, stats, victory_quotes):
        
        self.name = name
        self.type = p_type
        self.stats = stats
        self.health_max = self.stats["hp"]
        self.magic_max = self.stats["mp"]
        self.meter = 0
        self.victoryquotes = victory_quotes

        self.items : dict = {}
        self.raged : bool = False

    def allocate_stats(self):

        self.attack = self.stats["atk"]
        self.defence = self.stats["def"]
        self.health = self.stats["hp"]
        self.magic = self.stats["mp"]
        self.energy = self.stats["ene"]
        self.super = self.stats["spr"]
        self.rage = self.stats["rge"]
        


    def print_stats(self):

        print(f"{self.name} ({self.type})'s stats :\n")

        healthprint = self.health // 5000
        Hbar = "■" * healthprint
        space = " " * (10 - healthprint)

        if healthprint >= 8.5 and healthprint <= 10:
            print(f"health :\t\t[{bcolours.OKGREEN}{Hbar}{space}{bcolours.ENDC}]    {self.health}")
        elif healthprint < 1.5 :
            print(f"health :\t\t[{bcolours.FAIL}{Hbar}{space}{bcolours.ENDC}]    {self.health}")

        elif healthprint >= 10 and healthprint <= 10:
            ex = "■" * (healthprint - 10)
            t = "■" * (10 - len(ex))
            print(f"health :\t\t[{bcolours.CYELLOW2}{ex}{bcolours.OKGREEN}{t}{bcolours.ENDC}]    {self.health}")

        else:
            print(f"health :\t\t[{Hbar}{space}]    {self.health}")

        time.sleep(0.25)

        attkprint = self.attack // 10
        Abar = "■" * attkprint
        space = " " * (10 - attkprint)

        if attkprint >= 8.5 and attkprint <= 10:
            print(f"attack power :\t\t[{bcolours.OKGREEN}{Abar}{space}{bcolours.ENDC}]    {self.attack}")

        elif attkprint <= 1.5:
            print(f"attack power :\t\t[{bcolours.FAIL}{Abar}{space}{bcolours.ENDC}]    {self.attack}")

        elif attkprint > 10:
            ex = "■" * (attkprint - 10)
            t = "■" * (10 - len(ex))
            print(f"attack power :\t\t[{bcolours.CYELLOW2}{ex}{bcolours.OKGREEN}{t}{bcolours.ENDC}]    {self.attack}")

        else:
            print(f"attack power :\t\t[{Abar}{space}]    {self.attack}")

        time.sleep(0.25)

        defprint = self.defence // 5
        Dbar = "■" * defprint
        space = " " * (10 - defprint)

        if defprint >= 8.5 and defprint <= 10:
            print(f"defence :\t\t[{bcolours.OKGREEN}{Dbar}{space}{bcolours.ENDC}]    {self.defence}")
        elif defprint <= 1.5:
            print(f"defence :\t\t[{bcolours.FAIL}{Dbar}{space}{bcolours.ENDC}]    {self.defence}")

        elif defprint > 10:
            ex = "■" * (defprint - 10)
            t = "■" * (10 - len(ex))
            print(f"defence :\t\t[{bcolours.CYELLOW2}{ex}{bcolours.OKGREEN}{t}{bcolours.ENDC}]    {self.defence}")

        else:
            print(f"defence :\t\t[{Dbar}{space}]    {self.defence}")

        time.sleep(0.25)

        magprint = self.magic // 40
        Mbar = "■" * magprint
        space = " " * (10 - magprint)

        if magprint >= 8.5 and magprint <= 10:
            print(f"magic capacity :\t[{bcolours.OKGREEN}{Mbar}{space}{bcolours.ENDC}]    {self.magic}")
        elif magprint < 1.5:
            print(f"magic capacity :\t[{bcolours.FAIL}{Mbar}{space}{bcolours.ENDC}]    {self.magic}")

        elif magprint >= 10:
            ex = "■" * (magprint - 10)
            t = "■" * (10 - len(ex))
            print(f"magic capacity :\t\t[{bcolours.CYELLOW2}{ex}{bcolours.OKGREEN}{t}{bcolours.ENDC}]    {self.magic}")

        else:
            print(f"magic capacity :\t[{Mbar}{space}]    {self.magic}")

        time.sleep(0.25)

        eneprint = self.energy // 40
        Ebar = "■" * eneprint
        space = " " * (10 - eneprint)

        if eneprint >= 8.5 and eneprint <= 10:
            print(f"stamina :\t\t[{bcolours.OKGREEN}{Ebar}{space}{bcolours.ENDC}]    {eneprint}")
        elif eneprint <= 1.5:
            print(f"stamina :\t\t[{bcolours.FAIL}{Ebar}{space}{bcolours.ENDC}]    {eneprint}")

        elif eneprint > 10:
            ex = "■" * (eneprint - 10)
            t = "■" * (10 - len(ex))
            print(f"stamina :\t\t[{bcolours.CYELLOW2}{ex}{bcolours.OKGREEN}{t}{bcolours.ENDC}]    {eneprint}")
        else:
            print(f"stamina :\t\t[{Ebar}{space}]    {eneprint}")

        print("\n\n")
        time.sleep(1)


    def displayHealth(self):
        
        if self.rage:
            healthprint = int(self.health // (self.health_max // 10))
            Hbar = "■" * healthprint
            space = " " * (10 - healthprint)

            if healthprint >= 8.5 and healthprint <= 10:
                print(f"  {bcolours.CRED}[{bcolours.OKGREEN}{Hbar}{space}{bcolours.CRED}] {self.health} / {self.health_max}" ,end="")
            elif healthprint < 1.5:
                print(f"  {bcolours.CRED}[{bcolours.FAIL}{Hbar}{space}{bcolours.CRED}] {self.health} / {self.health_max}" ,end="")

            elif healthprint >= 10:
                ex = "■" * (healthprint - 10)
                t = "■" * (10 - len(ex))
                print(f"  {bcolours.CRED}[{bcolours.CYELLOW2}{ex}{bcolours.OKGREEN}{t}{bcolours.CRED}] {self.health} / {self.health_max}",end="")

            else:
                print(f"  {bcolours.CRED}[{Hbar}{space}] {self.health} / {self.health_max}",end="")
                
        else:
            

            healthprint = int(self.health // (self.health_max // 10))
            Hbar = "■" * healthprint
            space = " " * (10 - healthprint)

            if healthprint >= 8.5 and healthprint <= 10:
                print(f"  [{bcolours.OKGREEN}{Hbar}{space}{bcolours.ENDC}] {self.health} / {self.health_max}" ,end="")
            elif healthprint < 1.5:
                print(f"  [{bcolours.FAIL}{Hbar}{space}{bcolours.ENDC}] {self.health} / {self.health_max}" ,end="")

            elif healthprint >= 10:
                ex = "■" * (healthprint - 10)
                t = "■" * (10 - len(ex))
                print(f"  [{bcolours.CYELLOW2}{ex}{bcolours.OKGREEN}{t}{bcolours.ENDC}] {self.health} / {self.health_max}",end="")

            else:
                print(f"  [{Hbar}{space}] {self.health} / {self.health_max}",end="")


        print(bcolours.ENDC,end = "")
        
    def assignItem(self,newitem):
        self.items[newitem] = newitem

    def print_energy(self):
        
        if self.energy > 25:
            print(f"ene : [{self.energy}]",end="")
        else:
            print(f"{bcolours.CRED}ene : [{self.energy}] (Tired)",end="")

    def useitem(self,item_used):
        
        if self.items[item_used].type == "Healing":
            
            self.heal(self.items[item_used].function())
            self.items.pop(item_used)
            
        elif self.items[item_used].type == "Damager":
            
            self.items.pop(item_used)
            return self.items[item_used].function()
        
        elif self.items[item_used].type == "Booster":
            
            self.items.pop(item_used)
            return self.items[item_used].function()

    def changeAttack(self,attk):

        self.attack = attk

    def fillMeter(self,amount):

        if (self.meter + amount) <= 100:
            self.meter += amount

        elif (self.meter + amount) > 100:
            self.meter = 100

        elif self.meter < 0:
            self.meter = 0

    def resetMeter(self):
        self.meter = 0

    def loseEnergy(self,amount):
        if self.energy - amount < 0:
            self.energy = 0
        else:
            self.energy -= amount

    def change_defence(self,defence):
        self.defence = defence

    def change_health(self,hp):
        self.health = hp

    def change_mp(self,cost):
        self.magic += cost

    def take_damage(self,damage):
        try:
            self.health -= (damage / self.defence)
        except:
            pass
    
    def heal(self,heal):
        
        if (self.health + heal) > self.health_max:
            self.health = self.health_max
        else:
            self.health += heal

    def boost_health(self,boost):

        self.health_max += boost
        self.health += (boost/2)
    
    def aqquire_rage(self):
        self.rage = True

    def naturalRage(self):
        if (self.health / self.health_max) < 0.15:
            self.rage = True

    def check_rage(self):
        
        if not self.raged and self.rage == True:

            self.attack *= 1.8
            self.defence *= 0.5
            self.energy *= 1.5
            self.meter += 50

            self.raged = True

    def victory_quote(self):
        pos = random.randint(0,len(self.victoryquotes))
        return self.victoryquotes[pos]