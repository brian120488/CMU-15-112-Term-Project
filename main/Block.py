from cmu_112_graphics import *

class Block(object):
    width = 16
    height = 20

    def __init__(self, app, row, col, material):
        self.row = row
        self.col = col
        self.material = material
        self.sprite = app.loadImage(f"sprites/{material}.png")
    
    def draw(self, app, canvas):
        x0, y0, x1, y1 = self.getCellBounds(app)
        x = (x0 + x1) / 2
        y = (y0 + y1) / 2
        canvas.create_image(x, y, image=ImageTk.PhotoImage(self.sprite))
    
    def getCellBounds(self, app):
        x0 = Block.width * self.col
        y0 = Block.height * self.row
        x1 = x0 + Block.width
        y1 = y0 + Block.height
        return x0, y0, x1, y1

