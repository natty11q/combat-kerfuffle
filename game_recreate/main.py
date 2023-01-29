import pregame
import utility
import playerclass
import random
import bcolours
import moves
import player_super_easter_egg
import playerturn

import itertools
import time

def intro():
    padding : str = ""
    title : str = "11q combat simulator!"
    for i in range(len(title)):
        padding += "="

    print(f"{padding}\n{title}\n{padding}\n\n")

def setup():
    
    
    
    quotes = {
        "Sword User" : ["it seems my blade had more edge than than you","ill parry whatever you throw at me","it ends how it ends",
        "its over","you fought well my friend"],

        "Boxer" : ["GET OUTTA THE RING!","my fists tell no lies, im just better than you!","work on hmm... EVERYTHING, youre just BAD",
        "maybe i should add padding to my gloves"],

        "Martial Artist" : ["you didnt even scuff my gi.","you did well warrior","yor movements are too hasty","you need to stay calm",
        "that was closer than i thought"],

        "Parkour Expert" : ["well, that was cool i guess","im gonna go back to jumping across the roofes of buildings",
        "BACKFLIP!","FRONTFLIP!","brb im gonna go climb the outside of the burj","boutta climb eiffel again"],

        "Mage" : ["abra cadabra or something idk","kinda easy ngl","its actually leviosahhh not leviosaaah","yippee? *disapeares*",
        "*teleports behind you* nothing personél kid."]
    }

    name = pregame.name_iput();
    egg_check = utility.easter_egg_name_check(name)

    if not egg_check["isEasterEgg"]:

        player_type  = str(pregame.chose_type());
        player_stats = utility.turn_stats(player_type);
        victory_quotes = quotes[player_type]
    
    else:

        player_type = egg_check["playertype"]
        player_stats = egg_check["stats"]
        victory_quotes = egg_check["victoryquotes"]
    
    return[name,player_type,player_stats,victory_quotes]

def setup_npc():

    quotes = {
        "Sword User" : ["it seems my blade had more edge than than you","ill parry whatever you throw at me","it ends how it ends",
        "its over","you fought well my friend"],

        "Boxer" : ["GET OUTTA THE RING!","my fists tell no lies, im just better than you!","work on hmm... EVERYTHING, youre just BAD",
        "maybe i should add padding to my gloves"],

        "Martial Artist" : ["you didnt even scuff my gi.","you did well warrior","yor movements are too hasty","you need to stay calm",
        "that was closer than i thought"],

        "Parkour Expert" : ["well, that was cool i guess","im gonna go back to jumping across the roofes of buildings",
        "BACKFLIP!","FRONTFLIP!","brb im gonna go climb the outside of the burj","boutta climb eiffel again"],

        "Mage" : ["abra cadabra or something idk","kinda easy ngl","its actually leviosahhh not leviosaaah","yippee? *disapeares*",
        "*teleports behind you* nothing personél kid."]
    }

    chartypes = ["Sword User","Boxer","Martial Artist","Parkour Expert","Mage"]
    npc_type : str = chartypes[random.randint(0 , (len(chartypes) - 1))]
    npc_stats = utility.turn_stats(npc_type)
    npc_quotes = quotes[npc_type].append("bro really got beaten by an npc, LMAO")
    return npc_type , npc_stats , npc_quotes

def clearlines():
    space = " " * 100
    print(f"\033[A{space}\033[A", end="\r")    
        
def create_players():
    
    return_list = []

    print("""select your gamemode!!
    
    (1) player vs cpu
    (2) player vs player
    (3) cpu vs cpu\n
    """)
    
    clearNum = 1
    gamemode = 0

    n = 0
    midvalid = True
    while midvalid:
        
        
        print("- ", end="")
        gamemode = input()

        if gamemode == "1":

            player_input1 = setup()
            player_1 = playerclass.Player(player_input1[0],player_input1[1],player_input1[2],player_input1[3])
            
            npctype , npcstats , npcquotes = setup_npc()
            player_2 = playerclass.Player("npc" , npctype , npcstats , npcquotes)

            
            return_list.append(player_1)
            return_list.append(player_2)
            midvalid = 0

        elif gamemode == "2":

            player_input1 = setup()
            player_1 = playerclass.Player(player_input1[0],player_input1[1],player_input1[2],player_input1[3])

            player_input2 = setup()
            player_2 = playerclass.Player(player_input2[0],player_input2[1],player_input2[2],player_input2[3])

            return_list.append(player_1)
            return_list.append(player_2)
            midvalid = 0
        
        elif gamemode == "3":

            npctype , npcstats , npcquotes = setup_npc()
            player_1 = playerclass.Player("npc1" , npctype , npcstats , npcquotes)

            npctype , npcstats , npcquotes = setup_npc()
            player_2 = playerclass.Player("npc2" , npctype , npcstats , npcquotes)

            
            return_list.append(player_1)
            return_list.append(player_2)
            midvalid = 0

        else:
            
            if n < 1:
                clearlines()
                print(f"\n{bcolours.CRED}please input enither {bcolours.WARNING}1 , 2 or 3{bcolours.CRED}, depending on what gamode you would like{bcolours.ENDC}\n\nplease select your gamemode\n", end = "\r")
                
            else:
                clearlines()
                print(n)
                clearlines()
                clearlines()
                print(f"\n{bcolours.CRED}please input enither {bcolours.WARNING}1 , 2 or 3{bcolours.CRED}, depending on what gamode you would like{bcolours.ENDC}\n\nplease select your gamemode\n", end = "\r")
                
            n += 1
            
    gamemode = int(gamemode)

    return return_list , gamemode


