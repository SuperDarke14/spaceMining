"""
Mining.py
This section handles:

Selecting a resource that is on the planet in a user-visual manner (DONE)
'Mining' That resource and removing it from the planet
Re-displaying the planet
"""
global selectorIndex
global indicesOfNewline
global loadedPlanet
global resourceMeter
global columns
global buildingList
buildingList = ["($)(M)($)", "V", "F"]
import os
import planetGeneration
import building
from pynput import keyboard


resourceMeter = {material: 0 for material in planetGeneration.materials}
columns = os.get_terminal_size().columns
loadedPlanet = None
indicesOfNewline = []
selectorIndex = 0

def on_press(key):  
    global selectorIndex
    #this if chain deals with key input
    if key == keyboard.Key.right:
        try:
            if selectorIndex >= len(loadedPlanet)-1:
                selectorIndex = len(loadedPlanet)-1 #can't select the last one, I guess \:
            else: 
                selectorIndex += 1
        except:
            selectorIndex = selectorIndex
    elif key == keyboard.Key.left:
        try:
            if selectorIndex <= 0:
                selectorIndex = 0
            else:
                selectorIndex -= 1
        except:
            selectorIndex = selectorIndex
    elif key == keyboard.Key.down:
        try:
            selectorIndex = loadedPlanet.index("\n", selectorIndex)
            selectorIndex += 1
            
        except:
            selectorIndex = selectorIndex
    elif key == keyboard.Key.up: #this doesn't actually work, but whatever 
        try:
            selectorIndex = loadedPlanet[::-1].index("\n", selectorIndex)
        except:
            selectorIndex = selectorIndex
    elif key == keyboard.KeyCode.from_char("m"):
        mine()
    elif key == keyboard.KeyCode.from_char("b"):
        building.build()
    elif key == keyboard.KeyCode.from_char("x"):
        quit("User ran quit command")

    clearReprint(False)

def clearReprint(flagger):
    global columns
    os.system('cls' if os.name == "NT" else "clear")

    if flagger == True:
        print(loadedPlanet) if loadedPlanet != None else planetGeneration.printPlanet() #handles if planet hasn't been loaded yet
    else:
        formattedPlanet = "".join(loadedPlanet[:selectorIndex -1 ])+"\033[1m"+(loadedPlanet[selectorIndex])+"\033[0m"+ "".join(loadedPlanet[selectorIndex+1:])
        #I FINALLY DID IT- this print each method seems to work
        for each in formattedPlanet.splitlines():
            print(each.center(columns))
        print("\n \n \n" + f"Resources: {resourceMeter}")
        print(f"Select building to build: {buildingList}")
    #I did this travesty so that I can reference the planet without dealing with the original planet

def selector():

    global loadedPlanet
    loadedPlanet = planetGeneration.planetReturn() #this goofy line gets the planet from planetGeneration.py
    loadedPlanet = [char for char in loadedPlanet if char != " " ] #makes it editable e.g list format #list(loadedplanet
        
    with keyboard.Listener(
            on_press=on_press,
            on_release=None) as listener:
        listener.join()

def loadNewlineIndices():
    for each in loadedPlanet:
        if each == "\n":
            indicesOfNewline.append(loadedPlanet.index(each))

def mine():
    global selectorIndex
    global loadedPlanet
    global resourceMeter

    temp = loadedPlanet[selectorIndex]
    temp2 = resourceMeter.get(temp)
    #temp reads the resource from the planet
    #temp2  uses temp to get the number of resource TEMP

    if temp2 != None:
        resourceMeter.update({temp : temp2+1}) 
        #should add one to Temp2 value
    

    loadedPlanet.pop(selectorIndex) #this deletes the selected mineral from the planet
