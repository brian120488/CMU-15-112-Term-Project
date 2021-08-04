from cmu_112_graphics import *
from Player import Player

def runTerraria():
    width, height = 1280, 720
    runApp(width=width, height=height)

def appStarted(app):
    app.player = Player(app)

def keyPressed(app):
    pass

def mousePressed(app):
    pass

def redrawAll(app, canvas):
    for i in range(len(app.player.sprites)):
        canvas.create_image(20 * i, 200, image=ImageTk.PhotoImage(app.player.sprites[i]), anchor="w")
        canvas.create_line(0, 220, 20*19, 220)

def main():
    print('hi')
    runTerraria()

if __name__ == "__main__":
    main()