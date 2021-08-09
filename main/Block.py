from cmu_112_graphics import *

class Block(object):
    width = 16
    height = 20

    def __init__(self, app, row, col, material):
        self.row = row
        self.col = col
        self.material = material
        self.sprite = app.loadImage(f"sprites/{material}.png")

    def getXY(self, app):
        x = Block.width * self.col + Block.width / 2
        y = Block.height * self.row + Block.height / 2
        x += app.scrollX
        y += app.scrollY
        return x, y

    def draw(self, app, canvas):
        x, y = self.getXY(app)
        canvas.create_image(x, y, image=ImageTk.PhotoImage(self.sprite))

    def getTop(self, app):
        _, y = self.getXY(app)
        return int(y - Block.height / 2) + 5
    
    def getBottom(self, app):
        _, y = self.getXY(app)
        return int(y + Block.height / 2)
