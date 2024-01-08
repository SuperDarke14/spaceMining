"""
Building.py
Where we modify buildings
and the build command
"""
import mining
global loadedPlanet
global selectorIndex
global buildingList


class Building:
    def __init__(self, icon, function) -> None:
        self.icon = icon
        self.funciton = function
    class autoDrill:
        def __init__(self):
            self.icon = "V"
        def autoMine():
            pass
    class factory:
        def __init__(self):
            self.icon = "F"
        def produce():
            pass
    class market:
        def __init__(self):
            self.icon = "($)(M)($)"
        def sell():
            pass

def build():
    buildInput = input("Input index (starting from 0) of building to build")
    #select the building from the permitted list
    #put the selection into loadedPlanet
    try:
        mining.loadedPlanet.insert(mining.selectorIndex, mining.buildingList[int(buildInput)])
    except:
        print("Invalid input error, probably") #error handling like a pro
    buildInput = None
    #clear variable for maemory safety

# def buildMenu():
#     global loadedPlanet
#     loadedPlanet.append(f"Select building to build: {buildingList}")
#     loadedPlanet.remove(f"Select building to build: {buildingList}")

#defunct function