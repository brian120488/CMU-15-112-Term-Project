from cmu_112_graphics import *

class Player(object):
    walkingSprites: list
    spriteCounter: int = 0
    width: int = 20
    height: int = 30
    x: int
    y: int
    speed: int = 10  # can make less jittery?
    direction: int = 1


    def __init__(self, app):
        self.x, self.y = app.width / 2, app.height / 2

        # initializes sprites
        path = "sprites/player_sprites.png"
        spritestrip = app.loadImage(path)
        numSprites = 19
        self.walkingSprites = []
        for i in range(6, numSprites):
            sprite = spritestrip.crop((self.width * i, 0, self.width * (i + 1), self.height))
            self.walkingSprites.append(sprite.transpose(Image.FLIP_LEFT_RIGHT))

    def __repr__(self):
        return "hi"

    def draw(self, app, canvas):
        sprite = self.walkingSprites[self.spriteCounter]
        canvas.create_image(self.x, self.y, image=ImageTk.PhotoImage(sprite))

    def move(self, direction):
        if direction != self.direction:
            self.direction = direction
            for i in range(len(self.walkingSprites)):
                self.walkingSprites[i] = self.walkingSprites[i].transpose(Image.FLIP_LEFT_RIGHT)
        self.x += self.speed * direction
        self.spriteCounter = (self.spriteCounter + 1) % len(self.walkingSprites)