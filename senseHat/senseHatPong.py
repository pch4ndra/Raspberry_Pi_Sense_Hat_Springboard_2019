from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()

white = (255, 255, 255)
ballColor = (0, 255, 0)
b = (0, 0, 0)
numBlocks = 0

batY = 4
ballPosition = [3, 3]
ballVelocity = [1, 1]
score = 0

blocks = [[b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b]]

# Functions ------------------------
def newBlocks():
    global numBlocks
    for x in range(7,8):
        for y in range(0,8):
            blocks[y][x] = (randint(50,255), randint(50,255), randint(50,255))
            numBlocks += 1
            
def drawBlocks():
    sense.set_pixels(sum(blocks, []))

def drawBat():
    sense.set_pixel(0, batY, white)
    sense.set_pixel(0, batY + 1, white)
    sense.set_pixel(0, batY - 1, white)
    
def moveUp(event):
    global batY
    if event.action == 'pressed' and batY > 1:
        batY -= 1
        
def moveDown(event):
    global batY
    if event.action == 'pressed' and batY < 6:
        batY += 1
        
def drawBall():
    global numBlocks
    sense.set_pixel(ballPosition[0],ballPosition[1],ballColor)
    ballPosition[0] += ballVelocity[0]
    if ballPosition[0] == 7 or ballPosition[0] == 0:
        ballVelocity[0] = -ballVelocity[0]
    ballPosition[1] += ballVelocity[1]
    if ballPosition[1] == 7 or ballPosition[1] == 0:
        ballVelocity[1] = -ballVelocity[1]
    if ballPosition[0] == 1 and (batY - 1) <= ballPosition[1] <= (batY +1): 
       ballVelocity[0] = -ballVelocity[0]
       if numBlocks <= 0:
           newBlocks()
    if ballPosition[0] == 0:
        sense.show_message("L !" )
    if ballPosition[0] < 7 and blocks[ballPosition[1]][ballPosition[0]+ ballVelocity[0]] != b:
        blocks[ballPosition[1]][ballPosition[0]+ ballVelocity[0]] = b
        numBlocks -= 1
        print(str(numBlocks))
        ballVelocity[0] = -ballVelocity[0]
    if 0 < ballPosition[1] < 7 and blocks[ballPosition[1] + ballVelocity[1]][ballPosition[0]] != b:
        blocks[ballPosition[1] +  ballVelocity[1]][ballPosition[0]] = b
        numBlocks -= 1
        print(str(numBlocks))
        ballVelocity[1] = -ballVelocity[1]
    elif ballPosition[0] < 7 and 0 < ballPosition[1] < 7 and blocks[ballPosition[1] + ballVelocity[1]][ballPosition[0] + ballVelocity[0]] != b:
        blocks[ballPosition[1] + ballVelocity[1]][ballPosition[0] + ballVelocity[0]] = b
        numBlocks -= 1
        print(str(numBlocks))
        ballVelocity[1] = -ballVelocity[1]
        ballVelocity[0] = -ballVelocity[0]
    
# Main -----------------------------
numBlocks = 0
newBlocks()
sense.stick.direction_up = moveUp
sense.stick.direction_down = moveDown
while True:
    sense.clear(0, 0, 0)
    drawBlocks()
    drawBat()
    drawBall()
    sleep(0.2)