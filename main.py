import pygame, math
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
player2 = pygame.Rect(screen_width - 20, screen_height/2 -70, 10 , 140)
ball = pygame.Rect(screen_width/2 -20, screen_height/2 -20, 20, 20)

#Movement

ball_speedx = 4
ball_speedy = 4
player1_speed = 0

#Ball Animation
def ball_animation():
    global ball_speedx, ball_speedy
    ball.x += ball_speedx
    ball.y += ball_speedy

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speedy *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_speedx *= -1

    if ball.colliderect(player1) or ball.colliderect(player2
):
        ball_speedx *= -1



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
    # if player1_speed!= 0 :
    #     player1[1] += player1_speed
    
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height  

    #Visual
    screen.fill(SCHWARZ)
    pygame.draw.ellipse(screen, WEISS, ball)
    pygame.draw.rect(screen, WEISS, player1)
    pygame.draw.rect(screen, WEISS, player2
)

    
   
    #Update
    pygame.display.flip()
    clock.tick(60)
