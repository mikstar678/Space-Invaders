import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 800, 700
FPS = 60
score = 20
def add_ten():
    global score
    score += 10
def add_twenty():
    global score 
    score += 20
def add_thirty():
    global score
    score += 30
def print_score():
    global score
    print(score)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

font = pygame.font.Font("Font/ARCADECLASSIC.ttf", 50)

PurpleBaddie1 = pygame.image.load("Graphics/PurpleBaddie1.png").convert_alpha()
PurpleBaddie1 = pygame.transform.scale(PurpleBaddie1, (40, 30))

GreenBaddie1 = pygame.image.load("Graphics/GreenBaddie1.png").convert_alpha()
GreenBaddie1 = pygame.transform.scale(GreenBaddie1, (35,35))

RedBaddie1 = pygame.image.load("Graphics/RedBaddie1.png").convert_alpha()
RedBaddie1 = pygame.transform.scale(RedBaddie1, (35,35))

GoodGuy = pygame.image.load("Graphics/GoodGuy.png").convert_alpha()
GoodGuy = pygame.transform.scale(GoodGuy, (40, 30))

bullet_img = pygame.image.load("Graphics/bullet.jpg").convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (5, 5))

SISTARTTEXT = font.render('SPACE INVADERS', False, (255, 0, 0))
SISTARTTEXT2 = font.render('SHOOT ALIEN   TO   START', False, (255,0,0))
level1endtext1 = font.render('LEVEL   1   C LE A R E D  !', False, (255,0,0))
level1endtext2 = font.render('Press   x    to  continue', False, (255,0,0))
scoretext = font.render('Score', False, (255,5,0))
scoretext = pygame.transform.scale(scoretext, (100,40)) 
def update_score():
    scorenumber = font.render(str(score), False, (255,5,0))
    scorenumber = pygame.transform.scale(scorenumber, (40,40))
def showscore():
    global scorenumber
    screen.blit((scorenumber),(0,0))
