# # _dict = {"a" : 1, "b" : 2}

# # for x,y in _dict.items():
# #     print(f"{x} : {y}")

import bcolours
import time
# from itertools import cycle

# print(f"{bcolours.FLASHING}WOAH")

# RAINBOW = ['\033[41m','\033[43m','\33[103m','\033[42m','\33[104m','\33[105m','\033[45m','\033[46m']

# # i : int = 0
# # while 1:
# #     i += 1
    
# #     dots = "." * i
# #     print(dots,flush = True, end = "\r")
    
# #     if i == 4:
# #         i = 0
# #         print("    ", end = "\r")
    
# #     time.sleep(1)
# print("all",end="\t")
# print("of")
# print("this",end="")

# c : int = 0
# for i in cycle([1,2]):
    
#     if i == 1:
#         if c < (len(RAINBOW)-1):
#             c += 1
#         else:
#             c = 0

#         print(f"\t{RAINBOW[c]}POWER!!{bcolours.ENDC}",flush=True, end= "\r")
#         time.sleep(0.025)

#     else:
#         print("\t                         ",end="\r")
#         time.sleep(0.010)


"""

for i in range (100):
    if i%2 == 0:
        print(f"{bcolours.CGREENBG2}POWER {bcolours.ENDC}",end="\r")
    else:
        print(f"{bcolours.CREDBG}POWER {bcolours.ENDC}",end="\r")
        
    time.sleep(0.05)
print(f"{bcolours.CGREENBG2}POWER{bcolours.ENDC}")

"""


"""

import keyboard 

global abc
abc = True

def run_func():
  
  global abc
  print('Hi, welcome!')
  print('If you want to do this, press A or press B for doing that.')
  
  while abc:
    if keyboard.is_pressed('a'):
      print('This function is run!')
      abc = True

    elif keyboard.is_pressed('b'):
      print('That function is run!')
      abc = True

print('To start press S')

while abc:
  if keyboard.is_pressed('S'): 
    run_func()
  abc = True
  
"""

"""

import pygame
import bcolours
import sys

pygame.init()


keys = pygame.key.get_pressed()
clock = pygame.time.Clock()
input_string = ""
m =0
gameloop = True
while gameloop:
    
    
	if m == (len(bcolours.RAINBOW)-1):
		m = 0
	else:
		m += 1
	
	print(f"          {bcolours.RAINBOW[m]}[(5) ULTRA!       ]{bcolours.ENDC}  -",end = "\r")
 
	if pygame.key.get_pressed():

		if keys[pygame.K_a]:
			
			input_string += "a"

		if keys[pygame.K_b]:

			input_string += "b"

		if keys[pygame.K_c]:

			input_string += "c"

		if keys[pygame.K_d]:

			input_string += "d"

		if keys[pygame.K_e]:

			input_string += "e"

		if keys[pygame.K_f]:

			input_string += "f"

		if keys[pygame.K_g]:

			input_string += "g"

		if keys[pygame.K_h]:

			input_string += "h"

		if keys[pygame.K_i]:

			input_string += "i"

		if keys[pygame.K_j]:

			input_string += "j"

		if keys[pygame.K_k]:

			input_string += "k"

		if keys[pygame.K_l]:

			input_string += "l"

		if keys[pygame.K_m]:

			input_string += "m"

		if keys[pygame.K_n]:

			input_string += "n"

		if keys[pygame.K_o]:

			input_string += "o"

		if keys[pygame.K_p]:

			input_string += "p"

		if keys[pygame.K_q]:

			input_string += "q"

		if keys[pygame.K_r]:

			input_string += "r"

		if keys[pygame.K_s]:

			input_string += "s"

		if keys[pygame.K_t]:

			input_string += "t"

		if keys[pygame.K_u]:

			input_string += "u"

		if keys[pygame.K_v]:

			input_string += "v"

		if keys[pygame.K_w]:

			input_string += "w"

		if keys[pygame.K_x]:

			input_string += "x"

		if keys[pygame.K_y]:

			input_string += "y"

		if keys[pygame.K_z]:

			input_string += "z"
       
		if keys[pygame.K_SPACE]:
			
			gameloop = 0
			print(f"you input : \"{input_string}\"")
			pygame.quit
			sys.exit()
   
   
	

	
	clock.tick(60)
   
"""

dict = {"a" : 1,
        "b" : 2,
        "c" : 3}

print(dict.values())
print(dict.keys())