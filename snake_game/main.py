'''Importing pygame'''
import pygame
from pygame.locals import * # from pygame.locals importing "K_UP", etc and "import *" allows you to directly "QUIT"

class Snake: # making blue print for the snake
    def __init__(self, parent_screeen): # initializing parent_screen bascially the screen
        self.parent_screen = parent_screeen # assinging parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert() # assining block to an image
        self.x = 100 # assigning x to 100
        self.y = 100 # assigning y to 100
        
    def draw(self): # defining draw 
        self.parent_screen.fill((235, 52, 207)) # filling the parent screen with color pink
        self.parent_screen.blit(self.block, (self.x, self.y)) #drawing the block image at x,100 and y,100
        pygame.display.flip() # update entire screen with whatever is drawn on parent_screen

    def move_left(self): #def move_left
        self.x -= 10 # left arrow moves x -10
        self.draw() # using draw function to draw new position
    
    def move_right(self): # defining move_right
        self.x += 10 # right arrow moves x +10
        self.draw() # using draw function to draw new position
    
    def move_up(self): # defining move_up
        self.y -= 10 # up arrow moves y -10
        self.draw() # using draw function to draw new position

    def move_down(self): # defining move_down
        self.y += 10 # down arrrow move y +10
        self.draw() # using draw function to draw new position

class Game: #making blue print for Game
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500)) # assigning surface to a window 500 x 500 pixels
        self.surface.fill((235, 52, 207)) # filling the window with color which is pink
        self.snake = Snake(self.surface) # assigning snake to the snake class then passed onto the surface
        self.snake.draw() # drawing the snake onto the surface (window)

    def run(self): #defining run
        running = True # assigning running to true

        while running: # creating loop
            for event in pygame.event.get(): # fetching all events in pygame
                if event.type == KEYDOWN: # checking key type
                    if event.key == K_ESCAPE: # if the ESC key is pressed:
                        running = False #game return false/ browser will be closed

                    if event.key == K_LEFT: # if left arrow clicked:
                        self.snake.move_left() # snake moves left

                    if event.key == K_RIGHT: # if right arrow is clicked:
                        self.snake.move_right() # snake moves right

                    if event.key == K_UP: # if up arrow is pushed:
                        self.snake.move_up() # snake moves up

                    if event.key == K_DOWN: # if down arrow is clicked:
                        self.snake.move_down() # snake moves down

                elif event.type == QUIT: # If quit is pushed:
                    running = False # game returns false, then closes


if __name__ == "__main__":
    game = Game()
    game.run()





    