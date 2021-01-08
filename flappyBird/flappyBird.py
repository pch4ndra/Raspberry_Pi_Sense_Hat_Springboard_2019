from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)

x = 2
y = 0
gameOver = False
score = -2

matrix = [[blue for column in range(8)] for row in range(8)]

def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened

def genPipes(matrix):
    for row in matrix:
        row[-1] = green
    gap = randint(1,5)
    matrix[gap][-1] = blue
    matrix[gap - 1][-1] = blue
    matrix[gap + 1][-1] = blue
    return matrix

def movePipes(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i+1]
        row[-1]= blue
    return matrix

def drawAstronaut(event):
    global x
    global y
    global gameOver
    sense.set_pixel(x, y, blue)
    if event.action == "pressed":
        if event.direction == "up" and y > 0:
            y -= 1
    sense.set_pixel(x, y, yellow)
    if matrix[y][x] == green:
        gameOver = True
    
def checkCollision(matrix):
    global y
    return matrix[y][x] == green or y == 7

def gravity():
    global y
    y += 1
    
# Main ------------------------------
sense.stick.direction_any = drawAstronaut
while not gameOver:
    matrix = genPipes(matrix)
    if checkCollision(matrix):
        gameOver = True
    for i in range(6):
        if(i%2 == 0):
            matrix = movePipes(matrix)
        sense.set_pixels(flatten(matrix))
        gravity()
        if checkCollision(matrix):
            gameOver = True
            break
        sense.set_pixel(x, y, yellow)
        sleep(0.5)
    score += 1
    print("Score: " + str(score))
if score < 0:
    score = 0
sense.show_message("Score: " + str(score))
print("Score: " + str(score))