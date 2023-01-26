import bcolours

def amin():
    var_A   : int
    sto     : str
    validation : bool = True
    
    
    sto = input()
    
    
    while validation:
        try:
            var_a = int(sto)
        except:
            print(f"{bcolours.CRED}THAT ISNT AN INTIGER YOU DUMB WHORE")