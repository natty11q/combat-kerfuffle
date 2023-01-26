import playerclass
import bcolours
import items


def playermove(player : playerclass.Player):
    
    valid_moves = ["1","2","3"]
    
    if player.meter == 100:
        valid_moves.append("5")
        
    if len(player.items) > 0:
        valid_moves.append("4")
    
    
    move_on : bool = True
    while move_on:
        pass