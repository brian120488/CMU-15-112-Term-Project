class Player(object):
    sprites: list
    spriteCounter: int = 0
    width: int = 20
    height: int = 30

    def __init__(self, app):
        path = "sprites/player_sprites.png"
        spritestrip = app.loadImage(path)
        self.sprites = []
        numSprites = 19
        for i in range(numSprites):
            sprite = spritestrip.crop((self.width * i, 0, self.width * (i + 1), self.height))
            self.sprites.append(sprite)

    def __repr__(self):
        return self.spritestrip