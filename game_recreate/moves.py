import random
import playerclass
import items
import bcolours

def basic_attacks(player : playerclass.Player) -> list:
    
    validating = True
    while validating:
        
        print(f"{bcolours.ENDC}== pick your attack =={bcolours.ENDC}\n")
        print("[1] weak attack (2 energy)\n[2] medium attack (4 energy)\n[3] strong attack (8 energy)\n\n(4)back")
        
        validating2 = True
        while validating2:
            
            move = input("\n- ")
            
            if move not in ["1","2","3","4"]:
                print("\ninvalid input")
                
            else:
                if move == "1":
                    player.loseEnergy(2)
                    validating2 = 0
                    return [(1 * player.attack), "weak basic attack"]
                    
                elif move == "2":
                    player.loseEnergy(4)
                    validating2 = 0
                    return [(2.5 * player.attack) , "medium basic attack"]
                
                elif move == "3":
                    player.loseEnergy(8)
                    validating2 = 0
                    return [(6 * player.attack) , "heavy basic attack"]
                
                elif move == "4":
                    return [0 , "back"]
                
    return [0,"error occured"]
                    
def super_attack(player : playerclass.Player, playerSupers) -> int:
    
    super_name = player.super[0]
    super_dmg  = player.super[1]
    
    print(f"\n{player.name} used their super [{super_name}]\n")
    
    return super_dmg


def itemchoose(player : playerclass.Player):
    
    num : int = 1
    
    for i_tem in player.items:
        print(f"[({num}){i_tem}]")