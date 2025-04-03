from time import *

timerinterval = 1

print("Demo Timer 1.0")
print("by steelsofliquid")

sleep(1)

try:
    timerinterval = int(input("How long should the timer be? (Input in seconds): "))
except KeyboardInterrupt:
    quit; # unsure if i ever learned this but a simple google search, mentally calling ai a dunce and first result gives my brain an idea
except ValueError:
    print("Value Error")
    quit;
except:
    print("Unhandled Exception") # what else could it be?
    quit;
    # The problem with this is that I don't know how to make it return to the try part >_<

for i in range(0, timerinterval): # had a brain fart here with range
    print(timerinterval - i)
    sleep(1)

print("Time\'s up!")
# I wish I could make it play a sound here but I don't have the expertise (never was taught to do it)
