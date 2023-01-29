import playerclass

_items = ["Bandages","Plaster","Medicine","pillow","Adrenaline Shot","Riot Shield"
             ,"Lazer Pointer","C4","C4 Remote","Grenade","Gas mask","Posion Gas"]


class Item:
    def __init__(self,name,itemType,description,cost):
        padding = "*" * 2 * len(name)
        print(f"\n{padding}\n{name}[\ntype: {itemType}\ndesc: {description}\nturns: {cost}\n]\n{padding}\n")


class Healer(Item):
    def _init_(self,name,description,cost,excludedchars ,amount):
        self.name = name
        self.desc = description
        self.cost = cost
        self.exclu = excludedchars
        self.heal = amount
        self.type = "Healing"
    
    def printr(self):
        super().__init__(self.name,"Healing",self.desc,self.cost)
        
    def function(self):
        return self.heal


class Booster(Item):
    
    def _init_(self,name,description,cost,amount,stat,turns,excludedchars):
        self.name = name
        self.desc = description
        self.cost = cost
        self.exclu = excludedchars
        self.amount = amount
        self.stat = stat
        self.turns = turns
        self.type = "Booster"
        
    def printr(self):
        super().__init__(self.name,"Booster",self.desc,self.cost)
    
    def function(self):
        return self.stat, self.amount, self.turns

    #return the stat that needs to be changed, the amount it needs to be changed by, and the number of turns
    
class damager(Item):
    def __init__(self, name, description, cost, damage , selfdamage : bool):
        self.name = name
        self.desc = description
        self.cost = cost
        self.dmg = damage
        self.selfdmg = selfdamage 
        self.type = "Damager"
        
    def printr(self):
        super().__init__(self.name ,"Damager",self.desc ,self.cost)
        
    def function(self):
        if self.selfdmg:
            return self.dmg , (self.dmg * 0.8)
        else:
            return self.dmg
        
