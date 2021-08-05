from cmu_112_graphics import *

class Player(object):
    walkingSprites: list
    spriteCounter: int = 0
    width: int = 20
    height: int = 30
    speed: int = 6
    x: int
    y: int
    speed: int = 10  # can make less jittery?


    def __init__(self, app):
        self.x, self.y = app.width / 2, app.height / 2

        # initializes sprites
        path = "sprites/player_sprites.png"
        spritestrip = app.loadImage(path)
        numSprites = 19
        self.walkingSprites = []
        for i in range(6, numSprites):
            sprite = spritestrip.crop((self.width * i, 0, self.width * (i + 1), self.height))
            self.walkingSprites.append(sprite)

    def __repr__(self):
        return "hi"

    def draw(self, app, canvas):
        sprite = self.walkingSprites[self.spriteCounter]
        canvas.create_image(self.x, self.y, image=ImageTk.PhotoImage(sprite))

    def move(self, direction):
        self.x += self.speed * direction
        self.spriteCounter = (self.spriteCounter + 1) % len(self.walkingSprites)
