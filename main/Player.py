from cmu_112_graphics import *

class Player(object):
    def __init__(self, app):
        self.x, self.y = app.width / 2, app.height / 2
        self.width, self.height = 20, 30
        self.spriteCounter = 0
        self.speed = 10
        self.direction = 1
        self.jumpSpeed = -10
        #self.onGround = False
        self.gravity = 1
        self.dy = 0

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

    def jump(self, app):
        self.dy = self.jumpSpeed
        self.y += self.dy
        
    def fall(self, app):
        self.dy += self.gravity
        self.y += self.dy

    def onGround(self, app):
        margin = 5 # margin of an error
        for row in app.terrain:
            for block in row:
                if block != None:
                    if block.getTop() <= self.getBottom() <= block.getBottom():
                        self.y = block.getTop() - self.height / 2 + margin
                        return True
        return False

    def getBottom(self):
        return int(self.y + self.height / 2)

def withinNum(x, y, n = 1):
    return 0 <= abs(x - y) <= n