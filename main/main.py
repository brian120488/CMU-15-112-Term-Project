from cmu_112_graphics import *
from Player import Player

def runTerraria():
    width, height = 1280, 720
    runApp(width=width, height=height)

def appStarted(app):
    app.player = Player(app)
    app.terrain = [[1]*app.width]

def keyPressed(app, event):
    if event.key == "a":
        app.player.move(-1)
    elif event.key == "d":
        app.player.move(1)

def mousePressed(app, event):
    pass

def redrawAll(app, canvas):
    app.player.draw(app, canvas)

def main():
    runTerraria()

if __name__ == "__main__":
    main()