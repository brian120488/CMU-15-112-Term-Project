from cmu_112_graphics import *

class Player(object):
    def __init__(self, app):
        self.x, self.y = app.width / 2, app.height / 2
        self.width, self.height = 20, 30
        self.spriteCounter = 0
        self.direction = 1
        self.isMoving = False
        self.speed = 10
        self.jumpSpeed = 10

        # initializes sprites
        path = "sprites/player_sprites.png"
        spritestrip = app.loadImage(path)
        self.walkingSprites = []
        for i in range(6, 19):
            sprite = spritestrip.crop((self.width * i, 0, self.width * (i + 1), self.height))
            self.walkingSprites.append(sprite.transpose(Image.FLIP_LEFT_RIGHT))

    def draw(self, app, canvas):
        sprite = self.walkingSprites[self.spriteCounter]
        canvas.create_image(self.x, self.y, image=ImageTk.PhotoImage(sprite))

    def move(self, direction):
        if direction != self.direction:
            self.direction = direction
            for i in range(len(self.walkingSprites)):
                self.walkingSprites[i] = self.walkingSprites[i].transpose(Image.FLIP_LEFT_RIGHT)
        self.spriteCounter = (self.spriteCounter + 1) % len(self.walkingSprites)

    def onGround(self, app):
        for row in app.terrain:
            for block in row:
                if block != None:
                    if block.getTop(app) <= self.getBottom() <= block.getBottom(app):
                        app.scrollDY = 0
                        dif = self.getBottom() - block.getTop(app)
                        app.scrollY += dif
                        return True
        return False

    def getBottom(self):
        return int(self.y + self.height / 2)