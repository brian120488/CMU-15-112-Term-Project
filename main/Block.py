from cmu_112_graphics import *

class Block(object):
    width = 16
    height = 20

    def __init__(self, app, row, col, material):
        self.row = row
        self.col = col
        self.material = material
        self.sprite = app.loadImage(f"sprites/{material}.png")

    # @staticmethod
    # def moveAllBlocks(app, drow, dcol):
    #     rows = len(app.terrain)
    #     cols = len(app.terrain[0])
    #     for i in range(rows):
    #         for j in range(cols):
    #             block = app.terrain[i][j]
    #             if block != None:
    #                 block.row += drow
    #                 block.col += dcol
    
    def getXY(self):
        x = Block.width * self.col + Block.width / 2
        y = Block.height * self.row + Block.height / 2
        return x, y

    def draw(self, app, canvas):
        x, y = self.getXY()
        x -= app.scrollX
        canvas.create_image(x, y, image=ImageTk.PhotoImage(self.sprite))

    def getTop(self):
        _, y = self.getXY()
        return int(y - Block.height / 2)
    
    def getBottom(self):
        _, y = self.getXY()
        return int(y + Block.height / 2)
