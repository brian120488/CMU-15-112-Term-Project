from cmu_112_graphics import *
from Player import Player
from Block import Block
from Perlin import Perlin
import random

def runTerraria():
    width, height = 800, 400
    runApp(width=width, height=height)

# TODO:
# cite images(check again)
# cannot generate to the left because blocks based on row, col
# moving in tight spaces is buggy
# add placing and pressing numbers to change block

def appStarted(app):
    app._root.resizable(False, False)
    app.timerDelay = 10
    app.rows = int(app.height / Block.height) + 1
    app.cols = int(app.width / Block.width)

    app.player = Player(app)
    app.scrollX = 0
    app.scrollY = 0
    app.scrollDY = 0
    app.gravity = 1

    app.terrain = [[None] for _ in range(app.rows)]
    app.midRow = int(app.rows / 2) + 2
    for col in range(app.cols):
        appendColumn(app, app.terrain, app.midRow)

    app.ampl = 25
    app.freq = 1000
    app.showPerlin = False

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
    elif event.key == "p":
        app.showPerlin = not app.showPerlin
    elif event.key == "r":
        appStarted(app)

def mousePressed(app, event):
    mouseX = event.x - app.scrollX
    mouseY = event.y - app.scrollY
    mouseRow = int(mouseY / Block.height)
    mouseCol = int(mouseX / Block.width)
    block = app.terrain[mouseRow][mouseCol]

    # when the player mines a block
    if block != None:
        app.terrain[mouseRow][mouseCol] = None
        app.player.inventory[block.material] = app.player.inventory.get(block.material, 0) + 1
        if block.material == "grass_block":
            image = app.loadImage("sprites/grass_block.png")
            app.player.inventoryImages["grass_block"] = image
        elif block.material == "tree":
            image = app.loadImage("sprites/wood.png")
            app.player.inventoryImages["wood"] = image
            print(app.player.inventoryImages)
            pass # TODO
    else:
        # place block
        pass

def timerFired(app):
    distanceTravelled = -app.scrollX
    if distanceTravelled + app.width > len(app.terrain[0]) * Block.width:
        y = int(Perlin.perlin(distanceTravelled / app.freq) * app.ampl - 2)
        appendColumn(app, app.terrain, app.midRow + y)

    if app.player.isMoving:
        app.player.moveAnimation(app.player.direction)
        if app.player.direction == -1 and app.player.nextWall(app) != -1:
            app.scrollX += app.player.speed 
        elif app.player.direction == 1 and app.player.nextWall(app) != 1:
            app.scrollX -= app.player.speed 
        else:
            app.player.standAnimation(app.player.direction)

    if not app.player.onGround(app):
        app.player.fallAnimation(app.player.direction)
        app.scrollDY -= app.gravity
        app.scrollY += app.scrollDY

    if app.player.onGround(app) and not app.player.isMoving:
        app.player.standAnimation(app.player.direction)

def redrawAll(app, canvas):
    drawBlocks(app, canvas)
    app.player.draw(app, canvas)
    if app.showPerlin:
        drawPerlin(app, canvas)
    drawInventorySlots(app, canvas)
    drawInventory(app, canvas)

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
        canvas.create_oval(x*100, 100 + y*100, x*100 + 10, 100 + y*100 + 10, fill="black")
    
def drawInventorySlots(app, canvas):
    margin = 5
    cellSize = 40
    for i in range(10):
        canvas.create_rectangle(
            margin + (margin + cellSize) * i, margin, 
            (margin + cellSize) * (i + 1), margin + cellSize,
            fill = "#3D4AA9",
            width = 0.5 # no idea if this even does anything tbh
        )
        canvas.create_text(
            1 + margin + (margin + cellSize) * i, margin, 
            text = str(i+1), 
            fill = "white",
            anchor = "nw"
        )

def drawInventory(app, canvas):
    i = 0
    margin = 5
    cellSize = 40
    for material in app.player.inventory:
        x = (margin + (margin + cellSize) * (2 * i + 1)) / 2
        y = margin + cellSize / 2
        if material == "grass_block" and material in app.player.inventoryImages:
            image = app.player.inventoryImages[material]
            canvas.create_image(x, y, image=ImageTk.PhotoImage(image))
        elif material == "dirt_block":
            canvas.create_rectangle(x - 10, y - 10, x + 10, y + 10, fill="#8d654a", width=0)
        elif material == "tree" and "wood" in app.player.inventoryImages:
            image = app.player.inventoryImages["wood"]
            canvas.create_image(x, y, image=ImageTk.PhotoImage(image))

        canvas.create_text(
            1 + margin + (margin + cellSize) * i, margin + cellSize, 
            text = str(app.player.inventory[material]), 
            fill = "white",
            anchor = "sw"
        )

        i += 1

# appends a column of blocks in app.terrain at height h
# each iteration has a chance to spawn a tree
def appendColumn(app, L, h):
    for j in range(len(L)):
        row = L[j]
        if j == h - 1 and random.random() < 0.1:
            row.append(Block(app, j, len(L[0]) - 1, "tree"))
        elif j == h:
            row.append(Block(app, j, len(L[0]) - 1, "grass_block"))
        elif j > h:
            row.append(Block(app, j, len(L[0]) - 1, "dirt_block"))
        else:
            row.append(None)

def main():
    runTerraria()

if __name__ == "__main__":
    main()