def level2():
    lvl2 = 0
    bullets = []
    bullet_speed = -7
    last_shot = 0
    shoot_delay = 300
    badmove1 = 0
    badmovefunc1 = 0
    GOODGUYSPEED = 4
    killcount = 0
    FPS = 60
     # Alien Generation
    PurpleBaddies = []
    startxp = 107
    startyp = 105
    pbycount = 0
    for i in range(20):
        PurpleBaddies.append(PurpleBaddie1.get_rect(midtop=(startxp,startyp)))
        startxp += 62
        pbycount += 1
        if pbycount == 10:
            startyp += 50
            startxp = 107
    GreenBaddies = []
    startxg = 107
    startyg = 205
    gbycount = 0
    for i in range(20):
        GreenBaddies.append(GreenBaddie1.get_rect(midtop=(startxg,startyg)))
        startxg += 62
        gbycount += 1
        if gbycount == 10:
            startyg += 50
            startxg = 107
    RedBaddies = []
    startxr = 107
    startyr = 305
    rbycount = 0
    for i in range(20):
        RedBaddies.append(RedBaddie1.get_rect(midtop=(startxr,startyr)))
        startxr += 62
        rbycount += 1
        if rbycount == 10:
            startyr += 50
            startxr = 107
    while lvl2 == 0:

        #Housekeeping
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill("black")

        #GoodGuy Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            GOODGUYSPEED += 4
        if keys[pygame.K_a]:
            GOODGUYSPEED -=4
        
        #Bullet Generation
        now = pygame.time.get_ticks()
        if keys[pygame.K_w] and now - last_shot > shoot_delay:
            bullets.append(bullet_img.get_rect(midbottom=GoodGuyrect.midtop))
            last_shot = now
        
        #Bullet collision / bullet deletion
        for bullet in bullets[:]:
            bullet.y += bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)
                continue

            for alien in PurpleBaddies[:]:
                if alien.colliderect(bullet):
                    bullets.remove(bullet)
                    PurpleBaddies.remove(alien)
                    killcount += 1
                    add_thirty()
                    update_score()
                    break
            else:
                for alien in GreenBaddies[:]:
                    if alien.colliderect(bullet):
                        bullets.remove(bullet)
                        GreenBaddies.remove(alien)
                        killcount += 1
                        add_twenty()
                        update_score()
                        break
                else:
                    for alien in RedBaddies[:]:
                        if alien.colliderect(bullet):
                            bullets.remove(bullet)
                            RedBaddies.remove(alien)
                            killcount += 1
                            add_ten()
                            update_score()
                            showscore()
                            break

        #Alien Drawing -> bullet drawing
        for alien in PurpleBaddies:
            screen.blit(PurpleBaddie1, alien)
        for alien in GreenBaddies:
            screen.blit(GreenBaddie1, alien)
        for alien in RedBaddies:
            screen.blit(RedBaddie1, alien)
        for bullet in bullets:
            screen.blit(bullet_img, bullet)
        GoodGuyrect = GoodGuy.get_rect(topleft=(GOODGUYSPEED, 670))
        screen.blit(GoodGuy,GoodGuyrect)
        screen.blit(scoretext, (0,0))

        #Alien Movement
        badmove1 += 1
        if badmove1 % 120 == 0:
            if badmovefunc1 == 0:
                badmovefunc1 = 1
                for alien in PurpleBaddies:
                    alien.x += 30
                for alien in GreenBaddies:
                    alien.x += 30
                for alien in RedBaddies:
                    alien.x += 30
            elif badmovefunc1 == 1:
                badmovefunc1 = 2
                for alien in PurpleBaddies:
                    alien.y += 30
                for alien in GreenBaddies:
                    alien.y += 30
                for alien in RedBaddies:
                    alien.y += 30
            elif badmovefunc1 == 2:
                badmovefunc1 = 3
                for alien in PurpleBaddies:
                    alien.x -= 30
                for alien in GreenBaddies:
                    alien.x -= 30
                for alien in RedBaddies:
                    alien.x -= 30
            elif badmovefunc1 == 3:
                badmovefunc1 = 0
                for alien in PurpleBaddies:
                    alien.y -= 30
                for alien in GreenBaddies:
                    alien.y -= 30
                for alien in RedBaddies:
                    alien.y -= 30
        pygame.display.update()
        clock.tick(FPS)

def level1end():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill('black')
        screen.blit(level1endtext1, (165,150))
        screen.blit(level1endtext2, (165, 400))
        key = pygame.key.get_pressed()
        if key[pygame.K_x]:
            level2()
            y += 1
            
        pygame.display.update()
        clock.tick(FPS)


