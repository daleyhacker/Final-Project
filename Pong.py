"""
Patrick Daley
"""

from ggame import App, Color, LineStyle, Sprite, TextAsset, Color
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



Leftname = input("What is the player on the left side's name? ")
Rightname =input("What is the player on the right side's name? ")

LeftTA = (Leftname, style = "40pt Arial", width = 200, fill = black)


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
#----------------------------
global wkeyisdown
wkeyisdown = False
def wkey(event):
    global wkeyisdown
    wkeyisdown = True
myapp.listenKeyEvent('keydown', 'w', wkey)

def wkeyup(event):
    global wkeyisdown
    wkeyisdown = False
myapp.listenKeyEvent('keyup', 'w', wkeyup)

#--------------------------
global skeyisdown
skeyisdown = False
def skey(event):
    global skeyisdown
    skeyisdown = True
myapp.listenKeyEvent('keydown', 's', skey)

def skeyup(event):
    global skeyisdown
    skeyisdown = False
myapp.listenKeyEvent('keyup', 's', skeyup)

#-------------------------------------------------------------------------------
#Player 2
#PlayerRight = Sprite(player, (966,100))

class Playerright(Sprite):
    def __init__(self, x, y):
        self.vy = 0
        super().__init__(player, (x, y))
PlayerRight = Playerright(1000, 100)
#---------------------------------
global uparrowisdown
uparrowisdown = False
def uparrowkey(event):
    global uparrowisdown
    uparrowisdown = True

myapp.listenKeyEvent('keydown', 'up arrow', uparrowkey)

def uparrowkeyup(event):
    global uparrowisdown
    uparrowisdown = False
myapp.listenKeyEvent('keyup', 'up arrow', uparrowkeyup)
#------------------------------
global downarrowdown
downarrowdown = False
def downarrowkey(event):
    global downarrowdown
    downarrowdown = True
downarrowkeydown = myapp.listenKeyEvent('keydown', 'down arrow', downarrowkey)

def downarrowkeyup(event):
    global downarrowdown
    downarrowdown = False
