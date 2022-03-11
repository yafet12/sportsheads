import pygame

pygame.init()

# initialise screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.time.delay(1000)


# create background, and other shit

# create players

# create other objects - goals, ball

# define borders

# projectile motion of the ball

# check keys pressed

def check_if_key_pressed():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        # player jump
        pass

    elif keys[pygame.K_LEFT]:
        # move player left
        pass
    elif keys[pygame.K_RIGHT]:
        # move player right
        pass


def ball_projectile_motion():
    pass
