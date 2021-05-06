import pygame, math
from win32api import GetSystemMetrics


pygame.init()

#Farben [idk warum hier?]
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

#Randomstuff
pygame.display.set_caption("Pong")

spielaktiv = True

clock = pygame.time.Clock()

#Screen
screen_width=GetSystemMetrics(0)
screen_height=GetSystemMetrics(1)
screen=pygame.display.set_mode([screen_width, screen_height])

#Spieler
SPIELER_DURCHMESSER_Y = 100
SPIELER_DURCHMESSER_X = 10

spieler1pos_x = 20
spieler1pos_y = screen_height/2

spieler2pos_x = screen_width-20-SPIELER_DURCHMESSER_X
spieler2pos_y = screen_height/2

spielerbewegung_y = 5

spielfigur_1_bewegung = 0

#Ball
BALL_DURCHMESSER = 20

ballpos_x = 10
ballpos_y = screen_height/2

ball_bewegung_x = 4
ball_bewegung_y = 4

#Create Spieler Array
spieler_array = []

while spielaktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
        if event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")

            if event.key == pygame.K_ESCAPE:
                print("Spieler hat ESC runter gedrückt")
                spielaktiv = False
                
            # Taste für Spieler 1
            if event.key == pygame.K_UP:
                print("Spieler hat Pfeiltaste runter gedrückt")
                spielfigur_1_bewegung = -6
            elif event.key == pygame.K_DOWN:
                print("Spieler hat Pfeiltaste runter gedrückt")
                spielfigur_1_bewegung = 6

        if event.type == pygame.KEYUP:
            print("Spieler hat Taste losgelassen")

            # Tasten für Spieler 1
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                print("Spieler 1 stoppt bewegung")
                spielfigur_1_bewegung = 0

    # Spiellogik
    if spielfigur_1_bewegung != 0:
        spieler1pos_y += spielfigur_1_bewegung

    screen.fill(SCHWARZ)

    #Draw Ball
    pygame.draw.ellipse(screen, WEISS, [ballpos_x, ballpos_y, BALL_DURCHMESSER, BALL_DURCHMESSER])

    #Draw Players
    pygame.draw.rect(screen, WEISS,[spieler1pos_x, spieler1pos_y, SPIELER_DURCHMESSER_X, SPIELER_DURCHMESSER_Y ])
    pygame.draw.rect(screen, WEISS,[spieler2pos_x, spieler2pos_y, SPIELER_DURCHMESSER_X, SPIELER_DURCHMESSER_Y])

    #Balllogic
    ballpos_x += ball_bewegung_x
    ballpos_y += ball_bewegung_y

    
    if ballpos_y > screen_height - BALL_DURCHMESSER or ballpos_y < 0:
        ball_bewegung_y = ball_bewegung_y * -1

    if ballpos_x > screen_width - BALL_DURCHMESSER or ballpos_x < 0:
        ball_bewegung_x = ball_bewegung_x * -1
    
    #Kollisionslogik
    if ballpos_y >= spieler1pos_y and ballpos_y <= spieler1pos_y + SPIELER_DURCHMESSER_Y and ballpos_x - BALL_DURCHMESSER/2 <= spieler1pos_x + SPIELER_DURCHMESSER_X:
        ball_bewegung_x = ball_bewegung_x * -1
    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit()