def level1():
    GoodGuyrect = GoodGuy.get_rect(topleft=(0, 670))
    PurpleBaddie1rect = PurpleBaddie1.get_rect(midtop=(107,105))
    PurpleBaddie2rect = PurpleBaddie1.get_rect(midtop=(169,105))
    PurpleBaddie3rect = PurpleBaddie1.get_rect(midtop=(231,105))
    PurpleBaddie4rect = PurpleBaddie1.get_rect(midtop=(293,105))
    PurpleBaddie5rect = PurpleBaddie1.get_rect(midtop=(355,105))
    PurpleBaddie6rect = PurpleBaddie1.get_rect(midtop=(417,105))
    PurpleBaddie7rect = PurpleBaddie1.get_rect(midtop=(479,105))
    PurpleBaddie8rect = PurpleBaddie1.get_rect(midtop=(541,105))
    PurpleBaddie9rect = PurpleBaddie1.get_rect(midtop=(603,105))
    PurpleBaddie10rect = PurpleBaddie1.get_rect(midtop=(665,105))
    PurpleBaddie11rect = PurpleBaddie1.get_rect(midtop=(107,155))
    PurpleBaddie12rect = PurpleBaddie1.get_rect(midtop=(169,155))
    PurpleBaddie13rect = PurpleBaddie1.get_rect(midtop=(231,155))
    PurpleBaddie14rect = PurpleBaddie1.get_rect(midtop=(293,155))
    PurpleBaddie15rect = PurpleBaddie1.get_rect(midtop=(355,155))
    PurpleBaddie16rect = PurpleBaddie1.get_rect(midtop=(417,155))
    PurpleBaddie17rect = PurpleBaddie1.get_rect(midtop=(479,155))
    PurpleBaddie18rect = PurpleBaddie1.get_rect(midtop=(541,155))
    PurpleBaddie19rect = PurpleBaddie1.get_rect(midtop=(603,155))
    PurpleBaddie20rect = PurpleBaddie1.get_rect(midtop=(665,155))
    GreenBaddies = []
    startx = 107
    starty = 205
    gbycount = 0
    for i in range(20):
        GreenBaddies.append(GreenBaddie1.get_rect(midtop=(startx,starty)))
        startx += 62
        gbycount += 1
        if gbycount == 10:
            starty += 50
            startx = 107
    RedBaddies = []
    startx = 107
    starty = 305
    gbycount = 0
    for i in range(20):
        RedBaddies.append(RedBaddie1.get_rect(midtop=(startx,starty)))
        startx += 62
        gbycount += 1
        if gbycount == 10:
            starty += 50
            startx = 107

    bullets = []
    bullet_speed = -7
    last_shot = 0
    shoot_delay = 300
    badmove1 = 0
    badmovefunc1 = 0
    GOODGUYSPEED = 4
    killcount = 0
    yy = 0
    while yy == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            GoodGuyrect.x += GOODGUYSPEED
        if keys[pygame.K_a]:
            GoodGuyrect.x -= GOODGUYSPEED

        now = pygame.time.get_ticks()
        if keys[pygame.K_w] and now - last_shot > shoot_delay:
            bullets.append(bullet_img.get_rect(midbottom=GoodGuyrect.midtop))
            last_shot = now

        for bullet in bullets[:]:
            bullet.y += bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)
            elif PurpleBaddie1rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie1rect.x += 99999
            elif PurpleBaddie2rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1  
                PurpleBaddie2rect.x += 99999
            elif PurpleBaddie3rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie3rect.x += 99999
            elif PurpleBaddie4rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie4rect.x += 99999
            elif PurpleBaddie5rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie5rect.x += 99999
            elif PurpleBaddie6rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie6rect.x += 99999
            elif PurpleBaddie7rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie7rect.x += 99999
            elif PurpleBaddie8rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie8rect.x += 99999
            elif PurpleBaddie9rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie9rect.x += 99999
            elif PurpleBaddie10rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie10rect.x += 99999
            elif PurpleBaddie11rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie11rect.x += 99999
            elif PurpleBaddie12rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie12rect.x += 99999
            elif PurpleBaddie13rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie13rect.x += 99999
            elif PurpleBaddie14rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie14rect.x += 99999
            elif PurpleBaddie15rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie15rect.x += 99999
            elif PurpleBaddie16rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie16rect.x += 99999
            elif PurpleBaddie17rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie17rect.x += 99999
            elif PurpleBaddie18rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie18rect.x += 99999
            elif PurpleBaddie19rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie19rect.x += 99999
            elif PurpleBaddie20rect.colliderect(bullet):
                bullets.remove(bullet)
                killcount += 1
                PurpleBaddie20rect.x += 99999
            for alien in GreenBaddies[:]:
                 if alien.colliderect(bullet):
                    bullets.remove(bullet)
                    GreenBaddies.remove(alien)
                    killcount += 1
                    break
            for alien in RedBaddies[:]:
                if alien.colliderect(bullet):
                    bullets.remove(bullet)
                    RedBaddies.remove(alien)
                    killcount += 1
                    add_ten()
                    break
            
        screen.fill("black")
        screen.blit(GoodGuy, GoodGuyrect)
        screen.blit(PurpleBaddie1, PurpleBaddie1rect)
        screen.blit(PurpleBaddie1, PurpleBaddie2rect)
        screen.blit(PurpleBaddie1, PurpleBaddie3rect)
        screen.blit(PurpleBaddie1, PurpleBaddie4rect)
        screen.blit(PurpleBaddie1, PurpleBaddie5rect)
        screen.blit(PurpleBaddie1, PurpleBaddie6rect)
        screen.blit(PurpleBaddie1, PurpleBaddie7rect)
        screen.blit(PurpleBaddie1, PurpleBaddie8rect)
        screen.blit(PurpleBaddie1, PurpleBaddie9rect)
        screen.blit(PurpleBaddie1, PurpleBaddie10rect)
        screen.blit(PurpleBaddie1, PurpleBaddie11rect)
        screen.blit(PurpleBaddie1, PurpleBaddie12rect)
        screen.blit(PurpleBaddie1, PurpleBaddie13rect)
        screen.blit(PurpleBaddie1, PurpleBaddie14rect)
        screen.blit(PurpleBaddie1, PurpleBaddie15rect)
        screen.blit(PurpleBaddie1, PurpleBaddie16rect)
        screen.blit(PurpleBaddie1, PurpleBaddie17rect)
        screen.blit(PurpleBaddie1, PurpleBaddie18rect)
        screen.blit(PurpleBaddie1, PurpleBaddie19rect)
        screen.blit(PurpleBaddie1, PurpleBaddie20rect)
        for alien in GreenBaddies:
            screen.blit(GreenBaddie1, alien)
        for alien in RedBaddies:
            screen.blit(RedBaddie1, alien)
        screen.blit(scoretext, (10,5))

        badmove1 += 1
        if badmove1 % 120 == 0:
            if badmovefunc1 == 0:
                badmovefunc1 = 1
                PurpleBaddie1rect.x += 20
                PurpleBaddie2rect.x += 20
                PurpleBaddie3rect.x += 20
                PurpleBaddie4rect.x += 20
                PurpleBaddie5rect.x += 20
                PurpleBaddie6rect.x += 20
                PurpleBaddie7rect.x += 20
                PurpleBaddie8rect.x += 20
                PurpleBaddie9rect.x += 20
                PurpleBaddie10rect.x += 20
                PurpleBaddie11rect.x += 20
                PurpleBaddie12rect.x += 20
                PurpleBaddie13rect.x += 20
                PurpleBaddie14rect.x += 20
                PurpleBaddie15rect.x += 20
                PurpleBaddie16rect.x += 20
                PurpleBaddie17rect.x += 20
                PurpleBaddie18rect.x += 20
                PurpleBaddie19rect.x += 20
                PurpleBaddie20rect.x += 20
                for alien in GreenBaddies:
                    alien.x += 20
                for alien in RedBaddies:
                    alien.x +=20
            elif badmovefunc1 == 1:
                badmovefunc1 = 2
                PurpleBaddie1rect.y -= 20
                PurpleBaddie2rect.y -= 20
                PurpleBaddie3rect.y -= 20
                PurpleBaddie4rect.y -= 20
                PurpleBaddie5rect.y -= 20
                PurpleBaddie6rect.y -= 20
                PurpleBaddie7rect.y -= 20
                PurpleBaddie8rect.y -= 20
                PurpleBaddie9rect.y -= 20
                PurpleBaddie10rect.y -= 20
                PurpleBaddie11rect.y -= 20
                PurpleBaddie12rect.y -= 20
                PurpleBaddie13rect.y -= 20
                PurpleBaddie14rect.y -= 20
                PurpleBaddie15rect.y -= 20
                PurpleBaddie16rect.y -= 20
                PurpleBaddie17rect.y -= 20
                PurpleBaddie18rect.y -= 20
                PurpleBaddie19rect.y -= 20
                PurpleBaddie20rect.y -= 20
                for alien in GreenBaddies:
                    alien.y -= 20
                for alien in RedBaddies:
                    alien.y -= 20
            elif badmovefunc1 == 2:
                badmovefunc1 = 3
                PurpleBaddie1rect.x -= 20
                PurpleBaddie2rect.x -= 20
                PurpleBaddie3rect.x -= 20
                PurpleBaddie4rect.x -= 20
                PurpleBaddie5rect.x -= 20
                PurpleBaddie6rect.x -= 20
                PurpleBaddie7rect.x -= 20
                PurpleBaddie8rect.x -= 20
                PurpleBaddie9rect.x -= 20
                PurpleBaddie10rect.x -= 20
                PurpleBaddie11rect.x -= 20
                PurpleBaddie12rect.x -= 20
                PurpleBaddie13rect.x -= 20
                PurpleBaddie14rect.x -= 20
                PurpleBaddie15rect.x -= 20
                PurpleBaddie16rect.x -= 20
                PurpleBaddie17rect.x -= 20
                PurpleBaddie18rect.x -= 20
                PurpleBaddie19rect.x -= 20
                PurpleBaddie20rect.x -= 20
                for alien in GreenBaddies:
                    alien.x -= 20
                for alien in RedBaddies:
                    alien.x -= 20
            elif badmovefunc1 == 3:
                badmovefunc1 = 0 
                PurpleBaddie1rect.y += 20
                PurpleBaddie2rect.y += 20
                PurpleBaddie3rect.y += 20
                PurpleBaddie4rect.y += 20
                PurpleBaddie5rect.y += 20
                PurpleBaddie6rect.y += 20
                PurpleBaddie7rect.y += 20
                PurpleBaddie8rect.y += 20
                PurpleBaddie9rect.y += 20
                PurpleBaddie10rect.y += 20
                PurpleBaddie11rect.y += 20
                PurpleBaddie12rect.y += 20
                PurpleBaddie13rect.y += 20
                PurpleBaddie14rect.y += 20
                PurpleBaddie15rect.y += 20
                PurpleBaddie16rect.y += 20
                PurpleBaddie17rect.y += 20
                PurpleBaddie18rect.y += 20
                PurpleBaddie19rect.y += 20
                PurpleBaddie20rect.y += 20
                for alien in GreenBaddies:
                    alien.y += 20
                for alien in RedBaddies:
                    alien.y += 20

        for bullet in bullets:
            screen.blit(bullet_img, bullet)

        if killcount == 2:
            level1end()
            yy += 1
        pygame.display.update()
        clock.tick(FPS)

