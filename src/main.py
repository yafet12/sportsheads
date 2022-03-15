import os

import pygame

pygame.init()
pygame.mixer.init()

# initialise screen
Game_title = 'Sportsheads'
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(Game_title)
# load all images

GOAL_WIDTH = int(0.2*SCREEN_WIDTH)
GOAL_HEIGHT = int(0.4*SCREEN_HEIGHT)

background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT))
Right_goal = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Right goal.png")), (GOAL_WIDTH, GOAL_HEIGHT))

Left_goal = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets", "Right goal.png")), (GOAL_WIDTH, GOAL_HEIGHT))
Left_goal = pygame.transform.flip(Left_goal, True, False)

Player_1 = None
Player_2 = None
Ball = None
Goal_1 = None
Goal_2 = None

SCORE_FONT = pygame.font.SysFont('comicsans', 40, bold=True)
SCORE_COLOUR = (100, 0, 0)
# draw window
Player_1_score, Player_2_score = 0, 0

#Timer
Time_in_seconds = 200
mins = Time_in_seconds // 60
seconds = Time_in_seconds - 60 * mins

timer_interval = 1000 # 1 second
timer_event = pygame.USEREVENT + 1

print(mins)
print(seconds)

def draw_window(Player_1_score, Player_2_score, mins, seconds):
    screen.blit(background, (0, 0))
    screen.blit(Right_goal, (SCREEN_WIDTH - GOAL_WIDTH//2, SCREEN_HEIGHT - GOAL_HEIGHT))
    screen.blit(Left_goal, (-GOAL_WIDTH//2, SCREEN_HEIGHT - GOAL_HEIGHT))
    # pygame.draw.rect(screen)
    if mins < 10:
        mins = "0{}".format(mins)
    if seconds < 10:
        seconds = "0{}".format(seconds)
    Score_text = SCORE_FONT.render('Score {}:{}'.format(Player_1_score, Player_2_score), 1, SCORE_COLOUR)
    Timer = SCORE_FONT.render('{}:{}'.format(mins, seconds), 1, SCORE_COLOUR)
    # print(Score_text.get_width())
    # print(Timer.get_width())
    screen.blit(Score_text, ((SCREEN_WIDTH - Score_text.get_width()) // 2, 10))
    screen.blit(Timer, ((SCREEN_WIDTH - 90), 10))
    pygame.display.update()


# create players

# create other objects - goals, ball

# define borders

# projectile motion of the ball

# check keys pressed - movements

def jump():
    pass
    # check if player is on the ground - so they can't jump whilst already in mid air


X = 2


def check_if_key_pressed(event, Player_1_score, Player_2_score):

    if event.type == pygame.KEYDOWN:

        # if keys_pressed[pygame.K_UP]:
        #     # player jump
        #     pass

        if event.key == pygame.K_LEFT:
            Player_1_score += 1
            print('P1 ', Player_1_score)
            # move player left

        elif event.key == pygame.K_RIGHT:
            Player_2_score += 1
            print('P2 ', Player_2_score)
            # move player right


clock = pygame.time.Clock()


def ball_projectile_motion():
    pass


crashed = False

while not crashed:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:

            # if keys_pressed[pygame.K_UP]:
            #     # player jump
            #     pass

            if event.key == pygame.K_LEFT:
                Player_1_score += 1
                print('P1 ', Player_1_score)
                # move player left

            elif event.key == pygame.K_RIGHT:
                Player_2_score += 1
                print('P2 ', Player_2_score)
                # move player right

            elif event.key == pygame.K_k:
                pygame.time.set_timer(timer_event, timer_interval)

        # Timer
        elif event.type == timer_event:

            if seconds != -1:
                seconds -= 1
                if seconds == -1 and mins > 0:
                    seconds = 59
                    mins -= 1
                elif mins == 0 and seconds == -1:
                    seconds = 0
                    crashed = True


    keys_pressed = pygame.key.get_pressed()
    draw_window(Player_1_score, Player_2_score, mins, seconds)
    pygame.display.update()

