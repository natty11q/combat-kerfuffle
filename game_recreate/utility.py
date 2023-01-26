import bcolours

def turn_stats(P_type):

    types = ["Sword User","Boxer","Martial Artist","Parkour Expert","Mage"]

    if P_type == types[0]:
        return {"atk" : 80,"def" : 30,"hp" : 25000, "mp" : 100 ,"ene" : 100, "spr" : ("Billion Blade Barrage",1200) ,"rge" : False}
    
    elif P_type == types[1]:
        return {"atk" : 36,"def" : 25,"hp" : 30000, "mp" : 110 ,"ene" : 78, "spr" : ("Furious Fist Fracass",900) ,"rge" : False}
    
    elif P_type == types[2]:
        return {"atk" : 75,"def" : 10,"hp" : 20000, "mp" : 200 ,"ene" : 200, "spr" : ("Kezekatami Kontrol",1000) ,"rge" : False}

    elif P_type == types[3]:
        return {"atk" : 30,"def" : 19,"hp" : 23000, "mp" : 120 , "ene" : 400, "spr" : ("Reverse Airial rush",850) , "rge" : False}

    elif P_type == types[4]:
        return {"atk" : 20,"def" : 10,"hp" : 21000, "mp" : 400 , "ene" : 100, "spr" : ("Starfall",2500) ,"rge" : False}




