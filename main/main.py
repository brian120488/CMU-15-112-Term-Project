from cmu_112_graphics import *
from Player import Player

def runTerraria():
    width, height = 1920, 1080
    runApp(width=width, height=height)

def main():
    print(Player())
    runTerraria()

if __name__ == "__main__":
    main()