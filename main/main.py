from cmu_112_graphics import *
from Player import Player
from Block import Block

def runTerraria():
    width, height = 1280, 720
    runApp(width=width, height=height)

def appStarted(app):
    app.timerDelay = 1
    app.rows = int(app.height / Block.height)
    app.cols = int(app.width / Block.width)

    app.player = Player(app)
    app.scrollX = 0
    app.terrain = [[None] * app.cols for _ in range(app.rows)]

    for col in range(len(app.terrain[0])):
        app.terrain[20][col] = Block(app, 20, col, "grass_block")

def keyPressed(app, event):
    if event.key == "a":
        app.player.move(-1)
    elif event.key == "d":
        app.player.move(1)

def mousePressed(app, event):
    pass

def redrawAll(app, canvas):
    app.player.draw(app, canvas)
    for i in range(0, app.width, 16):
        canvas.create_line(i, 0, i, app.height)
    for i in range(0, app.height, 20):
        canvas.create_line(0, i, app.width, i)
    for row in range(len(app.terrain)):
        for col in range(len(app.terrain[0])):
            block = app.terrain[row][col]
            if block != None:
                block.draw(app, canvas)


def main():
    runTerraria()

if __name__ == "__main__":
    main()