def easter_egg_name_check(name):
    
    if name in ["mimi","kuni","kidnapper","psycho","french lady","cao skin 2"]:
        print("time to add another one to the collection.")

        return {
            "isEasterEgg"   : True,
            "playertype"    : "French Kidnapper",
            "stats"         : {
                "atk"   : 35,
                "def"   : 20,
                "hp"    : 6000,
                "mp"    : 30,
                "ene"   : 85,
                "spr"   : ("HYPER Fat Attack", 150),
                "rge"   : False,
            },
            "victoryquotes" : ["HA goteem!", f"HA g-G-G-G-G{bcolours.WARNING}{bcolours.BOLD} GOTEEM!{bcolours.ENDC}",
            "Y so much plastic tho ???","have you ever had a dream?","Pingus."]
            }

    if name.lower() in ["banit","jamm","james","janit","goodwarj","raj","techsupport1","JANIB"]:
        print("░██████╗░██████╗░██████╗░\n██╔════╝░██╔══██╗██╔══██╗\n██║░░██╗░██████╔╝██████╔╝\n██║░░╚██╗██╔══██╗██╔══██╗\n╚██████╔╝██║░░██║██║░░██║\n░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝")
        
        return {
            "isEasterEgg" : True,
            "playertype"    : "IT tech support",
            "stats"         : {
                "atk"   : 35,
                "def"   : 40,
                "hp"    : 60000,
                "mp"    : 30,
                "ene"   : 85,
                "spr"   : ("HYPER Fat Attack", 150),
                "rge"   : False,
            },
            "victoryquotes" : []
        }
    
    if name in ["clayte","clay"]:
        return{
            "isEasterEgg" :  True,
            "playertype" :  "singer / manga artist",
            "stats" : {
                "atk" : 1.2,
                "def" : 9999,
                "hp" : 1049284,
                "mp" : "400",
                "ene" : "1",
                "spr" : "blancattack!!"
            },
            "victoryquotes" : ["winner winner chicken dinner "]
            } 
    
    if name.lower() in ["anita","misha","oreo","pingus"]:
        print("PINGUS")

        return {
        "isEasterEgg" : True,
        "playertype" : "Sorokina",
        "stats" : {
            "atk" : 60,
            "def" : 60,
            "hp" : 20000,
            "mp" : 200,
            "ene" : 300,
            "spr" : ("\"NO! You Cant pet my dogs!\"",3000),
            "rge" : False
        },

        "victoryquotes" : ["HA goteem!", f"HA g-G-G-G-G{bcolours.WARNING}{bcolours.BOLD} GOTEEM!{bcolours.ENDC}",
        "Y so much plastic tho ???","have you ever had a dream?","Pingus."]
        }


    elif name in ["Mike","Mikee","Michael","mike","mikee","michael","updog","UpDog"]:

        print("hello Michael :D")

        return {
        "isEasterEgg" : True,

        "playertype" : "Obed",

        "stats" : {
            "atk" : 80,
            "def" : 50,
            "hp" : 40000,
            "mp" : 400,
            "ene" : 350,
            "spr" : ("Mikee Mashup MO-0",7000),
            "rge" : False
        },

        "victoryquotes" : []

        }
    
    if name in ["alec","Alex","alex","Alex","ez alex","ez-alex","schiio","schizo","milky","coffee","8"]:
        print("I don't like your skin colour! Let me help with that.\n")

        return {
        "isEasterEgg" : True,
        "playertype" : "Nigo-Britallian",
        "stats" : {
            "atk" : 98,
            "def" : 80,
            "hp" : 37000,
            "mp" : 100,
            "ene" : 50,
            "spr" : ("Spawn Joe",999999),
            "rge" : False
        },

        "victoryquotes" : ["say hi to jet for me.", f"So let's see about that skin colour...",
        "Wanna see the TRUE lightskin stare?","The white flames of supremacy conquer all!!! MUAHAHAHAHAHAHAHAHA",
        "WHITE POWER!",f"i truly hate you {bcolours.BOLD}BLACKS{bcolours.ENDC}"]
        }

 
    elif name in ["natty","nathaniel","Natty","Nathaniel","natty11q","Natty11q"]:

        print("do you wanna see jesus ?")
        return {
        
        "isEasterEgg" : True,
        "playertype" : "11q",
        "stats" : {
            "atk" : 160,
            "def" : 40,
            "hp" : 50000,
            "mp" : 400,
            "ene" : 350,
            "spr" : ("Spawn Androminito",999999),
            "rge" : False
        },

        "victoryquotes" : ["im young to shatter more than just your bones.",
        "should've parried","dond slin't wake up tomorrow","my happed",
        "it isnt over yet!",f"{bcolours.FAIL}im not done with you yet{bcolours.ENDC}",
        "time to start tryin","my bad","alright! lets start fighting for REAL",
        "Cmon! you gotta be stronger than that!","im going to sell your limbs.",
        "maybe try next time?","do better","start running."]
        }

    elif name in ["isa","isaiah","isaiah1h000","03","isaia03","yoshaaa9","yosha","yata9"]:
        print("Time to commit some devious acts >)\n")
        return {
        
        "isEasterEgg" : True,
        "playertype" : "Ejiniwebi",
        "stats" : {
            "atk" : 110,
            "def" : 50,
            "hp" : 45000,
            "mp" : 400,
            "ene" : 280,
            "spr" : ("Spawn Danyo",999999),
            "rge" : False
        },
        
        "victoryquotes" : ["you should really try dodging next time",
        f"You cant beat me JUST LOOK AT MY {bcolours.OKBLUE}SPEED{bcolours.ENDC}",
        "do better next time","No tears my friend, only vicory",
        f"skidaddle skidoodle {bcolours.CRED}OR ILL KICK YOU LIKE I KICKED THAT POODLE!{bcolours.ENDC}",
        "Predicatble.","move out the way next time.","should've dodged.",
        "do better","GG.","These are the actions of your conciquences."]
        }

    elif name in ["Doe","doe","Doene","doene","Kiwi","kiwi","KIWI"]:

        print("why are you here\n")

        return{
            "isEasterEgg" : True,
            "playertype" : "cao's slave",
            "stats" : {
                "atk" : 10,
            "def" : 10,
            "hp" : 5000,
            "mp" : 50,
            "ene" : 50,
            "spr" : ("Doe noises",1),
            "rge" : False
            },            
            "victoryquotes" : ["how wtf?", "literally how", "theres no way anybody is seeing this text rn","how did anyone lose to this fatty smh"]
        }
    
    elif name in ["meow","sheyzil","ZZIILL","sheshsh","moew moew", "mow" , "meowewoewo"]:
        
        print(fr""" {bcolours.CVIOLET}
                    /\_____/\
                   /  o   o  \
                  ( ==  ^  == )
                   )         (
                  (           )
                 ( (  )   (  ) )
                (__(__)___(__)__)
              {bcolours.ENDC}
              """)
        
        return{
            "isEasterEgg" : True,
            "playertype" : "CANIBALIST!!?",
            "stats" : {
                "atk" : 20,
            "def" : 25,
            "hp" : 10000,
            "mp" : 50,
            "ene" : 100,
            "spr" : ("MEOW MEWO",1000000),
            "rge" : False
            },
            "victoryquotes" : ["MEOW", "MEOW MOEW", "MEOW MOEW MOEW","MEOW?","MEUW","MOW","BARK"]
        }
    
    else:

        return {"isEasterEgg" : False}