def main():
    intro()
    
    P_1 :   playerclass.Player
    P_2 :   playerclass.Player

    playerlist , gamemode = create_players()
    
    P_1 , P_2 = playerlist[0] , playerlist[1]

    P_1.allocate_stats()
    P_2.allocate_stats()
    
    for p in [P_1,P_2]:
        itemz = pregame.chose_items()
        
        for i in range(len(itemz)):
            p.assignItem(itemz[i])
        
        print(p.name, "assigned")

    P_1.print_stats() 
    P_2.print_stats()

    
    turn : int = 1

    game_on_print : str = "Game Start"
    padding : str = "=" * len(game_on_print)
    print(f"\n\n{padding} {game_on_print} {padding}\n\n")



# ---------------------------------------- Main Game Loop ----------------------------------------- #

    main_game_loop : bool = True
    while main_game_loop:
        
        print(f"\n{bcolours.BOLD}* Turn {turn} *{bcolours.ENDC}\n")
        
        movesave = {
        
        }

        damage = 0
        
        # --------------------------- platerturns -------------------------- #
        
        for _player_ in [P_1,P_2]:
            
            move_choice = True
            
            while move_choice:
                
                available_inputs = ["1","2","3"]
                
                if _player_.rage:
                    print(f"{bcolours.CRED}")
                else:
                    print(bcolours.ENDC)
                
                print(f"{_player_.name} ({_player_.type})",end = "")
                
                if _player_.rage:
                    print(" ❂",end = "")
                    
                _player_.displayHealth()
                
                print("\n")
                
                _player_.print_energy()
                
                if _player_.rage:
                    print(f"{bcolours.CRED} :\n\n")
                else:
                    print(f"{bcolours.ENDC} :\n\n")
                
                
                if _player_.name in ["natty","natty11q"]:
                    if turn == 3:
                        _player_.aqquire_rage()
                
                    _player_.fillMeter(random.randint(1,100))
                
                print("[(1) Basic Attcks ]" , end= "\t")
                print("[(2) Super Attacks]" , end= "\n")
                print("[(3) Magic Skils  ]" , end= "\t")
                print("[(4) Items        ]" , end= "\n\n")
                
                
                
                if _player_.meter < 100:
                    
                    print(f"{bcolours.CBLACK}           [(5) ULTRA!       ]{bcolours.ENDC}")
                else:

                    m = 0
                    for i in itertools.cycle(bcolours.RAINBOW): 
                        print(f"           {i}[(5) ULTRA!       ]{bcolours.ENDC}",end = "\r")
                        m += 1

                        if m == 15:
                            break
                        time.sleep(0.05)
                        
                    available_inputs.append("5")
                    
                    print(f"           {bcolours.CYELLOW}[(5) ULTRA!       ]{bcolours.ENDC}")
                
                if len(_player_.items.keys()) > 0:
                    available_inputs.append("4")
                
                movechoose = input("\n- ")
                movechoose.strip()
                
                if movechoose not in ["1","2","3","4","5"]:
                    print("\ninput must be a number inicating wich of the options you would like to use")
                
                else:
                    
                    if movechoose in available_inputs:
                        
                        if movechoose == "1":
                            
                            [damage , lastmove] = moves.basic_attacks(_player_)
                            
                            if lastmove == "back":
                                pass
                            else:
                                movesave[_player_] = damage
                                move_choice = False

        for player_dmg in [P_1,P_2]:
            player_dmg.take_damage(damage)
                             
                
           
            
            
            
            print("\n\n")
         
            
                
            
            
            
                
            
            

        
        
        turn += 1

        # game goes here$
        # 2 turns then calc healths
        # do the meter 
        # check rage
        # use def stats
        # enable / disable supers
        # item class

    return

if __name__ == "__main__":
    main()