#Main.py
import planetGeneration
import mining
def main():
    planetGeneration.generatePlanet(3)
    mining.clearReprint(True)
    mining.selector()
main()
