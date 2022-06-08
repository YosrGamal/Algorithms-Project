import pygame
import time
from collections import deque
from queue import PriorityQueue
def setMaze():
    global maze
    maze = [
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0],
     [0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0],
     [0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0],
     [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0],
     [0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0],
     [0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0],
     [0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0],
     [0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0],
     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0],
     [0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
     [0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0],
     [0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0],
     [0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0],
     [0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0],
     [0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0],
     [0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0],
     [0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
     [0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0],
     [0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0],
     [0,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
     [0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0],
     [0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0],
     [0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0],
     [0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0],
     [0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0],
     [0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0],
     [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,3,0,1,0,1,0],
     [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0],
     [0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0],
     [0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
     [0,4,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    global mazeRealCost
    mazeRealCost =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 155, 37, 101, 27, 104, 16, 115, 0, 99, 0, 33, 0, 76, 46, 44, 23, 95, 17, 185, 155, 120, 188, 73, 0, 200, 44, 108, 0, 31, 94, 25, 15, 53, 0, 75, 0],
     [0, 144, 0, 0, 0, 0, 0, 0, 0, 94, 0, 125, 0, 0, 0, 9, 0, 66, 0, 0, 0, 192, 0, 0, 0, 81, 0, 0, 0, 0, 0, 0, 0, 7, 0, 172, 0], 
     [0, 46, 96, 179, 85, 53, 5, 14, 0, 20, 145, 0, 138, 187, 2, 186, 0, 62, 0, 102, 71, 13, 4, 7, 0, 63, 10, 197, 18, 80, 0, 59, 0, 77, 169, 67, 0],
     [0, 0, 0, 0, 0, 28, 0, 0, 0, 0, 0, 67, 0, 0, 0, 92, 0, 155, 0, 137, 0, 62, 0, 0, 0, 19, 0, 0, 0, 0, 0, 149, 0, 56, 0, 0, 0], 
     [0, 3, 36, 77, 0, 66, 0, 79, 0, 4, 0, 14, 191, 160, 0, 46, 0, 192, 0, 27, 0, 167, 189, 0, 0, 95, 0, 197, 137, 110, 0, 183, 0, 46, 30, 152, 0], 
     [0, 96, 0, 0, 0, 28, 0, 126, 0, 51, 0, 121, 0, 0, 0, 36, 0, 0, 0, 0, 0, 159, 0, 0, 0, 156, 0, 69, 0, 0, 0, 172, 0, 0, 0, 123, 0], 
     [0, 164, 57, 27, 79, 108, 41, 129, 0, 138, 170, 55, 85, 37, 0, 158, 33, 10, 0, 193, 191, 178, 0, 82, 147, 19, 193, 198, 0, 1, 0, 117, 0, 105, 195, 154, 0], 
     [0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 190, 0, 0, 0, 0, 0, 0, 0, 175, 0, 0, 0, 182, 0, 0, 0, 110, 0, 128, 0, 120, 0, 135, 0], 
     [0, 119, 164, 78, 63, 79, 28, 93, 29, 57, 70, 126, 60, 92, 0, 37, 24, 193, 80, 72, 29, 34, 0, 33, 0, 176, 47, 110, 0, 95, 191, 59, 94, 43, 0, 180, 0], 
     [0, 3, 0, 97, 0, 0, 0, 0, 0, 69, 0, 32, 0, 0, 0, 17, 0, 148, 0, 137, 0, 0, 0, 61, 0, 78, 0, 0, 0, 168, 0, 0, 0, 74, 0, 90, 0], 
     [0, 29, 0, 2, 0, 109, 60, 48, 161, 80, 0, 109, 0, 150, 0, 26, 0, 109, 0, 133, 8, 95, 100, 175, 0, 19, 27, 171, 0, 129, 0, 43, 0, 164, 0, 53, 0],
     [0, 80, 0, 57, 0, 183, 0, 0, 0, 0, 0, 0, 0, 155, 0, 95, 0, 0, 0, 0, 0, 0, 0, 0, 0, 157, 0, 0, 0, 173, 0, 5, 0, 0, 0, 119, 0], 
     [0, 44, 0, 179, 0, 161, 0, 125, 169, 39, 103, 105, 0, 197, 97, 124, 0, 151, 6, 15, 56, 103, 0, 45, 5, 8, 131, 47, 0, 76, 82, 60, 0, 64, 138, 93, 0], 
     [0, 0, 0, 11, 0, 0, 0, 89, 0, 198, 0, 0, 0, 0, 0, 56, 0, 0, 0, 0, 0, 100, 0, 0, 0, 183, 0, 0, 0, 185, 0, 0, 0, 0, 0, 170, 0], 
     [0, 107, 23, 2, 147, 120, 0, 67, 0, 138, 0, 55, 117, 62, 3, 192, 0, 184, 0, 163, 1, 112, 88, 85, 0, 58, 0, 164, 108, 94, 0, 169, 0, 169, 0, 127, 0],
     [0, 106, 0, 98, 0, 57, 0, 19, 0, 116, 0, 0, 0, 174, 0, 0, 0, 137, 0, 0, 0, 181, 0, 0, 0, 22, 0, 123, 0, 28, 0, 111, 0, 166, 0, 15, 0], 
     [0, 154, 0, 167, 0, 73, 0, 91, 0, 14, 61, 60, 177, 120, 41, 132, 166, 6, 171, 112, 9, 143, 149, 89, 138, 9, 0, 106, 0, 13, 0, 166, 142, 184, 187, 51, 0], 
     [0, 0, 0, 172, 0, 0, 0, 0, 0, 0, 0, 142, 0, 119, 0, 186, 0, 0, 0, 0, 0, 167, 0, 0, 0, 193, 0, 33, 0, 0, 0, 194, 0, 0, 0, 0, 0],
     [0, 57, 13, 100, 181, 119, 180, 110, 0, 99, 0, 90, 0, 164, 0, 86, 197, 76, 82, 47, 0, 78, 175, 115, 0, 83, 18, 176, 188, 92, 0, 186, 0, 165, 159, 184, 0], 
     [0, 0, 0, 0, 0, 18, 0, 120, 0, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 164, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 124, 0, 177, 0, 0, 0],
     [0, 97, 113, 86, 0, 51, 0, 17, 145, 120, 137, 148, 107, 145, 188, 83, 108, 30, 0, 73, 0, 5, 176, 113, 180, 112, 0, 138, 88, 195, 0, 200, 0, 171, 26, 102, 0], 
     [0, 3, 0, 0, 0, 159, 0, 0, 0, 0, 0, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 132, 0, 0, 0, 0, 0, 186, 0, 183, 0, 127, 0, 0, 0, 126, 0],
     [0, 63, 0, 144, 68, 148, 0, 59, 83, 36, 184, 59, 84, 0, 163, 61, 134, 62, 25, 102, 154, 165, 0, 41, 15, 164, 98, 8, 0, 31, 112, 11, 188, 169, 1, 200, 0], 
     [0, 137, 0, 13, 0, 115, 0, 0, 0, 0, 0, 117, 0, 0, 0, 35, 0, 139, 0, 125, 0, 18, 0, 68, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 6, 0, 186, 0, 130, 71, 2, 0, 158, 78, 191, 72, 161, 0, 75, 0, 76, 0, 18, 0, 55, 137, 179, 95, 193, 40, 192, 0, 168, 143, 12, 0, 67, 0, 198, 0],
     [0, 15, 0, 12, 0, 0, 0, 109, 0, 0, 0, 97, 0, 112, 0, 3, 0, 104, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 200, 0, 163, 0, 114, 0], 
     [0, 51, 0, 181, 125, 99, 0, 198, 0, 74, 72, 45, 0, 28, 0, 182, 0, 12, 135, 62, 0, 21, 0, 122, 123, 10, 0, 133, 0, 0, 0, 158, 173, 137, 149, 151, 0],
     [0, 72, 0, 0, 0, 103, 0, 0, 0, 159, 0, 0, 0, 0, 0, 108, 0, 0, 0, 178, 0, 95, 0, 23, 0, 0, 0, 0, 0, 184, 0, 22, 0, 0, 0, 0, 0], 
     [0, 129, 177, 73, 116, 81, 50, 107, 0, 96, 130, 70, 0, 51, 13, 47, 182, 176, 0, 124, 0, 24, 175, 125, 88, 168, 0, 121, 26, 44, 0, 182, 0, 49, 57, 102, 0],
     [0, 0, 0, 27, 0, 159, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 195, 0, 0, 0, 103, 0, 0, 0, 196, 0, 82, 0, 0, 0, 120, 0, 199, 0, 0, 0],
     [0, 74, 0, 47, 0, 1, 0, 80, 0, 27, 0, 2, 0, 26, 0, 19, 32, 172, 48, 8, 0, 29, 0, 32, 72, 48, 0, 142, 0, 142, 15, 3, 0, 182, 0, 171, 0],
     [0, 170, 0, 110, 0, 3, 0, 183, 0, 181, 0, 56, 0, 92, 0, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 107, 0, 9, 0, 129, 0, 183, 0, 97, 0, 40, 0],
     [0, 51, 129, 103, 33, 98, 129, 5, 0, 168, 197, 94, 0, 169, 147, 184, 48, 198, 105, 71, 77, 163, 127, 193, 200, 59, 153, 96, 150, 132, 0, 114, 88, 110, 160, 1, 0],
     [0, 96, 0, 33, 0, 17, 0, 133, 0, 0, 0, 83, 0, 0, 0, 37, 0, 0, 0, 0, 0, 0, 0, 66, 0, 0, 0, 62, 0, 0, 0, 41, 0, 0, 0, 163, 0],
     [0, 4, 0, 130, 0, 77, 0, 117, 121, 100, 199, 36, 199, 125, 0, 133, 12, 100, 0, 136, 102, 188, 127, 154, 39, 127, 0, 43, 166, 157, 0, 42, 0, 93, 20, 7, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
#VARIABLES
square = 25
maplimit = 35
setMaze()
(width, height) = (len(maze) * square, len(maze[0]) * square)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
Solu_1 = {}
startx = 0
starty = 0 
endx = 0
endy = 0
path = []
explored = [] 
frontier = []
running =True

def wall(i,j):
    pygame.draw.rect(screen,(0,0,255),(j*square,i*square,square,square))
def food(i,j):
    pygame.draw.circle(screen,(255,255,255),(j*square+square//2, i * square+square//2),square//4)
def pacPath(i,j):
    pygame.draw.rect(screen,(0,0,0),(j*square,i*square,square,square))
def pacman(i,j):
    pygame.draw.circle(screen, (255,255,0),(j*square+square//2, i * square+square//2),square//4)
def greenTrack(i,j):
    pygame.draw.rect(screen,(0,255,0),(j*square,i*square,square,square))
def redTrack(i,j):
    pygame.draw.rect(screen,(255,0,0),(j*square,i*square,square,square))
def renderBoard():
    global startx, starty,endx, endy
    screen.fill((0,0,0))
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            element = maze[i][j]
            if element == 0:
                wall(i,j)
            elif element == 4:
                path.append((j,i))
                endx = j
                endy = i
                food(i,j)
            elif element == 1:
                    pacPath(i,j)
                    path.append((j,i))
            elif element == 3:
                startx = j
                starty = i
                pacman(i,j)
            elif element == 9:
                path.append((j,i))
                greenTrack(i,j)
            elif element == 10:
                path.append((j,i))
                redTrack(i,j)
    pygame.display.update()
def move(x,y):
    maze[y][x] = 10



def DFS(x,y):
    frontier.append((x,y))
    Solu_1[x,y] = x,y
    while len(frontier) > 0:
        time.sleep(0)
        current = (x,y)
        if (x - 1,y) in path and (x - 1,y) not in explored:
            left = (x - 1,y)
            Solu_1[left] = x,y
            frontier.append(left)
        if (x,y + 1) in path and (x,y + 1) not in explored:
            down = (x,y+1)
            Solu_1[down] = x,y
            frontier.append(down)
        if (x + 1,y) in path and (x+1,y) not in explored:
            right = (x + 1,y)
            Solu_1[right] = x,y
            frontier.append(right)
        if (x,y-1) in path and (x,y-1) not in explored:
            up = (x,y-1)
            Solu_1[up] = x,y
            frontier.append(up)
        x,y = frontier.pop()
        maze[y][x] = 9
        explored.append(current)
        if (x,y) == (endx,endy):
            return
        renderBoard()



def UCS(x,y): 
    frontier = PriorityQueue()
    explored = set()
    frontier.put((mazeRealCost[y][x],(x,y)))
    Solu_1[x,y] = x,y
    while not frontier.empty():
        time.sleep(0)
        node = frontier.get()
        Cost,Location=node
        if(Location[0] - 1,Location[1]) in path and (Location[0]-1,Location[1]) not in explored:
            left = (Location[0]-1,Location[1])
            Solu_1[left] = Location[0],Location[1]
            maze[left[1]][left[0]] = 9
            frontier.put((Cost+mazeRealCost[Location[1]][Location[0]-1],(left)))
            explored.add((Location[0]-1,Location[1]))
        if(Location[0],Location[1]-1) in path and (Location[0],Location[1]-1) not in explored:
            up = (Location[0],Location[1]-1)
            Solu_1[up] = Location[0],Location[1]
            maze[up[1]][up[0]] = 9
            frontier.put((Cost+mazeRealCost[Location[1]-1][Location[0]],(up)))
            explored.add((Location[0],Location[1]-1))
        if(Location[0]+1,Location[1]) in path and (Location[0]+1,Location[1]) not in explored:
            right = (Location[0]+1,Location[1])
            Solu_1[right] = Location[0],Location[1]
            maze[right[1]][right[0]] = 9
            frontier.put((Cost+mazeRealCost[Location[1]][Location[0]+1],(right)))
            explored.add((Location[0]+1,Location[1]))
        if (Location[0],Location[1]+1) in path and (Location[0],Location[1]+1) not in explored:
            down = (Location[0],Location[1]+1)
            Solu_1[down] = Location[0],Location[1]
            maze[down[1]][down[0]] = 9
            frontier.put((Cost+mazeRealCost[Location[1]+1][Location[0]],(down)))
            explored.add((Location[0],Location[1]+1))
        if (Location[0],Location[1]) == (endx,endy):
            return
        renderBoard() 

def gbfs(x,y):
    frontier = PriorityQueue()
    explored = set()
    frontier.put((heursiticdata[y][x],(x,y)))
    Solu_1[x,y] = x,y
    while not frontier.empty():
        time.sleep(0)
        node = frontier.get()
        Cost,Location=node
        if(Location[0] - 1,Location[1]) in path and (Location[0]-1,Location[1]) not in explored:
            left = (Location[0]-1,Location[1])
            Solu_1[left] = Location[0],Location[1]
            maze[left[1]][left[0]] = 9
            frontier.put((heursiticdata[Location[1]][Location[0]-1],(left)))
            explored.add((Location[0]-1,Location[1]))
        if(Location[0],Location[1]-1) in path and (Location[0],Location[1]-1) not in explored:
            up = (Location[0],Location[1]-1)
            Solu_1[up] = Location[0],Location[1]
            maze[up[1]][up[0]] = 9
            frontier.put((heursiticdata[Location[1]-1][Location[0]],(up)))
            explored.add((Location[0],Location[1]-1))
        if(Location[0]+1,Location[1]) in path and (Location[0]+1,Location[1]) not in explored:
            right = (Location[0]+1,Location[1])
            Solu_1[right] = Location[0],Location[1]
            maze[right[1]][right[0]] = 9
            frontier.put((heursiticdata[Location[1]][Location[0]+1],(right)))
            explored.add((Location[0]+1,Location[1]))
        if (Location[0],Location[1]+1) in path and (Location[0],Location[1]+1) not in explored:
            down = (Location[0],Location[1]+1)
            Solu_1[down] = Location[0],Location[1]
            maze[down[1]][down[0]] = 9
            frontier.put((heursiticdata[Location[1]+1][Location[0]],(down)))
            explored.add((Location[0],Location[1]+1))
        if (Location[0],Location[1]) == (endx,endy):
            return
        renderBoard()
def AStar(x,y):
    frontier = PriorityQueue()
    explored = set()
    frontier.put((mazeRealCost[y][x]+heursiticdata[y][x],(x,y)))
    Solu_1[x,y] = x,y
    while not frontier.empty():
        time.sleep(0)
        node = frontier.get()
        Cost,Location=node
        if(Location[0] - 1,Location[1]) in path and (Location[0]-1,Location[1]) not in explored:
            left = (Location[0]-1,Location[1])
            Solu_1[left] = Location[0],Location[1]
            maze[left[1]][left[0]] = 9
            frontier.put((Cost+mazeRealCost[y][x]+heursiticdata[Location[1]][Location[0]-1],(left)))
            explored.add((Location[0]-1,Location[1]))
        if(Location[0],Location[1]-1) in path and (Location[0],Location[1]-1) not in explored:
            up = (Location[0],Location[1]-1)
            Solu_1[up] = Location[0],Location[1]
            maze[up[1]][up[0]] = 9
            frontier.put((Cost+mazeRealCost[y][x]+heursiticdata[Location[1]-1][Location[0]],(up)))
            explored.add((Location[0],Location[1]-1))
        if(Location[0]+1,Location[1]) in path and (Location[0]+1,Location[1]) not in explored:
            right = (Location[0]+1,Location[1])
            Solu_1[right] = Location[0],Location[1]
            maze[right[1]][right[0]] = 9
            frontier.put((Cost+mazeRealCost[y][x]+heursiticdata[Location[1]][Location[0]+1],(right)))
            explored.add((Location[0]+1,Location[1]))
        if (Location[0],Location[1]+1) in path and (Location[0],Location[1]+1) not in explored:
            down = (Location[0],Location[1]+1)
            Solu_1[down] = Location[0],Location[1]
            maze[down[1]][down[0]] = 9
            frontier.put((Cost+mazeRealCost[y][x]+heursiticdata[Location[1]+1][Location[0]],(down)))
            explored.add((Location[0],Location[1]+1))
        if (Location[0],Location[1]) == (endx,endy):
            return
        renderBoard()

def backRoute(x,y):
    global cost
    global score
    while(x,y) != (startx,starty):
        x,y = Solu_1[x,y]
        score+=mazeRealCost[x][y]
        move(x,y)
        time.sleep(0)
        renderBoard()
        cost += 1



####################################################################
from collections import defaultdict

class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")
####################################################################

g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()    

    #Remove the comment of desired algo

renderBoard()
#BFS(startx,starty)
DFS(startx,starty)
#UCS(startx,starty)
#gbfs(startx,starty)
#AStar(startx,starty)
setMaze()
renderBoard()
cost = 0
score=0
backRoute(endx,endy)
print(cost)
print(score)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False