GoodGuyrect = GoodGuy.get_rect(topleft=(0, 670))
PurpleBaddie1rect = PurpleBaddie1.get_rect(midtop=(90, 90))

bullets = []
bullet_speed = -7
last_shot = 0
shoot_delay = 300
GOODGUYSPEED = 4
begin = 0

while begin == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        GoodGuyrect.x += GOODGUYSPEED
    if keys[pygame.K_a]:
        GoodGuyrect.x -= GOODGUYSPEED

    now = pygame.time.get_ticks()
    if keys[pygame.K_w] and now - last_shot > shoot_delay:
        bullets.append(bullet_img.get_rect(midbottom=GoodGuyrect.midtop))
        last_shot = now

    for bullet in bullets[:]:
        bullet.y += bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)
        elif PurpleBaddie1rect.colliderect(bullet):
            bullets.remove(bullet)
            level1()
            begin += 1

    screen.fill("black")
    screen.blit(GoodGuy, GoodGuyrect)
    screen.blit(PurpleBaddie1, PurpleBaddie1rect)
    screen.blit(SISTARTTEXT,(400,350))
    screen.blit(SISTARTTEXT2,(250,400))

    for bullet in bullets:
        screen.blit(bullet_img, bullet)

    pygame.display.update()
    clock.tick(FPS)




