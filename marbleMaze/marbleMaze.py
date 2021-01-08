from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()


o = sense.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]
print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))

r = (255, 0, 0)
b = (0,0,0)
w = (255,255,255)
g = (0, 255, 0)
bl = (0, 0, 255)
yl = (255,255,0)

x = 1
y = 1

score = 0
gameOver = False

maze1 = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,bl,r],
        [r,r,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,yl,bl,r,g,r,b,r],
        [r,r,r,r,r,r,r,r]]

maze1b = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,bl,r],
        [r,r,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,bl,r,g,b,b,r],
        [r,r,r,r,r,r,r,r]]

maze2 = [[r,r,r,r,r,r,r,r],
         [r,bl,b,r,b,bl,bl,r],
         [r,b,b,b,b,b,bl,r],
         [r,b,r,b,b,r,r,r],
         [r,b,r,r,b,bl,b,r],
         [r,b,r,b,b,r,b,r],
         [r,g,r,b,b,r,b,r],
         [r,r,r,r,r,r,r,r]]

maze3 = [[r,r,r,r,r,r,r,r],
         [r,g,r,r,r,r,r,r],
         [r,b,r,b,b,b,b,r],
         [r,b,r,b,bl,r,b,r],
         [r,b,b,b,bl,b,b,r],
         [r,bl,bl,r,bl,b,r,r],
         [r,b,b,b,b,b,r,r],
         [r,r,r,r,r,r,r,r]]

maze = maze1

def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 0 < pitch < 179 and x != 0:
        new_x -= 1
    elif 181 < pitch < 357 and x != 7:
        new_x += 1
    if 0 < roll < 179 and y != 7:
        new_y += 1
    elif 181 < roll < 359 and y != 0:
        new_y -= 1
    new_x, new_y = check_wall(x,y,new_x,new_y)
    return new_x, new_y

def check_wall(x,y,new_x,new_y):
    if (maze[new_y][new_x] != r):
        return new_x, new_y
    elif (maze[new_y][x] != r):
        return x, new_y
    elif (maze[y][new_x] != r):
        return new_x, y
    else:
        return x, y

while not gameOver:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    x,y = move_marble(pitch, roll, x, y)
    if (maze[y][x] == yl):
        maze = maze1b
        sense.set_pixels(sum(maze,[]))
    if (maze[y][x] == g):
        score += 1
        print("Score: " + str(score))
        if (maze == maze1b):
            maze = maze2
        elif (maze == maze2):
            maze = maze3
        elif (maze == maze3):
            maze = maze1
    if (maze[y][x] == bl):
        print("You Lose, Final Score: " + str(score))
        sense.show_message("You Lose, Final score: " + str(score))
        break
    maze[y][x] = w
    sense.set_pixels(sum(maze,[]))
    sleep(0.2)
    maze[y][x] = b