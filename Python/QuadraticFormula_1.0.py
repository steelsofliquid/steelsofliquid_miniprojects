# python 3.12.2
# now for something involving a tinge of math

from time import *
from math import *

quada = float()
quadb = float()
quadc = float()

piece1 = float()
piece2 = float()
piece3 = float()
piece4 = float()
piece5 = float()
piece6 = float()

result1 = float() # positive
result2 = float() # negative

print("Quadratic Formula Solver 1.0")
print("By SteelsOfLiquid")
sleep(1)

# input zone
print("ax^2 + bx + c")
quada = float(input("a? "))
quadb = float(input("b? "))
quadc = float(input("c? "))

try:
    piece1 = quadb * -1
    
    piece2 = quadb ** 2
    piece3 = 4 * quada * quadc
    
    piece4 = piece2 - piece3
    piece5 = 2 * quada

    piece6 = sqrt(piece4)
    print(piece1, " ± ", piece6, sep='')

    result1 = ((piece1 + piece6) / piece5)
    result2 = ((piece1 - piece6) / piece5)

    print("\n\nSolution 1: ", result1, sep='')
    print("Solution 2: ", result2, sep='')

except KeyboardInterrupt:
    quit()
except:
    print("An error occurred.")
