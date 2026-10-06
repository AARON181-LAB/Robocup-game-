import pygame as pg
import sys


#screen size
WIDTH = 1400
HEIGHT = 800
x,y = 700, 400  # Initial position of the character
#game initialization
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Soccer Game")
clock = pg.time.Clock()
running = True
Character = pg.image.load("character/m0.png")
char_run1 = pg.image.load("character/m1.png")
char_run2 = pg.image.load("character/m2.png")
char_run3 = pg.image.load("character/m3.png")
char_run4 = pg.image.load("character/m4.png")
#background
bg_image = pg.image.load("Background/b1.png").convert()
bg_image = pg.transform.scale(bg_image, (1400, 800))


class movement:
    def __init__(self):
        self.inputs = ""

    def keyboard(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.inputs = "up"
        elif keys[pg.K_s]:
            self.inputs = "down"
        elif keys[pg.K_a]:
            self.inputs = "left"
        elif keys[pg.K_d]:
            self.inputs = "right"
        elif keys[pg.K_SPACE]:
            self.inputs = "dribble"
        elif keys[pg.K_KP_ENTER]:
            self.inputs = "kick"
        return str(self.inputs)

#character visibility
def char_visibility(v):
    if v == True:
        screen.blit(Character, (x, y))
    else:
        screen.blit(bg_image, (0, 0))  # Redraw the background to "hide" the character



#image button functionality    
class Button:
    def __init__(self, x, y, image_path, scale=None):
        # 1. Load the PNG image with alpha transparency support
        self.image = pg.image.load(image_path).convert_alpha()     
        # Optional: Scale the image if it's too big/small
        if scale:
            self.image = pg.transform.scale(self.image, scale)        
        # 2. Get the rectangular bounding box of the image and set its position
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self, surface):
        # 3. Draw (blit) the image onto the screen
        surface.blit(self.image, self.rect.topleft)
    def check_click(self, mouse_pos):
        # 4. Check if the mouse cursor coordinates collide with our button's rect
        return self.rect.collidepoint(mouse_pos)


start_button = Button(x=600, y=300, image_path="Buttons/play.png", scale=None)
exit_button = Button(x=1200, y=0, image_path="Buttons/exit.png", scale=None)
menu_button = Button(x=1200, y=70, image_path="Buttons/menu.png", scale=None)
#quit_button = Button(x=600, y=440, image_path="Buttons/quit.png", scale=None)

current_screen = "MENU"

def char_run_animation(x, y):
    # List of character running images
    run_images = [char_run1, char_run2, char_run3, char_run4]
    for img in run_images:
        screen.blit(img, (x, y))
        pg.display.flip()
        pg.time.delay(30)  # Delay to control the speed of the animation

while running == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1: #Listen for mouse click events
            if current_screen == "MENU":
                if start_button.check_click(event.pos):
                    current_screen = "GAME"  # Switch state to GAME  

            elif current_screen == "GAME":
                if exit_button.check_click(event.pos):   # quits the game
                    running = False
                elif menu_button.check_click(event.pos):
                   current_screen = "MENU"  # Switch state back to MENU
    #check the current screen
    if current_screen == "MENU":
        bg_image = pg.image.load("Background/b1.png").convert()
        bg_image = pg.transform.scale(bg_image, (1400, 800))
        screen.blit(bg_image, (0, 0))
        start_button.draw(screen)
        pg.display.flip()        
    elif current_screen == "GAME":
        bg_image = pg.image.load("Background/b2.png").convert()
        bg_image = pg.transform.scale(bg_image, (1400, 800))
        screen.blit(bg_image, (0, 0))
        char_visibility(True)  # Draw the character at the current position
        exit_button.draw(screen)
        menu_button.draw(screen)
        pg.display.flip()

    input = movement().keyboard()
    if input == "up":
        x+=10
        char_visibility(False)  # Hide the character
        char_run_animation(x, y)
    elif input == "down":
        x-=10
        char_visibility(False)  # Hide the character
        char_run_animation(x, y)
    elif input == "left":
        y-=10
        char_visibility(False)  # Hide the character
        char_run_animation(x, y)
    elif input == "right":
        y+=10
        char_visibility(False)  # Hide the character
        char_run_animation(x, y)
    elif input == "dribble":
        print("dribble")
    elif input == "kick":
        print("kick")
    
    pg.time.delay(100) #delay to control the speed of the game

pg.quit()# quits the game

