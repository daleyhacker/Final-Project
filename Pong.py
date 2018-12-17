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
            ballsprite.vy = -ballsprite.vy
            ballsprite.y += ballsprite.vy
        Downcollisions = ballsprite.collidingWithSprites(BoarderDown)
        if Downcollisions:
            ballsprite.vy = -ballsprite.vy
            ballsprite.y += ballsprite.vy
        PlayerLeftcollisions = ballsprite.collidingWithSprites(Playerleft)
        if PlayerLeftcollisions:
            ballsprite.vx = -ballsprite.vx
            ballsprite.x += ballsprite.vx
        PlayerRightcollisions = ballsprite.collidingWithSprites(Playerright)
        if PlayerRightcollisions:
            ballsprite.vx = -ballsprite.vx
            ballsprite.x += ballsprite.vx
         #----------------------------------------------------------------------
         #When ball hits wall behind the players
        Leftcollisions=ballsprite.collidingWithSprites(BoarderLeft)
        Rightcollisions=ballsprite.collidingWithSprites(BoarderRight)
        if Leftcollisions:
            print("Right Wins!")
            if ballsprite:
                ballsprite.destroy()
                ballsprite = None
            
            if ScoreRight4 and Leftcollisions:
                ScoreRight5 = ScoreLeft(974,5)
            elif ScoreRight3 and Leftcollisions:
                ScoreRight4 = ScoreLeft(982,5)
            elif ScoreRight2 and Leftcollisions:
                ScoreRight3 = ScoreLeft(990,5)
            elif ScoreRight1 and Leftcollisions:
                ScoreRight2 = ScoreLeft(998,5)
            elif Leftcollisions:
                ScoreRight1 = ScoreLeft(1006,5)
            
            if ScoreRight5:
                print("Player Right Wins!")
                print("Game Over")
            
            elif ScoreRight4 or ScoreLeft3:
                ballsprite = Ball(900, 100)
                ballsprite.vy = 7.5
                ballsprite.y += ballsprite.vy
                ballsprite.vx = -7.5
                ballsprite.x += ballsprite.vx
            elif ScoreRight3 or ScoreLeft2:
                ballsprite = Ball(900, 100)
                ballsprite.vy = 7
                ballsprite.y += ballsprite.vy
                ballsprite.vx = -7
                ballsprite.x += ballsprite.vx
            elif ScoreRight2 or ScoreLeft1:
                ballsprite = Ball(900, 100)
                ballsprite.vy = 6.5
                ballsprite.y += ballsprite.vy
                ballsprite.vx = -6.5
                ballsprite.x += ballsprite.vx
            elif ScoreRight1:
                ballsprite = Ball(900, 100)
                ballsprite.vy = 6
                ballsprite.y += ballsprite.vy
                ballsprite.vx = -6
                ballsprite.x += ballsprite.vx
            '''else:
                ballsprite = Ball(900, 100)
                ballsprite.vy = 5
                ballsprite.y += ballsprite.vy
                ballsprite.vx = -5
                ballsprite.x += ballsprite.vx'''
            
            
        if Rightcollisions:
            print("Left Wins!")
            if ballsprite:
                ballsprite.destroy()
                ballsprite = None
            
            if ScoreLeft4 and Rightcollisions:
                ScoreLeft5 = ScoreLeft(36, 5)
            elif ScoreLeft3 and Rightcollisions:
                ScoreLeft4 = ScoreLeft(28, 5)
            elif ScoreLeft2 and Rightcollisions:
                ScoreLeft3 = ScoreLeft(20, 5)
            elif ScoreLeft1 and Rightcollisions:
                ScoreLeft2 = ScoreLeft(12, 5)
            elif Rightcollisions:
                ScoreLeft1 = ScoreLeft(4, 5)
                
            if ScoreLeft5:
                print("Player Left Wins!")
                print("Game Over")
            
            elif ScoreLeft4 or ScoreRight3:
                ballsprite = Ball(55, 100)
                ballsprite.vy = 7.5
                ballsprite.y += ballsprite.vy
                ballsprite.vx = 7.5
                ballsprite.x += ballsprite.vx
            elif ScoreLeft3 or ScoreRight2:
                ballsprite = Ball(55, 100)
                ballsprite.vy = 7
                ballsprite.y += ballsprite.vy
                ballsprite.vx = 7
                ballsprite.x += ballsprite.vx
            elif ScoreLeft2 or ScoreRight1:
                ballsprite = Ball(55, 100)
                ballsprite.vy = 6.5
                ballsprite.y += ballsprite.vy
                ballsprite.vx = 6.5
                ballsprite.x += ballsprite.vx
            elif ScoreLeft1:
                ballsprite = Ball(55, 100)
                ballsprite.vy = 6
                ballsprite.y += ballsprite.vy
                ballsprite.vx = 6
                ballsprite.x += ballsprite.vx
            '''else:
                ballsprite = Ball(55, 100)
                ballsprite.vy = 5
                ballsprite.y += ballsprite.vy
                ballsprite.vx = 5
                ballsprite.x += ballsprite.vx'''
        #-----------------------------------------------------------------------
        #LeftcollisionsScore=ballsprite.collidingWithSprites(BoarderLeft)
        #RightcollisionsScore=ballsprite.collidingWithSprites(BoarderRight)
        
            
            
        
        
#-------------------------------------------------------------------------------







myapp.run(step)

