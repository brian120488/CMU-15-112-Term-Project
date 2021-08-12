from cmu_112_graphics import *

class Block(object):
    width = 20
    height = 20

    def __init__(self, app, row, col, material):
        self.row = row
        self.col = col
        self.material = material
        # https://hd-terraria-pics.fandom.com/wiki/Soil_Blocks grass block
        # https://www.pikpng.com/pngvi/iTJRwo_terraria-tree-terraria-tree-logo-png-clipart/ tree
        # https://terraria.fandom.com/wiki/Woods wood and wood block
        if self.material != "dirt_block":
            self.sprite = app.loadImage(f"sprites/{material}.png")

    def getXY(self, app):
        x = Block.width * self.col + Block.width / 2
        y = Block.height * self.row + Block.height / 2
        x += app.scrollX
        y += app.scrollY
        return x, y

    def draw(self, app, canvas):
        x, y = self.getXY(app)
        if self.material == "dirt_block":
            canvas.create_rectangle(self.getLeft(app), self.getTop(app) - 8, 
                                    self.getRight(app), self.getBottom(app),
                                    fill = "#8d654a",
                                    width = 0)
        elif self.material == "tree":
            image = self.getCachedPhotoImage(self.sprite)
            canvas.create_image(x, y - 22, image=image)
        else:
            image = self.getCachedPhotoImage(self.sprite)
            canvas.create_image(x, y, image=image)



    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#cachingPhotoImages
    def getCachedPhotoImage(self, image):
        # stores a cached version of the PhotoImage in the PIL/Pillow image
        if ('cachedPhotoImage' not in image.__dict__):
            image.cachedPhotoImage = ImageTk.PhotoImage(image)
        return image.cachedPhotoImage

    def getTop(self, app):
        _, y = self.getXY(app)
        return int(y - Block.height / 2) + 5
    
    def getBottom(self, app):
        _, y = self.getXY(app)
        return int(y + Block.height / 2)
    
    def getLeft(self, app):
        x, _ = self.getXY(app)
        return int(x - Block.width / 2)
        
    def getRight(self, app):
        x, _ = self.getXY(app)
        return int(x + Block.width / 2)
