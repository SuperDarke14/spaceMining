#planetGeneration.py
import random
from os import get_terminal_size
import time
from math import pi as pi

global planet #unfortunately this has to be global
planet = None 

columns = get_terminal_size().columns
materials = ["o", "#", "$", "%"]
random.seed(time.time()) #set a seed for variability

def generatePlanet(size):
    global planet

    buffer = []
    planet = []

    for i in range(0, size):
        matPick = random.randint(0, len(materials)-1)
        buffer.append(materials[matPick])
    #picks a random material then adds to a buffer
    
    counter = 1
    flag = False #this flag makes the counter keep going down
    #If there is no flag, with the logic implemented, counter would go from 4 to 5 to 4 to 5 etc

    for i in range(0, size*2):
        planet.append(("".join(buffer))*counter) #this will get proportionally bigger
        buffer = [] #reset and then re-randomize the buffer
        if counter <= size and flag == False: # this logic makes it circular
            counter += 1
        else:
            counter -= 1
            flag = True

        for i in range(0, size):
            matPick = random.randint(0, len(materials)-1)
            buffer.append(materials[matPick])
 
    planet = [each.center(columns, " ") for each in planet]
    planet = "\n".join(planet) #change it from list to an all-in-one object

def printPlanet():
    print(planet)
    #prints the planet
def planetReturn():
    return planet