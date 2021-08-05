class Block(object):
    width: int = 16
    height: int = 20
    row: int
    col: int
    material: str

    def __init__(self, row, col, material):
        self.row = row
        self.col = col
        self.material = material