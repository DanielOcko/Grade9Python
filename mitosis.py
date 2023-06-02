import sys
import time
import random

def growth():
    numCells = 1
    i = 11
    while numCells < 8192:
        numCells = numCells * 2
        print(f'the number of cells in our system is {numCells}')
        sys.stdout.write('\033[F')
        sys.stdout.write('\033[K')
        time.sleep(0.15)
    while numCells >= 8192 and numCells < 80000:
        numCells = (numCells - (((2**i)/2)-random.randint(-3500, 100))) * 2
        i = i + 1
        print(f'the number of cells in our system is {numCells}')
        sys.stdout.write('\033[F')
        sys.stdout.write('\033[K')
        time.sleep(0.5)
    if numCells > 80000:
        print('The simulation has reached the threshold for safe cell replication')
        time.sleep(3)

growth()

#2048 - ((2^11)/2) - 1 = 1025
#2050 - ((2^12)/2) - 1 =

"""
    So the easy parts of the project were just setting up the scaffolding to
hold the equation. The while loops, the if functions, the print statements, and
so on. The hard part, that I never really figured out was the right equation to
maintain an effecient cell equilibrium that was higher than 2048 cells. The
equation would probably have calculus involved, but part of modelling is simpli-
fying an equation as much as possible, so what do I know. In summation, what I
learned is that life is in a constant balancing act, on a unicycle, on a tight
rope, and the ground is on fire (when it comes to mitosis).
"""
