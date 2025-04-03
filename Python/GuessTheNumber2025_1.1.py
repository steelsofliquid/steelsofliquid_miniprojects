# 2025 Number-guessing game I wrote to understand my skills
# version 1.1, 1.0 was a proof-of-concept.

from random import *

yournum = 0
correctnum = randint(1, 10)
playcounter = 3

print("Guess the number 2025, version 1.1")
print("by steelsofliquid\n")

while playcounter >= 0:
    try:
        yournum = int(input("Pick a number between 1 and 10:"))
    except:
        print("Oops! Your response was invalid.")

    if yournum == correctnum:
        print("Congrats! You\'re correct. The number was ", correctnum, ".", sep='')
        break;

    elif playcounter == 0:
        print("Wrong. The number was ", correctnum, ". Better luck next time!", sep='') # during "playtesting" it was legitimately hard to get this response -_-
        break;
    else:
        print("Wrong. Try again! You have ", playcounter, " attempts remaining.", sep='')
        playcounter = (playcounter - 1)


# It works!!! ^_^ We are so back
# ... Albeit, with bugs >_<
