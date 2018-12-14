"""
Patrick Daley
"""

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor
myapp = App(1017,512)

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

#-------------------------------------------------------------------------------
#Boarder
boarderup = RectangleAsset(1016,1, blkline, black)
class BoarderUp(Sprite):
    def __init__(self, x, y):
        super().__init__(boarderup, (x, y))
BoarderUp(0,100)

boarderdown = RectangleAsset(1016,1, blkline, black)
class BoarderDown(Sprite):
    def __init__(self, x, y):
        super().__init__(boarderdown, (x, y))
BoarderDown(0,510)

boarderleft = RectangleAsset(1,511, blkline, black)
class BoarderLeft(Sprite):
    def __init__(self, x, y):
        super().__init__(boarderleft, (x, y))
BoarderLeft(0,100)

boarderright = RectangleAsset(1,511, blkline, black)
class BoarderRight(Sprite):
    def __init__(self, x, y):
        super().__init__(boarderright, (x, y))
BoarderRight(1015,100)
#-------------------------------------------------------------------------------

#Player 1
player = RectangleAsset(15, 100, blkline, black)
#PlayerLeft = Sprite(player, (0,101))

class Playerleft(Sprite):
    def __init__(self, x, y):
        self.vy = 0
        super().__init__(player, (x, y))
PlayerLeft = Playerleft(0, 101)

def wkey(event):
    PlayerLeft.y -=10
    Upcollisions = PlayerLeft.collidingWithSprites(BoarderUp)
    while Upcollisions:
        PlayerLeft.y +=1
        Upcollisions = PlayerLeft.collidingWithSprites(BoarderUp)
myapp.listenKeyEvent('keydown', 'w', wkey)


def skey(event):
    PlayerLeft.y += 10
    Downcollisions = PlayerLeft.collidingWithSprites(BoarderDown)
    while Downcollisions:
        PlayerLeft.y -=1
        Downcollisions = PlayerLeft.collidingWithSprites(BoarderDown)
myapp.listenKeyEvent('keydown', 's', skey)
#-------------------------------------------------------------------------------
#Player 2
#PlayerRight = Sprite(player, (966,100))

class Playerright(Sprite):
    def __init__(self, x, y):
        self.vy = 0
        super().__init__(player, (x, y))
PlayerRight = Playerright(1000, 100)

def uparrowkey(event):
    PlayerRight.y -=10
    Upcollisions = PlayerRight.collidingWithSprites(BoarderUp)
    while Upcollisions:
        PlayerRight.y +=1
        Upcollisions = PlayerRight.collidingWithSprites(BoarderUp)
myapp.listenKeyEvent('keydown', 'up arrow', uparrowkey)

def downarrowkey(event):
    PlayerRight.y +=10
    Downcollisions = PlayerRight.collidingWithSprites(BoarderDown)
    while Downcollisions:
        PlayerRight.y -=1
        Downcollisions = PlayerRight.collidingWithSprites(BoarderDown)
myapp.listenKeyEvent('keydown', 'down arrow', downarrowkey)

#-------------------------------------------------------------------------------

#Ball Sprite
ball = CircleAsset(20, thinline, red)
#Sprite(ball, (30, 30))

class Ball(Sprite):
    def __init__(self, x, y):
        self.vy = 0
        self.vx = 0
        super().__init__(ball, (x, y))

ballsprite = Ball(55,100)

#-------------------------------------------------------------------------------
#Score-tally marks
score = RectangleAsset(5,30, blkline, green)

class ScoreLeft(Sprite):
    def __init__(self, x, y):
        self.vy = 0
        super().__init__(score, (x, y))

class ScoreRight(Sprite):
    def __init__(self, x, y):
        self.vy = 0
        super().__init__(score, (x, y))
#ScoreLeft(5,5)

#-------------------------------------------------------------------------------
if ballsprite:
    ballsprite.vy = 5
    ballsprite.vx = 5



def step():
    global ballsprite
    if ballsprite:
        ballsprite.y += ballsprite.vy
        ballsprite.x += ballsprite.vx
        Upcollisions = ballsprite.collidingWithSprites(BoarderUp)
        if Upcollisions:
            ballsprite.vy = 5
            ballsprite.y += ballsprite.vy
        Downcollisions = ballsprite.collidingWithSprites(BoarderDown)
        if Downcollisions:
            ballsprite.vy = -5
            ballsprite.y += ballsprite.vy
        PlayerLeftcollisions = ballsprite.collidingWithSprites(Playerleft)
        if PlayerLeftcollisions:
            ballsprite.vx = 5
            ballsprite.x += ballsprite.vx
        PlayerRightcollisions = ballsprite.collidingWithSprites(Playerright)
        if PlayerRightcollisions:
            ballsprite.vx = -5
            ballsprite.x += ballsprite.vx
         #----------------------------------------------------------------------
         #When ball hits wall behind the players
        Leftcollisions=ballsprite.collidingWithSprites(BoarderLeft)
        Rightcollisions=ballsprite.collidingWithSprites(BoarderRight)
        if Leftcollisions:
            print("Right Wins!")
            if ballsprite:
                ballsprite.destroy()
                ScoreLeft1 = ScoreLeft(5,5)
            if 
            
            ballsprite = Ball(900, 100)
            ballsprite.vy = 5
            ballsprite.y += ballsprite.vy
            ballsprite.vx = -5
            ballsprite.x += ballsprite.vx
            
        if Rightcollisions:
            print("Left Wins!")
            if ballsprite:
                ballsprite.destroy()
            ballsprite = Ball(55, 100)
            ballsprite.vy = 5
            ballsprite.y += ballsprite.vy
            ballsprite.vx = 5
            ballsprite.x += ballsprite.vx
        #-----------------------------------------------------------------------
        LeftcollisionsScore=ballsprite.collidingWithSprites(BoarderLeft)
        RightcollisionsScore=ballsprite.collidingWithSprites(BoarderRight)
        if LeftcollisionsScore and ScoreLeft1:
            ScoreLeft2 = Score(12,5)
            
            
        
        
#-------------------------------------------------------------------------------







myapp.run(step)

