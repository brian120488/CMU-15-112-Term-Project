from cmu_112_graphics import *
from Player import Player
from Block import Block
from Perlin import Perlin

def runTerraria():
    width, height = 1280, 720
    runApp(width=width, height=height)


# TODO:
# make keyreleased work
# set random button to make a parabola jump?
# add citations
# proposal.txt
# how to procedurally generate
# update how blocks are generated and the blocks under it
# wall and ceiling collision

def appStarted(app):
    app._root.resizable(False, False)
    app.timerDelay = 10
    app.rows = int(app.height / Block.height)
    app.cols = int(app.width / Block.width)

    app.player = Player(app)
    app.scrollX = 0
    app.scrollY = 0
    app.scrollDY = 0
    app.gravity = 1

    app.terrain = [[None] * app.cols for _ in range(app.rows)]
    for col in range(len(app.terrain[0])):
        app.terrain[20][col] = Block(app, 25, col, "grass_block")

    app.ampl = 1
    app.freq = 1

def keyPressed(app, event):
    if event.key == "a":
        app.player.isMoving = True
        app.player.moveAnimation(-1)
    elif event.key == "d":
        app.player.isMoving = True
        app.player.moveAnimation(1)
    elif event.key == "s":
        app.player.isMoving = False
    elif event.key == "Space" and app.player.onGround(app):
        #app.player.jump(app)
        app.scrollDY = app.player.jumpSpeed
        app.scrollY += app.scrollDY

# runs even when key not released?
def keyReleased(app, event):
    #app.player.isMoving = False
    pass

def mousePressed(app, event):
    pass

def timerFired(app):
    if app.player.isMoving:
        app.player.moveAnimation(app.player.direction)
        if app.player.direction == -1:
            app.scrollX += app.player.speed 
        elif app.player.direction == 1:
            app.scrollX -= app.player.speed 

    if not app.player.onGround(app):
        app.player.fallAnimation(app.player.direction)
        app.scrollDY -= app.gravity
        app.scrollY += app.scrollDY

    if app.player.onGround(app) and not app.player.isMoving:
        app.player.standAnimation(app.player.direction)


def redrawAll(app, canvas):
    drawBlocks(app, canvas)
    app.player.draw(app, canvas)
    drawPerlin(app, canvas)

def drawBlocks(app, canvas):
    for row in range(len(app.terrain)):
        for col in range(len(app.terrain[0])):
            block = app.terrain[row][col]
            if block != None:
                block.draw(app, canvas)

def drawPerlin(app, canvas):
    x = 0
    while x < 50:
        x += 0.1
        y = Perlin.perlin(x)
        midX = app.width / 2
        midY = app.height / 2
        canvas.create_oval(x*100, 100 + y*100, x*100 + 10, 100 + y*100 + 10, fill="black")
    
def main():
    runTerraria()

if __name__ == "__main__":
    main()