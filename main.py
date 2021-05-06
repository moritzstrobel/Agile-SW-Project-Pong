import pygame, math

pygame.init()

ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
BALL_DURCHMESSER = 20
SPIELER_DURCHMESSER_Y = 50
SPIELER_DURCHMESSER_X = 10

screen_width=1920
screen_height=1080
screen=pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Pong")
spielaktiv = True
clock = pygame.time.Clock()
spieler1pos_x = 20
spieler1pos_y = screen_height/2
spieler2pos_x = screen_width-20-SPIELER_DURCHMESSER_X
spieler2pos_y = screen_height/2
# spielerbewegung_x = 5
spielerbewegung_y = 5
ballpos_x = 10
ballpos_y = screen_height/2

bewegung_x = 4
bewegung_y = 4

while spielaktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
        if event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")
            if event.type == pygame.K_ESCAPE:
               spielaktiv = False 
    screen.fill(SCHWARZ)
    pygame.draw.ellipse(screen, WEISS, [ballpos_x, ballpos_y, BALL_DURCHMESSER, BALL_DURCHMESSER])
    ballpos_x += bewegung_x
    ballpos_y += bewegung_y
    pygame.draw.rect(screen, WEISS,[spieler1pos_x, spieler1pos_y, SPIELER_DURCHMESSER_X, SPIELER_DURCHMESSER_Y ])
    pygame.draw.rect(screen, WEISS,[spieler2pos_x, spieler2pos_y, SPIELER_DURCHMESSER_X, SPIELER_DURCHMESSER_Y])

    if ballpos_y > screen_height - BALL_DURCHMESSER or ballpos_y < 0:
        bewegung_y = bewegung_y * -1

    if ballpos_x > screen_width - BALL_DURCHMESSER or ballpos_x < 0:
        bewegung_x = bewegung_x * -1
    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit()
