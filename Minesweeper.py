"""
Program Name: Minesweeper
Author: Moeez Sohail
Program Description: This program is a simple Minesweeper game where the user can click different cells 
and they will be told how many bombs are surrounding that cell. The goal of the game is to avoid the
bombs, however, if a bomb is clicked, the grid will be solved. 
Technologies: Python and Pygame
"""

import pygame
import random
 
# Defining constants 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (160, 160, 160) # Zero bombs
PURPLE = (238, 130, 238) # One bomb
BLUE = (0, 255, 255) # Two bombs
GREEN = (0, 255, 0) # Three bombs
YELLOW = (255, 255, 0) # Four bombs
ORANGE = (255, 165, 0) # Five bombs
RED = (255, 0, 0) # Bomb
WIDTH = 40 # Square Width
HEIGHT = 40 # Square Height
MARGIN = 10 # Margin between each square
BOMBS = 20 # Number of bombs
GRID_SIZE = 10 # Height and width of grid

# Creating 10x10 grids (one for the values and one for whether a cell has been discovered)
grid = [[0 for row in range(GRID_SIZE)] for col in range(GRID_SIZE)]
val = [[0 for row in range(GRID_SIZE)] for col in range(GRID_SIZE)]

# Function that generates mines in random locations
def generateMines():
    global val
    for num in range(BOMBS):
        x = random.randint(0,GRID_SIZE - 1)
        y = random.randint(0,GRID_SIZE - 1)
        val[x][y] = 'X'

# Function that determines the number of mines surrounding each cell      
def calculateMines():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if(val[row][col] != 'X'):
                if((row - 1) >= 0 and (col - 1) >= 0): # top left
                    if(val[row-1][col-1] == 'X'):
                        val[row][col] += 1
                if((row - 1) >= 0): # top middle
                    if(val[row-1][col] == 'X'): 
                        val[row][col] += 1
                if((row - 1) >= 0 and (col + 1) < GRID_SIZE): # top left
                    if(val[row-1][col+1] == 'X'):
                        val[row][col] += 1
                if((col - 1) >= 0): # middle left
                    if(val[row][col-1] == 'X'):
                        val[row][col] += 1
                if((col + 1) < GRID_SIZE): # middle right
                    if(val[row][col+1] == 'X'):
                        val[row][col] += 1
                if((row + 1) < GRID_SIZE and (col - 1) >= 0): # bottom left
                    if(val[row+1][col-1] == 'X'):
                        val[row][col] += 1
                if((row + 1) < GRID_SIZE): # bottom middle
                    if(val[row+1][col] == 'X'): 
                        val[row][col] += 1
                if((row + 1) < GRID_SIZE and (col + 1) < GRID_SIZE): # bottom right
                    if(val[row+1][col+1] == 'X'):
                        val[row][col] += 1

# Function that solves the grid by setting each cell to discovered
def setDiscovered():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            grid[row][col] = 1

# Main function that runs the program
def main():
    global grid, val
    pygame.init()

    # Set window size & title
    WINDOW_SIZE = [650, 515]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Minesweeper")

    # Setting up the grid
    generateMines()
    calculateMines()
    firstBomb = True

    # Creating a key that explains the colors
    font = pygame.font.SysFont(None, 50)
    font.set_underline(True)
    key = font.render('Key', True, WHITE)
    font.set_underline(False)
    zero = font.render('Zero', True, GREY)
    one = font.render('One', True, PURPLE)
    two = font.render('Two', True, BLUE)
    three = font.render('Three', True, GREEN)
    four = font.render('Four', True, YELLOW)
    five = font.render('Five', True, ORANGE)
    bomb = font.render('Bomb', True, RED)
    smallFont = pygame.font.SysFont(None, 30)
    loss = smallFont.render('You lost!', True, WHITE)
    reset = smallFont.render('Reset', True, BLACK)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # X was clicked
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: # Mouse was clicked
                mouse = pygame.mouse.get_pos()
                col = mouse[0] // (WIDTH + MARGIN)
                row = mouse[1] // (HEIGHT + MARGIN)
                if(row < GRID_SIZE and row >= 0 and col < GRID_SIZE and col >= 0): # Cell on grid was clicked
                    grid[row][col] = 1
                elif(530 <= mouse[0] <= 610 and 450 <= mouse[1] <= 490): # Reset was clicked
                    grid = [[0 for row in range(GRID_SIZE)] for col in range(GRID_SIZE)]
                    val = [[0 for row in range(GRID_SIZE)] for col in range(GRID_SIZE)]
                    generateMines()
                    calculateMines()
                    firstBomb = True
    
        # Output key
        screen.fill(BLACK)
        screen.blit(key, (535, 15))
        screen.blit(zero, (530, 60))
        screen.blit(one, (535, 105))
        screen.blit(two, (535, 150))
        screen.blit(three, (522, 195))
        screen.blit(four, (532, 240))
        screen.blit(five, (532, 285))
        screen.blit(bomb, (525, 330))
        pygame.draw.rect(screen, WHITE, [530,450,80,40])
        screen.blit(reset, (540, 465))

        # Output grid
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                color = WHITE
                if grid[row][col] == 1:
                    num = val[row][col]
                    if num == 0:
                        color = GREY
                    if num == 1:
                        color = PURPLE
                    elif num == 2:
                        color = BLUE
                    elif num == 3:
                        color = GREEN
                    elif num == 4:
                        color = YELLOW
                    elif num == 5:
                        color = ORANGE
                    elif num == 'X':
                        color = RED
                        screen.blit(loss, (530, 400))
                        if(firstBomb):
                            setDiscovered()
                            firstBomb = False
                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
    
        pygame.display.flip()

    pygame.quit()

main()