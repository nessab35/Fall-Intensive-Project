'''Importing pygame'''
import pygame
from pygame.locals import * # from pygame.locals importing "K_UP", etc and "import *" allows you to directly "QUIT"
import time

size = 40 # assigning size to 40 so the body of thee snake is 40 pizels apart
main_screen = (238, 148, 199) # assigning main_screen to the color of the screen

# TODO:
class Strawberry: #create strawberry class
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/strawberry.jpg").convert()
        self.parent_screen = parent_screen
        self.x = size * 3
        self.y = size * 3


    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y)) #drawing the block image at x,100 and y,100
        pygame.display.flip()



class Snake: # making blue print for the snake
    def __init__(self, parent_screen, length): # initializing parent_screen bascially the screen
        self.length = length
        self.parent_screen = parent_screen # assinging parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert() # assining block to an image
        self.x = [size] * length # assigning x to 100
        self.y = [size] * length # assigning y to 100
        self.direction = 'down'

    def move_left(self): #def move_left
        self.direction = 'left'
    
    def move_right(self): # defining move_right
        self.direction = 'right'
    
    def move_up(self): # defining move_up
        self.direction = 'up'

    def move_down(self): # defining move_down
        self.direction = 'down'

    def walk(self): # creating a function so the length of the snake follows behind the head

        for i in range (self.length-1,0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size
        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size

        self.draw()

    def draw(self): # defining draw 
        self.parent_screen.fill((main_screen)) # filling the parent screen with color pink
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i])) #drawing the block image at x,100 and y,100
        pygame.display.flip() # update entire screen with whatever is drawn on parent_screen


class Game: #making blue print for Game
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,800)) # assigning surface to a window 100 x 800 pixels
        self.snake = Snake(self.surface, 6) # assigning snake to the snake class then passed onto the surface, making the snake 6 block long
        self.snake.draw() # drawing the snake onto the surface (window)
        self.strawberry = Strawberry(self.surface)
        self.strawberry.draw()


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

            self.snake.walk()
            self.strawberry.draw()

            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()
