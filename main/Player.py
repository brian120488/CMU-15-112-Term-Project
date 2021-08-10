from cmu_112_graphics import *
from Block import Block

class Player(object):
    def __init__(self, app):
        self.x, self.y = app.width / 2, app.height / 2
        self.width, self.height = 20, 30
        self.spriteCounter = 0
        self.direction = 1
        self.isMoving = False
        self.speed = 10
        self.jumpSpeed = 10
        self.inventory = [None] * 10

        # initializes sprites from https://www.deviantart.com/omega7321/art/Terraria-Default-Player-sprite-sheet-637899627
        path = "sprites/player_sprites.png"
        spritestrip = app.loadImage(path)
        self.walkingSprites = []
        for i in range(6, 19):
            sprite = spritestrip.crop((self.width * i, 0, self.width * (i + 1), self.height))
            self.walkingSprites.append(sprite.transpose(Image.FLIP_LEFT_RIGHT))
            
        self.fallingSprites = []
        for i in range(5, 6):
            sprite = spritestrip.crop((self.width * i, 0, self.width * (i + 1), self.height))
            self.fallingSprites.append(sprite.transpose(Image.FLIP_LEFT_RIGHT))
            
        self.standingSprites = []
        for i in range(1):
            sprite = spritestrip.crop((self.width * i, 0, self.width * (i + 1), self.height))
            self.standingSprites.append(sprite.transpose(Image.FLIP_LEFT_RIGHT)) 
        
        self.currSprite = self.standingSprites[0]

    def draw(self, app, canvas):
        canvas.create_image(self.x, self.y, image=ImageTk.PhotoImage(self.currSprite))

    def rotateAllAnimations(self):
        for i in range(len(self.walkingSprites)):
            self.walkingSprites[i] = self.walkingSprites[i].transpose(Image.FLIP_LEFT_RIGHT)
        for i in range(len(self.fallingSprites)):
            self.fallingSprites[i] = self.fallingSprites[i].transpose(Image.FLIP_LEFT_RIGHT)
        for i in range(len(self.standingSprites)):
            self.standingSprites[i] = self.standingSprites[i].transpose(Image.FLIP_LEFT_RIGHT)

    def moveAnimation(self, direction):
        if direction != self.direction:
            self.direction = direction
            self.rotateAllAnimations()
        self.spriteCounter = (self.spriteCounter + 1) % len(self.walkingSprites)
        self.currSprite = self.walkingSprites[self.spriteCounter]

    def fallAnimation(self, direction):
        if direction != self.direction:
            self.direction = direction
            self.rotateAllAnimations()
        self.spriteCounter = (self.spriteCounter + 1) % len(self.fallingSprites)
        self.currSprite = self.fallingSprites[self.spriteCounter]

    def standAnimation(self, direction):
        if direction != self.direction:
            self.direction = direction
            self.rotateAllAnimations()
        self.spriteCounter = (self.spriteCounter + 1) % len(self.standingSprites)
        self.currSprite = self.standingSprites[self.spriteCounter]

    def onGround(self, app):
        for row in app.terrain:
            for block in row:
                if block != None:
                    if (block.getTop(app) <= self.getBottom() <= block.getBottom(app)
                        and block.getLeft(app) <= self.x <= block.getRight(app)
                        and app.scrollDY <= 0):
                        app.scrollDY = 0
                        dif = self.getBottom() - block.getTop(app)
                        app.scrollY += dif
                        return True
        return False

    # returns which wall the player is next to (-1 = left, 1 = right, and 0 = no walls)
    def nextWall(self, app):
        for row in app.terrain:
            for block in row:
                if block != None:
                    _, blockY = block.getXY(app)
                    blockLeft = block.getLeft(app)
                    blockRight = block.getRight(app)
                    if ((blockLeft <= self.getRight() <= blockRight
                        or blockLeft <= self.getLeft() <= blockRight)
                        and self.getTop() < blockY < self.getBottom()):
                        return int(blockLeft <= self.getRight() <= blockRight) * 2 - 1
        return 0

    def getTop(self):
        return int(self.y - self.height / 2)

    def getBottom(self):
        return int(self.y + self.height / 2)

    def getLeft(self):
        return int(self.x - self.width / 2)

    def getRight(self):
        return int(self.x + self.width / 2)

