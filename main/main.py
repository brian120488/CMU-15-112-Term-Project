from cmu_112_graphics import *
from Player import Player
from Block import Block

def runTerraria():
    width, height = 1280, 720
    runApp(width=width, height=height)


# TODO: make the terrain into set instead?
# check for keyreleased for better movement
# set random button to make a parabola jump?
# add citations
# proposal.txt

def appStarted(app):
    app._root.resizable(False, False)
    app.timerDelay = 10
    app.rows = int(app.height / Block.height)
    app.cols = int(app.width / Block.width)

    app.player = Player(app)
    app.scrollX = 0
    app.scrollY = 0
    app.scrollDY = 0
    app.gravity = 0.5

    app.terrain = [[None] * app.cols for _ in range(app.rows)]
    for col in range(len(app.terrain[0])):
        app.terrain[20][col] = Block(app, 25, col, "grass_block")

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
    if app.player.onGround(app):
        pass
    else:
        # player falling
        app.scrollDY -= app.gravity
        app.scrollY += app.scrollDY
    #print(app.scrollY)


def redrawAll(app, canvas):
    drawBlocks(app, canvas)
    app.player.draw(app, canvas)

def drawBlocks(app, canvas):
    for row in range(len(app.terrain)):
        for col in range(len(app.terrain[0])):
            block = app.terrain[row][col]
            if block != None:
                block.draw(app, canvas)

def main():
    runTerraria()

if __name__ == "__main__":
    main()