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

Leftcollisions=ballsprite.collidingWithSprites(BoarderLeft)
Rightcollisions=ballsprite.collidingWithSprites(BoarderRight)
ScoreLeft1 = None
ScoreLeft2 = None
ScoreLeft3 = None
ScoreLeft4 = None
ScoreLeft5 = None
ScoreRight1 = None
ScoreRight2 = None
ScoreRight3 = None
ScoreRight4 = None
ScoreRight5 = None

def step():
    global ballsprite
    global ScoreLeft1
    global ScoreLeft2
    global ScoreLeft3
    global ScoreLeft4
    global ScoreLeft5
    global ScoreRight1
    global ScoreRight2
    global ScoreRight3
    global ScoreRight4
    global ScoreRight5
    
    
    
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
            
            if ScoreLeft4 and Leftcollisions:
                ScoreLeft5 = ScoreLeft(37,5)
            elif ScoreLeft3 and Leftcollisions:
                ScoreLeft4 = ScoreLeft(29,5)
            elif ScoreLeft2 and Leftcollisions:
                ScoreLeft3 = ScoreLeft(21,5)
            elif ScoreLeft1 and Leftcollisions:
                ScoreLeft2 = ScoreLeft(13,5)
            elif Leftcollisions:
                ScoreLeft1 = ScoreLeft(5,5)
            
            if ScoreRight4 and Rightcollisions:
                ScoreRight5 = ScoreLeft(
             
            
            if ScoreLeft5:
                print("Player Right Wins!")
                print("Game Over")
            else:
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
        #LeftcollisionsScore=ballsprite.collidingWithSprites(BoarderLeft)
        #RightcollisionsScore=ballsprite.collidingWithSprites(BoarderRight)
        
            
            
        
        
#-------------------------------------------------------------------------------







myapp.run(step)

