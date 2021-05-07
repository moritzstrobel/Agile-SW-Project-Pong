import pygame, math
import random
from win32api import GetSystemMetrics

#Setup
pygame.init()
clock = pygame.time.Clock()

#Randomstuff
pygame.display.set_caption("Pong")
spielaktiv = True

#Farben [idk warum hier?]
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
WEISS = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

#Movement
ball_speedx = 8 * random.choice((1, -1))
ball_speedy = 8 * random.choice((1, -1))
player1_speed = 0
opponent_speed = 7.7

#Score
player_score = 0
opponent_score = 0
game_font = pygame.font.SysFont("freesansbold.TTF", 200)

#Score-Timer
score_time = None


#Screen
screen_width=GetSystemMetrics(0)
screen_height=GetSystemMetrics(1)
screen=pygame.display.set_mode([screen_width, screen_height])

#Rects
player1 = pygame.Rect(10, screen_height/2 - 80, 10 , 160)
opponent = pygame.Rect(screen_width - 20, screen_height/2 -80, 10 , 160)
ball = pygame.Rect(screen_width/2 -20, screen_height/2 -20, 20, 20)

wand1 = pygame.Rect(0, 0, screen_width, 10)
wand2 = pygame.Rect(0, screen_height - 10, screen_width, 10)

# #PoerupRando
# punishedPlayer = 0
# punishedOpponent = 0
# punishedBalls = 0

# def puballschneller(whotopunish):
#     global punishedPlayer, punishedBalls
#     #logic fuer die Groessenaenderung bei Powerup

# def puschnellerlangsam(whotopunish):
#     global punishedPlayer, punishedBalls
#     #logic fuer die Schnelligkeit bei Powerup
#     if whotopunish == 1:
#         punishedPlayer = -4
#         punishedOpponent = 0

#     if whotopunish == 0:
#         punishedPlayer = 0
#         punishedOpponent = 4

# def powerupPicker(whotopunish):
#     if whotopunish == 1:
#         puschnellerlangsam(1)

#     if whotopunish == 0:
#         puschnellerlangsam(0)

#Animation
def ball_animation():
    global ball_speedx, ball_speedy, opponent_score, player_score, score_time
    ball.x += ball_speedx
    ball.y += ball_speedy

    if ball.colliderect(wand1) or ball.colliderect(wand2):
        ball_speedy *= -1
        # ball_speedy += 0.1
        # ball_speedx += 0.1


    if ball.left <= 0:
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        player_score += 1
        score_time = pygame.time.get_ticks()


    if ball.colliderect(player1) or ball.colliderect(opponent):
        ball_speedx *= -1
        # ball_speedx += 0.1
        # ball_speedy += 0.1


def player_animation():
    player1.y += player1_speed
    if player1.top <= wand1[3]:
        player1.top = wand1[3]
    if player1.bottom >= screen_height - wand2[3]:
        player1.bottom = screen_height - wand2[3]
       

def opponent_ai():
    if ball.x > screen_width/2:
        if opponent.centery < ball.centery:
            opponent.centery += opponent_speed
        if opponent.centery > ball.centery:
            opponent.centery -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height 

def ball_start():
    
    global ball_speedx, ball_speedy, score_time
    

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)


    if current_time - score_time < 700:
        number_three = game_font.render("3", True, WEISS)
        screen.blit(number_three,(screen_width/ 2 - number_three.get_width()/2, screen_height/ 2 + number_three.get_height()/2))
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", True, WEISS)
        screen.blit(number_two,(screen_width/ 2 - number_two.get_width()/2, screen_height/ 2 + number_two.get_height()/2))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", True, WEISS)
        screen.blit(number_one,(screen_width/ 2 - number_one.get_width()/2, screen_height/ 2 + number_one.get_height()/2))

    if current_time - score_time < 2100:
        ball_speedx, ball_speedy = 0,0

        
    else:
        ball_speedy = 8 * random.choice((1, -1)) 
        ball_speedx = 8 * random.choice((1, -1))
        score_time = None

while spielaktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                    spielaktiv = False
            if event.key == pygame.K_DOWN:
                 player1_speed += 6
            if event.key == pygame.K_UP:
                 player1_speed -= 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                 player1_speed -= 6
            if event.key == pygame.K_UP:
                 player1_speed += 6
     
    ball_animation()  
    player_animation()
    opponent_ai()
     
    #Visual
    screen.fill("#1C1C26")
    pygame.draw.aaline(screen, WEISS, (screen_width / 2, 0), (screen_width / 2, screen_height), 1)
    pygame.draw.ellipse(screen, WEISS, ball)
    pygame.draw.rect(screen, "#82BEFF", player1)
    pygame.draw.rect(screen, "#DB797F", opponent)
    pygame.draw.rect(screen, WEISS, wand1)
    pygame.draw.rect(screen, WEISS, wand2)

    if score_time:
        ball_start()

    player_text = game_font.render(f'{player_score}', True, "#82BEFF")
    screen.blit(player_text, (screen_width/2 -player_text.get_width()/2 -150, screen_height/2 -player_text.get_height()/2))

    opponent_text = game_font.render(f'{opponent_score}',True,"#DB797F")
    screen.blit(opponent_text, (screen_width/2 -opponent_text.get_width()/2 +150, screen_height/2 -opponent_text.get_height()/2))



   
    #Update
    pygame.display.flip()
    clock.tick(60)
