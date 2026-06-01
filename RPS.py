import sys
import random
from enum import Enum

class RSP(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playerchoice = int(input('enter the choice\n1 for rock,\n2 for paper,\n3 for scissors\n\n'))
if playerchoice < 1 or playerchoice > 3:
    sys.exit('must enter 1,2,3')
computerchoice =int( random.choice('123'))
print("")
print("you chose " + str(RSP(playerchoice)).replace("RSP.",""))
print("computer chose " + str(RSP(computerchoice)).replace("RSP.",""))
print("")
if playerchoice == computerchoice:
    print("tie")
elif playerchoice == 1 and computerchoice == 3:
    print("celebrate! you win")
elif playerchoice == 2 and computerchoice == 1:
    print("celebrate! you win")
elif playerchoice == 3 and computerchoice == 2:
    print("celebrate! you win")
else:
    print("computer wins")