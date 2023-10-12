'''Importing pygame'''
import pygame
from pygame.locals import * # from pygame.locals importing "K_UP", etc and "import *" allows you to directly "QUIT"
import time # importing time
import random # importing random

size = 40 # assigning size to 40 so the body of the snake is 40 pizels apart
pink = (238, 148, 199) # assinging pink to rgb color
black = (0, 0, 0) # assigning black to rgb color
screen_size = (1000,800) # assinging screen size


class Strawberry: #create strawberry class
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/strawberry.jpg").convert() # loading image into game
        self.parent_screen = parent_screen # creating parent screeen
        self.x = size * 3 # creating x for strawberry
        self.y = size * 3 # creating y for strawberry

    # creating function to draw strawberry on to screen
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y)) #drawing the block image at x,100 and y,100
        pygame.display.flip() # update the display surface to the screen

    # creating function to move the strawberry
    def move(self):
        self.x = random.randint(0, 24) * size # divide screen size x=1000 by 40 and got 25 * size so it doesn't go out the window restrict it 1 lower=24
        self.y = random.randint(0, 19) * size # divide screen size y=800 by 40 and got 20 * size so doesn't go out the window restrict it 1 lower=19



# making class for the snake
class Snake:
    # initializing parent_screen bascially the screen and length
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen # assinging parent_screen
        self.image = pygame.image.load("resources/block.jpg").convert() # assigning image to block.jpg
        self.direction = 'down' # assigning the snake to auotmatically move down when game is started

        self.length = length # assigning length
        self.x = [40] * length # assigning x of snake to 40*length
        self.y = [40] * length # assigning y of snake to 40*length

    # defining increase length
    def increase_length(self):
        self.length += 1 # increase length by 1
        self.x.append(-1) # append x -1
        self.y.append(-1) # append y -1

    # def move_left
    def move_left(self):
        self.direction = 'left'
    
    # defining move_right
    def move_right(self):
        self.direction = 'right'
    
    # defining move_up
    def move_up(self):
        self.direction = 'up'

    # defining move_down
    def move_down(self):
        self.direction = 'down'

    # creating a function so the snake "walks"
    def walk(self):
        # creating a loop so the blcoks after the snake head follows the snake head
        for i in range (self.length-1,0, -1):
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

    # defining draw
    def draw(self):
        self.parent_screen.fill((pink)) # filling the parent screen with color pink
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i])) #drawing the block image at x,100 and y,100
        pygame.display.flip() # update entire screen with whatever is drawn on parent_screen



# creating class for game
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake and Strawberry-Nessa Begay") # setting caption of window

        pygame.mixer.init()
        self.play_background_music() # playing background music
        self.surface = pygame.display.set_mode((screen_size)) # assigning surface to a window 100 x 800 pixels
        self.snake = Snake(self.surface, 1) # assigning snake to the snake class then passed onto the surface, making the snake 6 block long
        self.snake.draw() # drawing the snake onto the surface (window)
        self.strawberry = Strawberry(self.surface) # adding strawberry on game screen
        self.strawberry.draw() # drawing strawberry on screen

    # defining display_score
    def display_score(self):
        font = pygame.font.SysFont('timesnewroman', 30) # assinging font to certain font and size
        score = font.render(f"Score: {self.snake.length}", True, (black)) # displaying score with color
        self.surface.blit(score, (800,10)) # putting score on scren with position

    # defining collsion using x,y,1,2
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size: # if x1 greater than x2 plus size and x1 less than x2 plus size
            if y1 >= y2 and y1 < y2 + size: # if y1 greater than y2 plus size and y1 less than y2 plus size
                return True # then return true
            
        return False # or return false

    # defining background music
    def play_background_music(self):
        pygame.mixer.music.load("resources/bg_music_.mp3")  # loading backgroud song
        pygame.mixer.music.play() # playing the sound

    # defining function for play sound for ding and crash
    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"resources/{sound}.mp3") # assigning sound to play certain soud
        pygame.mixer.Sound.play(sound) # playing sound

    # defining play so all pieces go onto the screen
    def play(self):
        self.snake.walk()
        self.strawberry.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating strawberry
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.strawberry.x, self.strawberry.y):
            self.play_sound("eating")
            self.snake.increase_length() # increaseing length if there is a collision with snake and strawberry
            self.strawberry.move() # then move straberry

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise "Game over!"
        
        # snake goes out of bounds then game is over
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            self.play_sound("crash")
            raise "Game over!"
        
    # defining game over
    def show_game_over(self):
        self.surface.fill(black)
        font = pygame.font.SysFont('timesnewroman', 30)
        line_1 = font.render(f"Game Over! Your score is: {self.snake.length}", True, (pink))
        self.surface.blit(line_1, (200,300))
        line_2 = font.render("To play again, press ENTER. To exit press ESC!", True, (pink))
        self.surface.blit(line_2, (200, 350))

        pygame.display.flip() # display flip is used to display onto full screen

        pygame.mixer.music.pause()

    # defining reset
    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.strawberry = Strawberry(self.surface)

    # defining run
    def run(self):
        running = True # assigning running to true
        pause = False # setting pause to false until end of game

        # creating loop
        while running:
            for event in pygame.event.get(): # fetching all events in pygame
                if event.type == KEYDOWN: # checking key type
                    if event.key == K_ESCAPE: # if the ESC key is pressed:
                        running = False #game return false/ browser will be closed

                    if event.key == K_RETURN: # if enter/return is pushed
                        pygame.mixer.music.unpause()
                        pause = False #then the game restarts

                    if not pause:
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

            try:
                if not pause:
                    self.play() # using function def play(self):
            except Exception as e:
                print(f"Error: {e}")
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.1) # setting speed of snake to .25 seconds


if __name__ == "__main__":
    game = Game()
    game.run()
 