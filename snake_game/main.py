'''Importing pygame'''
import pygame
from pygame.locals import * # from pygame.locals importing "K_UP", etc and "import *" allows you to directly "QUIT"
import time # importing time
import random # importing random

size = 40 # assigning size to 40 so the body of thee snake is 40 pizels apart
main_screen = (238, 148, 199) # assigning main_screen to the color of the screen

# TODO:
class Strawberry: #create strawberry class
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/strawberry.jpg").convert() # loading image into game
        self.parent_screen = parent_screen # creating parent screeen
        self.x = size * 3 # creating x for strawberry
        self.y = size * 3 # creating y for strawberry


    def draw(self): # creatring a function to draw the starwberry
        self.parent_screen.blit(self.image, (self.x, self.y)) #drawing the block image at x,100 and y,100
        pygame.display.flip() # update the display surface to the screen

    def move(self):
        self.x = random.randint(0, 25) * size # divide screen size x=1000 by 40 and got 25 * size so it doesn't go out the window
        self.y = random.randint(0, 20) * size # divide screen size y=800 by 40 and got 20 * size so doesn't go out the window



class Snake: # making blue print for the snake
    def __init__(self, parent_screen, length): # initializing parent_screen bascially the screen
        self.parent_screen = parent_screen # assinging parent_screen
        self.image = pygame.image.load("resources/block.jpg").convert() # assigning image to block.jpg
        self.direction = 'down' # assigning the snake to auotmatically move down when game is started

        self.length = length # assigning length
        self.x = [40] * length # assigning x of snake to 40*length
        self.y = [40] * length # assigning y of snake to 40*length

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self): #def move_left
        self.direction = 'left'
    
    def move_right(self): # defining move_right
        self.direction = 'right'
    
    def move_up(self): # defining move_up
        self.direction = 'up'

    def move_down(self): # defining move_down
        self.direction = 'down'

    def walk(self): # creating a function so the snake "walks"

        for i in range (self.length-1,0, -1): # creating a loop so the blcoks after the snake head follows the snake head
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left': # if direction is left, the snake will move left 40 pixels
            self.x[0] -= size
        if self.direction == 'right': # if direction is right, the snake will move right 40 pixels
            self.x[0] += size
        if self.direction == 'up': # if direction is up, the snake will move up 40 pixels
            self.y[0] -= size
        if self.direction == 'down': # if direction is down, the snake will move down 40 pixels
            self.y[0] += size

        self.draw() # draw

    def draw(self): # defining draw
        self.parent_screen.fill((main_screen)) # filling the parent screen with color pink
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i])) #drawing the block image at x,100 and y,100
        pygame.display.flip() # update entire screen with whatever is drawn on parent_screen


class Game: # making class for Game
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,800)) # assigning surface to a window 100 x 800 pixels
        self.snake = Snake(self.surface, 1) # assigning snake to the snake class then passed onto the surface, making the snake 6 block long
        self.snake.draw() # drawing the snake onto the surface (window)
        self.strawberry = Strawberry(self.surface) # adding strawberry on game screen
        self.strawberry.draw() # drawing strawberry on screen

    def is_collision(self, x1, y1, x2, y2): # defining collsion using x,y,1,2
        if x1 >= x2 and x1 < x2 + size: # if x1 greater than x2 plus size and x1 less than x2 plus size
            if y1 >= y2 and y1 < y2 + size: # if y1 greater than y2 plus size and y1 less than y2 plus size
                return True # then return true
            
        return False # or return false

    def play(self): # defining play so all pieces go onto the screen
        self.snake.walk()
        self.strawberry.draw()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.strawberry.x, self.strawberry.y): # if collion occurs sanke.x[0]/snake.y[0] with strawberryx,y
            self.snake.increase_length() # increaseing length if there is a collision with snake and strawberry
            self.strawberry.move() # then move straberry


    def run(self): # defining run
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

            self.play() # using function def play(self):

            time.sleep(.2) # setting speed of snake to .2 seconds


if __name__ == "__main__":
    game = Game()
    game.run()
