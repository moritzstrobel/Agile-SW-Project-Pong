import pygame, math
import random
from win32api import GetSystemMetrics

#Setup
pygame.init()
clock = pygame.time.Clock()

#Farben [idk warum hier?]
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

#Randomstuff
pygame.display.set_caption("Pong")
spielaktiv = True


#Screen
screen_width=GetSystemMetrics(0)
screen_height=GetSystemMetrics(1)
screen=pygame.display.set_mode([screen_width, screen_height])

#Rects
player1 = pygame.Rect(10, screen_height/2 - 70, 10 , 140)
opponent = pygame.Rect(screen_width - 20, screen_height/2 -70, 10 , 140)
ball = pygame.Rect(screen_width/2 -20, screen_height/2 -20, 20, 20)

wand1 = pygame.Rect(0, 0, screen_width, 10)
wand2 = pygame.Rect(0, screen_height - 10, screen_width, 10)

powerup = pygame.Rect(0, 0, 20, 20)


#PoerupRando
punishedPlayer = 0
punishedOpponent = 0
punishedBalls = 0

def puballschneller(whotopunish):
    global punishedPlayer, punishedBalls
    #logic fuer die Groessenaenderung bei Powerup


def puschnellerlangsam(whotopunish):
    global punishedPlayer, punishedBalls
    #logic fuer die Schnelligkeit bei Powerup
    if whotopunish == 1:
        punishedPlayer = -4
        punishedOpponent = 0

    if whotopunish == 0:
        punishedPlayer = 0
        punishedOpponent = 4

def powerupPicker(whotopunish):
    if whotopunish == 1:
        puschnellerlangsam(1)

    if whotopunish == 0:
        puschnellerlangsam(0)

#Movement

ball_speedx = 4 * random.choice((1, -1))
ball_speedy = 4 * random.choice((1, -1))
player1_speed = 0
opponent_speed = 11 + punishedOpponent

#Score
player_score = 0
opponent_score = 0

game_font = pygame.font.SysFont("freesansbold.TTF", 32)

#Animation

def ball_animation():
    global ball_speedx, ball_speedy, opponent_score, player_score, punishedBalls
    ball.x += ball_speedx + punishedBalls
    ball.y += ball_speedy + punishedBalls

    if ball.colliderect(wand1) or ball.colliderect(wand2):
        ball_speedy *= -1 

    if ball.left <= 0 or ball.right >= screen_width:
        if ball.left <= 0:
            player_score += 1
            powerupPicker(0)
        if ball.right >= screen_width:
            opponent_score += 1
            powerupPicker(1)
        ball_restart()

    if ball.colliderect(player1) or ball.colliderect(opponent):
        ball_speedx *= -1

def player_animation():
    player1.y += player1_speed
    if player1.top <= wand1[3]:
        player1.top = wand1[3]
    if player1.bottom >= screen_height - wand2[3]:
        player1.bottom = screen_height - wand2[3]
       

def opponent_ai():
    if ball.x > screen_width/2:
        if opponent.top < ball.y:
            opponent.top += opponent_speed
        if opponent.bottom > ball.y:
            opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height 

def ball_restart():
    global ball_speedx, ball_speedy
    ball.center = (screen_width/2, screen_height/2)
    ball_speedy *= random.choice((1, -1)) 
    ball_speedx *= random.choice((1, -1))




#Create Spieler Array
spieler_array = []

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
    screen.fill(SCHWARZ)
    pygame.draw.ellipse(screen, WEISS, ball)
    pygame.draw.rect(screen, "#3B50BF", player1)
    pygame.draw.rect(screen, "#E62C27", opponent)
    pygame.draw.rect(screen, "#555455", wand1)
    pygame.draw.rect(screen, "#555455", wand2)
    pygame.draw.aaline(screen, "#555455", (screen_width / 2, 0), (screen_width / 2, screen_height))

   

    player_text = game_font.render(str(player_score) + "  ", False, "#3B50BF")
    screen.blit(player_text, (screen_width/2 + player_text.get_width(), screen_height/2))

    opponent_text = game_font.render(str(opponent_score) + "  ", False, "#E62C27")
    screen.blit(opponent_text, (screen_width/2 - opponent_text.get_width()*1.5, screen_height/2))



   
    #Update
    pygame.display.flip()
    clock.tick(60)
