"""
Patrick Daley
"""

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor
myapp = App()
blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)

#--------------------------------------------------------------------------------------------------------------------
#Boarder
boarderup = RectangleAsset(1016,1, noline, black)
Sprite(boarderup, (0,100))
boarderdown = RectangleAsset(1016,1, noline, black)
Sprite(boarderdown, (0,511))
boarderleft = RectangleAsset(1,511, noline, black)
Sprite(boarderleft, (0,100))
boarderright = RectangleAsset(1,511, noline, black)
Sprite(boarderright, (1016,100))
#--------------------------------------------------------------------------------------------------------------------

#Player 1
player = RectangleAsset(50,200, blkline, black)
PlayerLeft = Sprite(player, (0,0))

class Playerleft(Sprite):
    def __init__(self, x, y):
        self.vy = 0
        super().__init__(player, (x, y))

def wkey(event):
    PlayerLeft.y -=10
    Upcollisions = PlayerLeft.collidingWithSprites(boarderup)
    while Upcollisions:
        PlayerLeft.y +=1
        Upcollisions = PlayerLeft.collidingWithSprites(boarderup)
myapp.listenKeyEvent('keydown', 'w', wkey)

def skey(event):
    PlayerLeft.y += 10
    Downcollisions = PlayerLeft.collidingWithSprites(boarderdown)
    while Downcollisions:
        PlayerLeft.y -=1
        Downcollisions = PlayerLeft.collidingWithSprites(boarderdown)

#--------------------------------------------------------------------------------------------------------------------
#Player 2
PlayerRight = Sprite(player, (966,0))

class Playerright(Sprite):
    def __init__(self, x, y):
        self.vy = 0
        super().__init__(player, (x, y))

def uparrowkey(event):
    PlayerRight.y -=10
    Upcollisions = PlayerRight.collidingWithSprites(boarderup)
    while Upcollisions:
        PlayerLeft.y +=1
        Upcollisions = PlayerRight.collidingWithSprites(boarderup)
myapp.listenKeyEvent('keydown', 'uparrow', uparrowkey)


#--------------------------------------------------------------------------------------------------------------------

#Ball Sprite
ball = CircleAsset(20, thinline, red)
#Sprite(ball, (30, 30))

class Ball(Sprite):
    def __init__(self, x, y):
        self.vy = 0
        super().__init__(ball, (x, y))





myapp.listenKeyEvent('keydown', 's', skey)



myapp.run()