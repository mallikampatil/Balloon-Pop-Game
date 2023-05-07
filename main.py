import pygame
from sys import exit
import random

from pygame.examples.moveit import GameObject

# Biggest Current Challenges to solve:
# Collision Detection:
# There is a TODO for when the score needs to be updated
pygame.init()
screen = pygame.display.set_mode((500, 650))
pygame.display.set_caption('Balloon Pop')
clock = pygame.time.Clock()
my_font = pygame.font.Font('font/Pixeltype.ttf', 76)
my_score_font = pygame.font.Font('font/Pixeltype.ttf', 50)
darts_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_over = pygame.font.Font('font/Pixeltype.ttf', 85)

my_score = 0
sky_surface = pygame.image.load('images/sky.png')
my_text_surface = my_font.render('Balloon Pop Game', False, 'Yellow')
pink_balloon_surface = pygame.image.load('images/balloon-pink.png').convert_alpha()
blue_balloon_surface = pygame.image.load('images/balloon-blue.png').convert_alpha()
pink_balloon_surface_2 = pygame.image.load('images/balloon-pink-2.png').convert_alpha()
blue_balloon_surface_2 = pygame.image.load('images/balloon-blue-2.png').convert_alpha()

blue_balloon_y_pos = random.randint(0,500)
pink_balloon_y_pos = random.randint(0,500)
blue_balloon_y_pos_2 = random.randint(0,500)
pink_balloon_y_pos_2 = random.randint(0,500)

DART_GUN_IMAGE_RESIZE = (300, 300)
DART_IMAGE_RESIZE = (25, 25)

dart_gun = pygame.image.load('images/dart-gun.png')
dart_gun_resized_img = pygame.transform.scale(dart_gun, DART_GUN_IMAGE_RESIZE);
dart_gun_x_pos = 300
alpha = 0

dart = pygame.image.load('images/dart.png')
dart_resized_img = pygame.transform.scale(dart, DART_IMAGE_RESIZE);
dart_y_pos = 515

# MOVING LEFT AND RIGHT
moving_left = False
moving_right = False
number_of_darts = 5
shoot_dart = False

dart_location = [350, 550]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()

    go_surface = darts_font.render(str('GAME OVER'), False, 'black')

    # If keydown == SPACE, then throw
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dart_y_pos = 515
                number_of_darts -= 1
                shoot_dart = True
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                # dart_gun_x_pos = dart_gun_x_pos + 5
                moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                # dart_gun_x_pos = dart_gun_x_pos + 5
                moving_right = False
        # If keydown == LEFT, then move rocket left
        # If keydown == RIGHT, then move rocket right

    my_score_surface = my_score_font.render(str('Score: ') + str(my_score), False, 'coral3')
    my_darts_surface = darts_font.render(str('Darts: ') + str(number_of_darts), False, 'coral3')

    if moving_left == True:
        dart_location[0] -= 5
    if moving_right == True:
        dart_location[0] += 5

    screen.blit(sky_surface,(0,0))
    screen.blit(my_text_surface,(50,50))
    screen.blit(my_score_surface,(300,125))
    screen.blit(my_darts_surface,(300,150))
    screen.blit(dart_gun,dart_location)
    shoot_dart_x = dart_location[0] + 35

    if shoot_dart == True:
        dart_y_pos -= 3
        screen.blit(dart, (shoot_dart_x, dart_y_pos))


    blue_balloon_y_pos -= 5
    if blue_balloon_y_pos < -100:
        blue_balloon_y_pos = 500
    screen.blit(blue_balloon_surface,(blue_balloon_y_pos, 150))

    pink_balloon_y_pos -= 5
    if pink_balloon_y_pos < -100: pink_balloon_y_pos = 500
    screen.blit(pink_balloon_surface,(pink_balloon_y_pos, 5))

    blue_balloon_y_pos_2 -= 5
    if blue_balloon_y_pos_2 < -100: blue_balloon_y_pos_2 = 500
    screen.blit(blue_balloon_surface_2,(blue_balloon_y_pos_2, 250))

    pink_balloon_y_pos_2 -= 5
    if pink_balloon_y_pos_2 < -100: pink_balloon_y_pos_2 = 500
    screen.blit(pink_balloon_surface_2,(pink_balloon_y_pos_2, 300))

    transparent = (0, 0, 0, 0)
    # Quickly check for collisions between balloons and darts
    # TODO: Need to add scoring mechanism
    # Add text on right corner top to update score variable if the dart collides with the balloon
    if blue_balloon_y_pos == dart_y_pos:
        blue_balloon_surface.set_alpha(alpha)
        my_score += 1
    if pink_balloon_y_pos == dart_y_pos:
        pink_balloon_surface.set_alpha(alpha)
        my_score += 1
    if blue_balloon_y_pos_2 == dart_y_pos:
        blue_balloon_surface_2.set_alpha(alpha)
        my_score += 1
    if pink_balloon_y_pos_2 == dart_y_pos:
        pink_balloon_surface_2.set_alpha(alpha)
        my_score += 1

    pygame.display.update()
    clock.tick(60)