myapp.listenKeyEvent('keyup', 'down arrow', downarrowkeyup)

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
    ballsprite.vy = 7
    ballsprite.vx = 7

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
    
    if skeyisdown:
        PlayerLeft.y += 5
        Downcollisions = PlayerLeft.collidingWithSprites(BoarderDown)
        while Downcollisions:
            PlayerLeft.y -=5
            Downcollisions = PlayerLeft.collidingWithSprites(BoarderDown)
    if wkeyisdown:
        PlayerLeft.y -=5
        Upcollisions = PlayerLeft.collidingWithSprites(BoarderUp)
        while Upcollisions:
            PlayerLeft.y +=5
            Upcollisions = PlayerLeft.collidingWithSprites(BoarderUp)
    if uparrowisdown:
        PlayerRight.y -=5
        Upcollisions = PlayerRight.collidingWithSprites(BoarderUp)
        while Upcollisions:
            PlayerRight.y +=1
            Upcollisions = PlayerRight.collidingWithSprites(BoarderUp)
    if downarrowdown:
        PlayerRight.y +=5
        Downcollisions = PlayerRight.collidingWithSprites(BoarderDown)
        while Downcollisions:
            PlayerRight.y -=1
            Downcollisions = PlayerRight.collidingWithSprites(BoarderDown)
        
    
    if ballsprite:
        ballsprite.y += ballsprite.vy
        ballsprite.x += ballsprite.vx
        Upcollisions = ballsprite.collidingWithSprites(BoarderUp)
        Downcollisions = ballsprite.collidingWithSprites(BoarderDown)
        PlayerLeftcollisions = ballsprite.collidingWithSprites(Playerleft)
        PlayerRightcollisions = ballsprite.collidingWithSprites(Playerright)
        if Upcollisions:
            ballsprite.vy = -(ballsprite.vy -.1)
            ballsprite.y += ballsprite.vy
        
        if Downcollisions:
            ballsprite.vy = -(ballsprite.vy +.1)
            ballsprite.y += ballsprite.vy
        
        if PlayerLeftcollisions:
            ballsprite.vx = -(ballsprite.vx -.1)
            ballsprite.x += ballsprite.vx
        
        if PlayerRightcollisions:
            ballsprite.vx = -(ballsprite.vx +.1)
            ballsprite.x += ballsprite.vx
         #----------------------------------------------------------------------
         #When ball hits wall behind the players
        Leftcollisions=ballsprite.collidingWithSprites(BoarderLeft)
        Rightcollisions=ballsprite.collidingWithSprites(BoarderRight)
        if Leftcollisions:
            
            if ballsprite:
                ballsprite.destroy()
                ballsprite = None
            
            if ScoreRight4 and Leftcollisions:
                ScoreRight5 = ScoreLeft(966,5)
            elif ScoreRight3 and Leftcollisions:
                ScoreRight4 = ScoreLeft(976,5)
            elif ScoreRight2 and Leftcollisions:
                ScoreRight3 = ScoreLeft(986,5)
            elif ScoreRight1 and Leftcollisions:
                ScoreRight2 = ScoreLeft(996,5)
            elif Leftcollisions:
                ScoreRight1 = ScoreLeft(1006,5)
            
            if ScoreRight5:
                print(Rightname + " Wins!")
                print("Game Over")
            
            elif ScoreRight4 or ScoreLeft3:
                ballsprite = Ball(900, 100)
                ballsprite.vy = 8.5
                ballsprite.y += ballsprite.vy
                ballsprite.vx = -8.5
                ballsprite.x += ballsprite.vx
            elif ScoreRight3 or ScoreLeft2:
                ballsprite = Ball(900, 100)
                ballsprite.vy = 8
                ballsprite.y += ballsprite.vy
                ballsprite.vx = -8
                ballsprite.x += ballsprite.vx
            elif ScoreRight2 or ScoreLeft1:
                ballsprite = Ball(900, 100)
                ballsprite.vy = 7.5
                ballsprite.y += ballsprite.vy
                ballsprite.vx = -7.5
                ballsprite.x += ballsprite.vx
            elif ScoreRight1:
                ballsprite = Ball(900, 100)
                ballsprite.vy = 7
                ballsprite.y += ballsprite.vy
                ballsprite.vx = -7
                ballsprite.x += ballsprite.vx
            '''else:
                ballsprite = Ball(900, 100)
                ballsprite.vy = 5
                ballsprite.y += ballsprite.vy
                ballsprite.vx = -5
                ballsprite.x += ballsprite.vx'''
            
            
        if Rightcollisions:
            
            if ballsprite:
                ballsprite.destroy()
                ballsprite = None
            
            if ScoreLeft4 and Rightcollisions:
                ScoreLeft5 = ScoreLeft(44, 5)
            elif ScoreLeft3 and Rightcollisions:
                ScoreLeft4 = ScoreLeft(34, 5)
            elif ScoreLeft2 and Rightcollisions:
                ScoreLeft3 = ScoreLeft(24, 5)
            elif ScoreLeft1 and Rightcollisions:
                ScoreLeft2 = ScoreLeft(14, 5)
            elif Rightcollisions:
                ScoreLeft1 = ScoreLeft(4, 5)
                
            if ScoreLeft5:
                print(Leftname + " Wins!")
                print("Game Over")
            
            elif ScoreLeft4 or ScoreRight3:
                ballsprite = Ball(55, 100)
                ballsprite.vy = 8.5
                ballsprite.y += ballsprite.vy
                ballsprite.vx = 7.5
                ballsprite.x += ballsprite.vx
            elif ScoreLeft3 or ScoreRight2:
                ballsprite = Ball(55, 100)
                ballsprite.vy = 8
                ballsprite.y += ballsprite.vy
                ballsprite.vx = 8
                ballsprite.x += ballsprite.vx
            elif ScoreLeft2 or ScoreRight1:
                ballsprite = Ball(55, 100)
                ballsprite.vy = 7.5
                ballsprite.y += ballsprite.vy
                ballsprite.vx = 7.5
                ballsprite.x += ballsprite.vx
            elif ScoreLeft1:
                ballsprite = Ball(55, 100)
                ballsprite.vy = 7
                ballsprite.y += ballsprite.vy
                ballsprite.vx = 7
                ballsprite.x += ballsprite.vx
            '''else:
                ballsprite = Ball(55, 100)
                ballsprite.vy = 5
                ballsprite.y += ballsprite.vy
                ballsprite.vx = 5
                ballsprite.x += ballsprite.vx'''
        #-----------------------------------------------------------------------
        
        
            
            
        
        
#-------------------------------------------------------------------------------







myapp.run(step)

