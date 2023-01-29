import random
import playerclass
import bcolours
import time
import itertools

def player_validate_input_main(_player_ : playerclass.Player,turn : int) -> str:
    
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

    print("[(1) Basic Moves  ]" , end= "\t")
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

    movechoose : str = ""
    choosing = True
    while choosing:

        movechoose = input("\n- ")
        movechoose.strip()

        if movechoose not in available_inputs:
            if movechoose == "4":
                print("you don't have any items on you")
            else:
                print("you arent ready to use that yet")

    return movechoose