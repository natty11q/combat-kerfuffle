import random
import item_classes

def name_iput():
    
    loop : bool = True ; loop2 : bool = False
    player_name: str = ""

    while loop:
        print(f"\ninput a name -\t", end = "")
        player_name = input("")
        print(f"\n\nthe name you have chosen is \" {player_name} \" is this correct?\n\n(y)es (n)o -\t", end = "")

        loop2 = True
        while loop2:
            response = input().strip().lower()

            if response in ["yes","y"]:
                loop2 = False
                loop = False
            elif response in ["no","n"]:
                print("\nre-enter the name\n\n")
                loop2 = False
            else:
                print(f"please input either yes or no -\t", end = "")
    
    print(f"time to begin {player_name} !\n")
    return player_name




def chose_type():

    player_type = ""
    typecheck : list = []

    chartypes = ["Sword User","Boxer","Martial Artist","Parkour Expert","Mage"]
    for i in range(len(chartypes)):
        print(f"{i+1}:\t{chartypes[i]}")
        typecheck.append(chartypes[i].lower())
    
    print(f"\nchose your characeters abilitiy -\t",end ="")

    loop = True
    loop2: bool = False

    while loop:

        player_type = input("")

        try:
            player_type = int(player_type)
            if player_type in range(1,len(chartypes)+1):
                loop2 = True
                player_type = chartypes[player_type - 1]

                print(f"you have chosen \"{player_type}\"\n\n(y)es (n)o? -\t", end = "")

        except:
            if player_type in typecheck:
                loop2 = True
                player_type = chartypes[typecheck.index(player_type)]

                print(f"you have chosen \"{player_type}\"\n\n(y)es (n)o? -\t", end = "")

        
        if not loop2:
            print(f"\nplease choose one of the options from 1 to {len(chartypes)} -\t", end = "")


        while loop2:

            confirm = input("")

            if confirm in ["yes","y"]:
                loop2 = False
                loop = False
                End = True

            elif confirm in ["no","n"]:
                print("\nre-chose your ability -\t",end="")
                loop2 = False

            else:
                print(f"please input either yes or no -\t", end = "")
    print("\n\n")

    return player_type


def chose_items():
    _items_ = item_classes._items.copy()
    player_items = []

    for i in range(8):
        b : int
        b = (len(_items_)-1)
        
        next_item = _items_[random.randint(0 , b)]
        player_items.append(next_item)
        _items_.remove(next_item)

    return player_items