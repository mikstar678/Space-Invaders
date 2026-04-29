from sys import exit
import pygame

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 700
FPS = 60

score = 0
level = 6


def st7():
    global level
    level = 7


def st8():
    global level
    level = 8


BLOCK_SIZE = 9
bunkers = []

shape = [
    "   XXXX   ",
    "  XXXXXX  ",
    " XXXXXXXX ",
    "XXXXXXXXXX",
    "XXX    XXX",
    "XX      XX"
]

for start_x in [80, 260, 440, 620]:
    for row, line in enumerate(shape):
        for col, char in enumerate(line):
            if char == "X":
                block = pygame.Rect(
                    start_x + col * BLOCK_SIZE,
                    520 + row * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE
                )
                bunkers.append(block)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

font = pygame.font.Font("Font/ARCADECLASSIC.ttf", 50)

PurpleBaddie1 = pygame.image.load("Graphics/PurpleBaddie1.png").convert_alpha()
PurpleBaddie1 = pygame.transform.scale(PurpleBaddie1, (40, 30))
PurpleBaddie2 = pygame.image.load("Graphics/PurpleBaddie2.png").convert_alpha()
PurpleBaddie2 = pygame.transform.scale(PurpleBaddie2, (40, 30))

GreenBaddie1 = pygame.image.load("Graphics/GreenBaddie1.png").convert_alpha()
GreenBaddie1 = pygame.transform.scale(GreenBaddie1, (35, 35))
GreenBaddie2 = pygame.image.load("Graphics/GreenBaddie2.png").convert_alpha()
GreenBaddie2 = pygame.transform.scale(GreenBaddie2, (35, 35))

RedBaddie1 = pygame.image.load("Graphics/RedBaddie1.png").convert_alpha()
RedBaddie1 = pygame.transform.scale(RedBaddie1, (35, 35))
RedBaddie2 = pygame.image.load("Graphics/RedBaddie2.png").convert_alpha()
RedBaddie2 = pygame.transform.scale(RedBaddie2, (35, 35))

GoodGuy = pygame.image.load("Graphics/GoodGuy.png").convert_alpha()
GoodGuy = pygame.transform.scale(GoodGuy, (40, 30))

bullet_img = pygame.image.load("Graphics/bullet.jpg").convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (5, 5))

shield_img = pygame.image.load("Graphics/shield.jpeg").convert_alpha()
shield_img = pygame.transform.scale(shield_img, (80, 65))

BIGALIEN = pygame.image.load("Graphics/BIGALIEN.png").convert_alpha()
BIGALIEN = pygame.transform.scale(BIGALIEN, (80, 40))

BG2 = pygame.image.load("Graphics/Space Background.jpg").convert_alpha()

# ======== HOMEPAGE STUFF =========
homepagett = font.render("HOMEPAGE", False, (255, 0, 0))
hpselect1 = font.render("1  Play", False, (255, 0, 0))
hpselect2 = font.render("2  Stats   STILL PENDING", False, (255, 0, 0))
hpselect3 = font.render("3  GAME   MANUAL", False, (255, 0, 0))
hpselect4 = font.render("4  TIPS   AND   TRICKS", False, (255, 0, 0,))
hpselect5 = font.render("5  Credits", False, (255, 0, 0))
exitpg = font.render("Press   E   to   exit", False, (255, 0, 0))

credittxt = font.render("CREDITS", False, (255, 0, 0))
credittxt1 = font.render("CONCEPT   BY   MIKAIL AKAR", False, (255, 0, 0))
credittxt2 = font.render("PROGRAMMED   BY   MIKAIL AKAR", False, (255, 0, 0))
credittxt3 = font.render("GAME   TESTED   BY   FATIH   AKAR", False, (255, 0, 0))
credittxt4 = font.render("GAME   TESTED   BY   BURCU   AKAR", False, (255, 0, 0))
credittxt5 = font.render("SPECIAL   MENTIONS", False, (255, 0, 0))
credittxt6 = font.render("THANK   YOU   FOR   PLAYING  !", False, (255, 0, 0))

one = font.render('1', False, (255, 0, 0))
two = font.render('2', False, (255, 0, 0))
three = font.render('3', False, (255, 0, 0))
four = font.render('4', False, (255, 0, 0))
five = font.render('5', False, (255, 0, 0))
six = font.render('6', False, (255, 0, 0))
seven = font.render('7', False, (255, 0, 0))
eight = font.render('8', False, (255, 0, 0))

SISTARTTEXT = font.render('SPACE INVADERS', False, (255, 0, 0))
SISTARTTEXT2 = font.render('SHOOT ALIEN   TO   START', False, (255, 0, 0))
level1endtext1 = font.render('LEVEL   1   C LE A R E D  !', False, (255, 0, 0))
level1endtext2 = font.render('Press   x    to  continue', False, (255, 0, 0))
level2endtext1 = font.render("LEVEL   2   C LE A R E D  !", False, (255, 0, 0))
level2endtext2 = font.render('Press   x    to  continue', False, (255, 0, 0))
level3endtext1 = font.render('LEVEL   3   C LE A R E D  !', False, (255, 0, 0))
level4endtext1 = font.render('LEVEL   4   C LE A R E D  !', False, (255, 0, 0))
level5endtext1 = font.render('LEVEL   5   C LE A R E D  !', False, (255, 0, 0))
level6endtext1 = font.render('LEVEL   6   C LE A R E D  !', False, (255, 0, 0))
level7endtext1 = font.render('LEVEL   7   C LE A R E D  !', False, (255, 0, 0))

shieldunlocktext1 = font.render('SHIELD   UNLOCKED', False, (255, 0, 0))
shieldunlocktext2 = font.render("Press   z   to  continue", False, (255, 0, 0))
shootbacktext = font.render("ALIEN   ATTACK   UNLOCKED", False, (255, 0, 0))
bigalientext1 = font.render("MYSTERY   ALIEN   UNLOCKED", False, (255, 0, 0))
homepageunlockedtext1 = font.render("YOU   HAVE UNLOCKED   THE HOMEPAGE", False, (255, 0, 0))
homepageunlockedtext2 = font.render("ENJOY   A   PROPER   UI", False, (255, 0, 0))
yourbad = font.render("YOU   DIED", False, (255, 0, 0))
yourbad2 = font.render("Press   Z   TO RESTART", False, (255, 0, 0))
leveltext = font.render('LEVEL ', False, (255, 5, 0))
leveltext = pygame.transform.scale(leveltext, (100, 40))



def page5():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        screen.fill("black")
        screen.blit(credittxt1, (10, 85))
        screen.blit(credittxt2, (10, 135))
        screen.blit(credittxt3, (10, 185))
        screen.blit(credittxt4, (10, 235))
        screen.blit(credittxt5, (10, 285))
        screen.blit(credittxt6, (10, 335))
        if keys[pygame.K_z]:
            homepage0()
            y += 1
        pygame.display.update()
        clock.tick(FPS)


def page1():
    print("hello")


def homepage0():
    y = 0
    global level
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        screen.fill("black")
        screen.blit(exitpg, (10, 625))
        screen.blit(homepagett, (10, 0))
        screen.blit(hpselect1, (10, 85))
        screen.blit(hpselect2, (10, 135))
        screen.blit(hpselect3, (10, 185))
        screen.blit(hpselect4, (10, 235))
        screen.blit(hpselect5, (10, 285))
        if keys[pygame.K_e]:
            y += 1
            exit()
        if keys[pygame.K_1]:
            if level == 6:
                level6()
                y += 1
            if level == 7:
                level7()
                y += 1
        if keys[pygame.K_5]:
            page5()
            y += 1
        pygame.display.update()
        clock.tick(FPS)


def homepageunlocked():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        screen.fill("black")
        screen.blit(homepageunlockedtext1, (10, 200))
        screen.blit(homepageunlockedtext2, (165, 350))
        screen.blit(shieldunlocktext2, (165, 500))
        if keys[pygame.K_z]:
            homepage0()
            y += 1
        pygame.display.update()
        clock.tick(FPS)


def level7end():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        screen.fill("black")
        screen.blit(level2endtext2, (165, 400))
        screen.blit(level7endtext1, (165, 100))
        if keys[pygame.K_x]:
            homepage0()
            y += 1
        pygame.display.update()
        clock.tick(FPS)


def level7():
    import random

    # === Game variables ===
    st8()
    lvl7 = 0
    bullets = []
    bullet_speed = -7
    last_shot = 0
    shoot_delay = 300
    badmove1 = 0
    badmovefunc1 = 0
    GOODGUYSPEED = 4
    killcount = 0
    FPS = 60
    big_alien_active = False
    big_alien_rect = BIGALIEN.get_rect(midtop=(-100, 40))  # start off-screen
    big_alien_speed = 3
    last_big_alien = 0
    big_alien_delay = 15000  # appears every 15 seconds
    # Alien shooting
    alien_bullets = []
    ALIEN_BULLET_SPEED = 5  # moves downward
    alien_shoot_delay = 1000  # ms
    last_alien_shot = 0
    alien_bullet_img = pygame.Surface((5, 10))
    alien_bullet_img.fill((255, 255, 255))

    # === Alien Generation ===
    PurpleBaddies, GreenBaddies, RedBaddies = [], [], []

    # Big Alien
    now = pygame.time.get_ticks()
    # Purple
    startxp, startyp, pbycount = 107, 105, 0
    for i in range(20):
        PurpleBaddies.append(PurpleBaddie2.get_rect(midtop=(startxp, startyp)))
        startxp += 62
        pbycount += 1
        if pbycount == 10:
            startyp += 50
            startxp = 107

    # Green
    startxg, startyg, gbycount = 107, 205, 0
    for i in range(20):
        GreenBaddies.append(GreenBaddie2.get_rect(midtop=(startxg, startyg)))
        startxg += 62
        gbycount += 1
        if gbycount == 10:
            startyg += 50
            startxg = 107

    # Red
    startxr, startyr, rbycount = 107, 305, 0
    for i in range(20):
        RedBaddies.append(RedBaddie2.get_rect(midtop=(startxr, startyr)))
        startxr += 62
        rbycount += 1
        if rbycount == 10:
            startyr += 50
            startxr = 107

    while lvl7 == 0:
        screen.fill("Black")
        screen.blit(BG2, (0, 0))

        # === Housekeeping ===
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            GOODGUYSPEED += 4
        if keys[pygame.K_a]:
            GOODGUYSPEED -= 4

        now = pygame.time.get_ticks()

        # === BIG ALIEN SPAWN ===
        if not big_alien_active and now - last_big_alien > big_alien_delay:
            big_alien_active = True
            big_alien_rect.x = -100
            last_big_alien = now

        # === BIG ALIEN MOVE ===
        if big_alien_active:
            big_alien_rect.x += big_alien_speed
            if big_alien_rect.left > WIDTH:
                big_alien_active = False

        # === Player ===
        GoodGuyrect = GoodGuy.get_rect(topleft=(GOODGUYSPEED, 670))

        # === Player shooting ===
        if keys[pygame.K_w] and now - last_shot > shoot_delay:
            bullets.append(bullet_img.get_rect(midbottom=GoodGuyrect.midtop))
            last_shot = now

        # === Player bullets ===
        for bullet in bullets[:]:
            bullet.y += bullet_speed

            if bullet.bottom < 0:
                bullets.remove(bullet)
                continue

            #  BIG ALIEN HIT (FIXED LOCATION)
            if big_alien_active and big_alien_rect.colliderect(bullet):
                bullets.remove(bullet)
                big_alien_active = False
                killcount += 5
                continue

            # Bunker collision
            for block in bunkers[:]:
                if block.colliderect(bullet):
                    bullets.remove(bullet)
                    bunkers.remove(block)
                    break

            # Alien collision
            for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                for alien in alien_list[:]:
                    if alien.colliderect(bullet):
                        bullets.remove(bullet)
                        alien_list.remove(alien)
                        killcount += 1
                        break
                else:
                    continue
                break

        # === Alien shooting ===
        if now - last_alien_shot > alien_shoot_delay and (PurpleBaddies or GreenBaddies or RedBaddies):
            all_aliens = PurpleBaddies + GreenBaddies + RedBaddies
            shooter = random.choice(all_aliens)
            alien_bullets.append(pygame.Rect(shooter.centerx, shooter.bottom, 5, 10))
            last_alien_shot = now

        # === Alien bullets ===
        for bullet in alien_bullets[:]:
            bullet.y += ALIEN_BULLET_SPEED

            if bullet.top > HEIGHT:
                alien_bullets.remove(bullet)
                continue

            if bullet.colliderect(GoodGuyrect):
                alien_bullets.remove(bullet)
                looser()

            for block in bunkers[:]:
                if block.colliderect(bullet):
                    alien_bullets.remove(bullet)
                    bunkers.remove(block)
                    break

        # === Draw bunkers ===
        for block in bunkers:
            pygame.draw.rect(screen, (0, 255, 0), block)

        # === Draw aliens ===
        for alien in PurpleBaddies:
            screen.blit(PurpleBaddie2, alien)
        for alien in GreenBaddies:
            screen.blit(GreenBaddie2, alien)
        for alien in RedBaddies:
            screen.blit(RedBaddie2, alien)

        # === Draw BIG ALIEN ===
        if big_alien_active:
            screen.blit(BIGALIEN, big_alien_rect)

        # === Draw bullets ===
        for bullet in bullets:
            screen.blit(bullet_img, bullet)
        for bullet in alien_bullets:
            screen.blit(alien_bullet_img, bullet)

        # === Draw player ===
        screen.blit(GoodGuy, GoodGuyrect)
        screen.blit(leveltext, (10, 0))
        screen.blit(seven, (110, 0))

        # === Alien movement (unchanged) ===
        badmove1 += 1
        if badmove1 % 120 == 0:
            if badmovefunc1 == 0:
                badmovefunc1 = 1
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.x += 30
            elif badmovefunc1 == 1:
                badmovefunc1 = 2
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.y += 30
            elif badmovefunc1 == 2:
                badmovefunc1 = 3
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.x -= 30
            elif badmovefunc1 == 3:
                badmovefunc1 = 0
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.y -= 30

        if killcount == 60:
            level7end()

            lvl7 += 1

        pygame.display.update()
        clock.tick(FPS)

    pygame.display.update()
    clock.tick(FPS)


def level6end():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        screen.fill("black")
        screen.blit(level2endtext2, (165, 400))
        screen.blit(level6endtext1, (165, 100))
        if keys[pygame.K_x]:
            homepage0()
            y += 1
        pygame.display.update()
        clock.tick(FPS)


def level6():
    import random

    # === Game variables ===
    st7()
    lvl6 = 0
    bullets = []
    bullet_speed = -7
    last_shot = 0
    shoot_delay = 300
    badmove1 = 0
    badmovefunc1 = 0
    GOODGUYSPEED = 4
    killcount = 0
    FPS = 60
    big_alien_active = False
    big_alien_rect = BIGALIEN.get_rect(midtop=(-100, 40))  # start off-screen
    big_alien_speed = 3
    last_big_alien = 0
    big_alien_delay = 15000  # appears every 15 seconds
    # Alien shooting
    alien_bullets = []
    ALIEN_BULLET_SPEED = 5  # moves downward
    alien_shoot_delay = 1000  # ms
    last_alien_shot = 0
    alien_bullet_img = pygame.Surface((5, 10))
    alien_bullet_img.fill((255, 255, 255))

    # === Alien Generation ===
    PurpleBaddies, GreenBaddies, RedBaddies = [], [], []

    # Big Alien
    now = pygame.time.get_ticks()
    # Purple
    startxp, startyp, pbycount = 107, 105, 0
    for i in range(20):
        PurpleBaddies.append(PurpleBaddie2.get_rect(midtop=(startxp, startyp)))
        startxp += 62
        pbycount += 1
        if pbycount == 10:
            startyp += 50
            startxp = 107

    # Green
    startxg, startyg, gbycount = 107, 205, 0
    for i in range(20):
        GreenBaddies.append(GreenBaddie2.get_rect(midtop=(startxg, startyg)))
        startxg += 62
        gbycount += 1
        if gbycount == 10:
            startyg += 50
            startxg = 107

    # Red
    startxr, startyr, rbycount = 107, 305, 0
    for i in range(20):
        RedBaddies.append(RedBaddie2.get_rect(midtop=(startxr, startyr)))
        startxr += 62
        rbycount += 1
        if rbycount == 10:
            startyr += 50
            startxr = 107

    while lvl6 == 0:
        screen.fill("black")

        # === Housekeeping ===
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            GOODGUYSPEED += 4
        if keys[pygame.K_a]:
            GOODGUYSPEED -= 4

        now = pygame.time.get_ticks()

        # === BIG ALIEN SPAWN ===
        if not big_alien_active and now - last_big_alien > big_alien_delay:
            big_alien_active = True
            big_alien_rect.x = -100
            last_big_alien = now

        # === BIG ALIEN MOVE ===
        if big_alien_active:
            big_alien_rect.x += big_alien_speed
            if big_alien_rect.left > WIDTH:
                big_alien_active = False

        # === Player ===
        GoodGuyrect = GoodGuy.get_rect(topleft=(GOODGUYSPEED, 670))

        # === Player shooting ===
        if keys[pygame.K_w] and now - last_shot > shoot_delay:
            bullets.append(bullet_img.get_rect(midbottom=GoodGuyrect.midtop))
            last_shot = now

        # === Player bullets ===
        for bullet in bullets[:]:
            bullet.y += bullet_speed

            if bullet.bottom < 0:
                bullets.remove(bullet)
                continue

            #  BIG ALIEN HIT (FIXED LOCATION)
            if big_alien_active and big_alien_rect.colliderect(bullet):
                bullets.remove(bullet)
                big_alien_active = False
                killcount += 5
                continue

            # Bunker collision
            for block in bunkers[:]:
                if block.colliderect(bullet):
                    bullets.remove(bullet)
                    bunkers.remove(block)
                    break

            # Alien collision
            for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                for alien in alien_list[:]:
                    if alien.colliderect(bullet):
                        bullets.remove(bullet)
                        alien_list.remove(alien)
                        killcount += 1
                        break
                else:
                    continue
                break

        # === Alien shooting ===
        if now - last_alien_shot > alien_shoot_delay and (PurpleBaddies or GreenBaddies or RedBaddies):
            all_aliens = PurpleBaddies + GreenBaddies + RedBaddies
            shooter = random.choice(all_aliens)
            alien_bullets.append(pygame.Rect(shooter.centerx, shooter.bottom, 5, 10))
            last_alien_shot = now

        # === Alien bullets ===
        for bullet in alien_bullets[:]:
            bullet.y += ALIEN_BULLET_SPEED

            if bullet.top > HEIGHT:
                alien_bullets.remove(bullet)
                continue

            if bullet.colliderect(GoodGuyrect):
                alien_bullets.remove(bullet)
                looser()

            for block in bunkers[:]:
                if block.colliderect(bullet):
                    alien_bullets.remove(bullet)
                    bunkers.remove(block)
                    break

        # === Draw bunkers ===
        for block in bunkers:
            pygame.draw.rect(screen, (0, 255, 0), block)

        # === Draw aliens ===
        for alien in PurpleBaddies:
            screen.blit(PurpleBaddie2, alien)
        for alien in GreenBaddies:
            screen.blit(GreenBaddie2, alien)
        for alien in RedBaddies:
            screen.blit(RedBaddie2, alien)

        # === Draw BIG ALIEN ===
        if big_alien_active:
            screen.blit(BIGALIEN, big_alien_rect)

        # === Draw bullets ===
        for bullet in bullets:
            screen.blit(bullet_img, bullet)
        for bullet in alien_bullets:
            screen.blit(alien_bullet_img, bullet)

        # === Draw player ===
        screen.blit(GoodGuy, GoodGuyrect)
        screen.blit(leveltext, (10, 0))
        screen.blit(six, (110, 0))

        # === Alien movement (unchanged) ===
        badmove1 += 1
        if badmove1 % 120 == 0:
            if badmovefunc1 == 0:
                badmovefunc1 = 1
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.x += 30
            elif badmovefunc1 == 1:
                badmovefunc1 = 2
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.y += 30
            elif badmovefunc1 == 2:
                badmovefunc1 = 3
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.x -= 30
            elif badmovefunc1 == 3:
                badmovefunc1 = 0
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.y -= 30

        if killcount == 60:
            level6end()
            lvl6 += 1

        pygame.display.update()
        clock.tick(FPS)

    pygame.display.update()
    clock.tick(FPS)


def level5end():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        screen.fill("black")
        screen.blit(level2endtext2, (165, 400))
        screen.blit(level5endtext1, (165, 100))
        if keys[pygame.K_x]:
            homepageunlocked()
            y += 1
        pygame.display.update()
        clock.tick(FPS)


def level5():
    import random

    # === Game variables ===
    lvl5 = 0
    bullets = []
    bullet_speed = -7
    last_shot = 0
    shoot_delay = 300
    badmove1 = 0
    badmovefunc1 = 0
    GOODGUYSPEED = 4
    killcount = 0
    FPS = 60
    big_alien_active = False
    big_alien_rect = BIGALIEN.get_rect(midtop=(-100, 40))  # start off-screen
    big_alien_speed = 3
    last_big_alien = 0
    big_alien_delay = 15000  # appears every 15 seconds
    # Alien shooting
    alien_bullets = []
    ALIEN_BULLET_SPEED = 5  # moves downward
    alien_shoot_delay = 1000  # ms
    last_alien_shot = 0
    alien_bullet_img = pygame.Surface((5, 10))
    alien_bullet_img.fill((255, 255, 255))

    # === Alien Generation ===
    PurpleBaddies, GreenBaddies, RedBaddies = [], [], []

    # Big Alien
    now = pygame.time.get_ticks()
    # Purple
    startxp, startyp, pbycount = 107, 105, 0
    for i in range(20):
        PurpleBaddies.append(PurpleBaddie1.get_rect(midtop=(startxp, startyp)))
        startxp += 62
        pbycount += 1
        if pbycount == 10:
            startyp += 50
            startxp = 107

    # Green
    startxg, startyg, gbycount = 107, 205, 0
    for i in range(20):
        GreenBaddies.append(GreenBaddie1.get_rect(midtop=(startxg, startyg)))
        startxg += 62
        gbycount += 1
        if gbycount == 10:
            startyg += 50
            startxg = 107

    # Red
    startxr, startyr, rbycount = 107, 305, 0
    for i in range(20):
        RedBaddies.append(RedBaddie1.get_rect(midtop=(startxr, startyr)))
        startxr += 62
        rbycount += 1
        if rbycount == 10:
            startyr += 50
            startxr = 107

    while lvl5 == 0:
        screen.fill("black")

        # === Housekeeping ===
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            GOODGUYSPEED += 4
        if keys[pygame.K_a]:
            GOODGUYSPEED -= 4

        now = pygame.time.get_ticks()

        # === BIG ALIEN SPAWN ===
        if not big_alien_active and now - last_big_alien > big_alien_delay:
            big_alien_active = True
            big_alien_rect.x = -100
            last_big_alien = now

        # === BIG ALIEN MOVE ===
        if big_alien_active:
            big_alien_rect.x += big_alien_speed
            if big_alien_rect.left > WIDTH:
                big_alien_active = False

        # === Player ===
        GoodGuyrect = GoodGuy.get_rect(topleft=(GOODGUYSPEED, 670))

        # === Player shooting ===
        if keys[pygame.K_w] and now - last_shot > shoot_delay:
            bullets.append(bullet_img.get_rect(midbottom=GoodGuyrect.midtop))
            last_shot = now

        # === Player bullets ===
        for bullet in bullets[:]:
            bullet.y += bullet_speed

            if bullet.bottom < 0:
                bullets.remove(bullet)
                continue

            #  BIG ALIEN HIT (FIXED LOCATION)
            if big_alien_active and big_alien_rect.colliderect(bullet):
                bullets.remove(bullet)
                big_alien_active = False
                killcount += 5
                continue

            # Bunker collision
            for block in bunkers[:]:
                if block.colliderect(bullet):
                    bullets.remove(bullet)
                    bunkers.remove(block)
                    break

            # Alien collision
            for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                for alien in alien_list[:]:
                    if alien.colliderect(bullet):
                        bullets.remove(bullet)
                        alien_list.remove(alien)
                        killcount += 1
                        break
                else:
                    continue
                break

        # === Alien shooting ===
        if now - last_alien_shot > alien_shoot_delay and (PurpleBaddies or GreenBaddies or RedBaddies):
            all_aliens = PurpleBaddies + GreenBaddies + RedBaddies
            shooter = random.choice(all_aliens)
            alien_bullets.append(pygame.Rect(shooter.centerx, shooter.bottom, 5, 10))
            last_alien_shot = now

        # === Alien bullets ===
        for bullet in alien_bullets[:]:
            bullet.y += ALIEN_BULLET_SPEED

            if bullet.top > HEIGHT:
                alien_bullets.remove(bullet)
                continue

            if bullet.colliderect(GoodGuyrect):
                alien_bullets.remove(bullet)
                looser()

            for block in bunkers[:]:
                if block.colliderect(bullet):
                    alien_bullets.remove(bullet)
                    bunkers.remove(block)
                    break

        # === Draw bunkers ===
        for block in bunkers:
            pygame.draw.rect(screen, (0, 255, 0), block)

        # === Draw aliens ===
        for alien in PurpleBaddies:
            screen.blit(PurpleBaddie1, alien)
        for alien in GreenBaddies:
            screen.blit(GreenBaddie1, alien)
        for alien in RedBaddies:
            screen.blit(RedBaddie1, alien)

        # === Draw BIG ALIEN ===
        if big_alien_active:
            screen.blit(BIGALIEN, big_alien_rect)

        # === Draw bullets ===
        for bullet in bullets:
            screen.blit(bullet_img, bullet)
        for bullet in alien_bullets:
            screen.blit(alien_bullet_img, bullet)

        # === Draw player ===
        screen.blit(GoodGuy, GoodGuyrect)
        screen.blit(leveltext, (10, 0))
        screen.blit(five, (110, 0))

        # === Alien movement (unchanged) ===
        badmove1 += 1
        if badmove1 % 120 == 0:
            if badmovefunc1 == 0:
                badmovefunc1 = 1
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.x += 30
            elif badmovefunc1 == 1:
                badmovefunc1 = 2
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.y += 30
            elif badmovefunc1 == 2:
                badmovefunc1 = 3
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.x -= 30
            elif badmovefunc1 == 3:
                badmovefunc1 = 0
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.y -= 30

        if killcount == 60:
            level5end()
            lvl5 += 1

        pygame.display.update()
        clock.tick(FPS)

    pygame.display.update()
    clock.tick(FPS)


def bigalien():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        screen.fill("black")
        screen.blit(bigalientext1, (125, 100))
        screen.blit(shieldunlocktext2, (165, 400))
        if keys[pygame.K_z]:
            level5()
            y += 1
        pygame.display.update()
        clock.tick(FPS)


def level4end():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        screen.fill("black")
        screen.blit(level2endtext2, (165, 400))
        screen.blit(level4endtext1, (165, 100))
        if keys[pygame.K_x]:
            bigalien()
            y += 1
        pygame.display.update()
        clock.tick(FPS)


def level4():
    import random

    # === Game variables ===
    lvl3 = 0
    bullets = []
    bullet_speed = -7
    last_shot = 0
    shoot_delay = 300
    badmove1 = 0
    badmovefunc1 = 0
    GOODGUYSPEED = 4
    killcount = 0
    FPS = 60

    # Alien shooting
    alien_bullets = []
    ALIEN_BULLET_SPEED = 5  # moves downward
    alien_shoot_delay = 1000  # ms
    last_alien_shot = 0
    alien_bullet_img = pygame.Surface((5, 10))
    alien_bullet_img.fill((255, 255, 255))

    # === Alien Generation ===
    PurpleBaddies, GreenBaddies, RedBaddies = [], [], []

    # Purple
    startxp, startyp, pbycount = 107, 105, 0
    for i in range(20):
        PurpleBaddies.append(PurpleBaddie1.get_rect(midtop=(startxp, startyp)))
        startxp += 62
        pbycount += 1
        if pbycount == 10:
            startyp += 50
            startxp = 107

    # Green
    startxg, startyg, gbycount = 107, 205, 0
    for i in range(20):
        GreenBaddies.append(GreenBaddie1.get_rect(midtop=(startxg, startyg)))
        startxg += 62
        gbycount += 1
        if gbycount == 10:
            startyg += 50
            startxg = 107

    # Red
    startxr, startyr, rbycount = 107, 305, 0
    for i in range(20):
        RedBaddies.append(RedBaddie1.get_rect(midtop=(startxr, startyr)))
        startxr += 62
        rbycount += 1
        if rbycount == 10:
            startyr += 50
            startxr = 107

    while lvl3 == 0:
        screen.fill("black")

        # === Housekeeping ===
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            GOODGUYSPEED += 4
        if keys[pygame.K_a]:
            GOODGUYSPEED -= 4

        # === Player shooting ===
        now = pygame.time.get_ticks()
        GoodGuyrect = GoodGuy.get_rect(topleft=(GOODGUYSPEED, 670))
        if keys[pygame.K_w] and now - last_shot > shoot_delay:
            bullets.append(bullet_img.get_rect(midbottom=GoodGuyrect.midtop))
            last_shot = now

        # === Player bullets ===
        for bullet in bullets[:]:
            bullet.y += bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)
                continue

            # Bunker collision
            for block in bunkers[:]:
                if block.colliderect(bullet):
                    bullets.remove(bullet)
                    bunkers.remove(block)
                    break

            # Alien collision
            for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                for alien in alien_list[:]:
                    if alien.colliderect(bullet):
                        bullets.remove(bullet)
                        alien_list.remove(alien)
                        killcount += 1
                        break
                else:
                    continue
                break

        # === Alien shooting ===
        if now - last_alien_shot > alien_shoot_delay and (PurpleBaddies or GreenBaddies or RedBaddies):
            all_aliens = PurpleBaddies + GreenBaddies + RedBaddies
            shooter = random.choice(all_aliens)
            alien_bullets.append(pygame.Rect(shooter.centerx, shooter.bottom, 5, 10))
            last_alien_shot = now

        # === Alien bullets ===
        for bullet in alien_bullets[:]:
            bullet.y += ALIEN_BULLET_SPEED
            if bullet.top > HEIGHT:
                alien_bullets.remove(bullet)
                continue

            # Player collision
            if bullet.colliderect(GoodGuyrect):
                alien_bullets.remove(bullet)
                looser()
                # handle player life/game over here

            # Bunker collision
            for block in bunkers[:]:
                if block.colliderect(bullet):
                    alien_bullets.remove(bullet)
                    bunkers.remove(block)
                    break

        # === Draw bunkers ===
        for block in bunkers:
            pygame.draw.rect(screen, (0, 255, 0), block)

        # === Draw aliens ===
        for alien in PurpleBaddies:
            screen.blit(PurpleBaddie1, alien)
        for alien in GreenBaddies:
            screen.blit(GreenBaddie1, alien)
        for alien in RedBaddies:
            screen.blit(RedBaddie1, alien)

        # === Draw bullets ===
        for bullet in bullets:
            screen.blit(bullet_img, bullet)
        for bullet in alien_bullets:
            screen.blit(alien_bullet_img, bullet)

        # === Draw player ===
        screen.blit(GoodGuy, GoodGuyrect)
        screen.blit(leveltext, (10, 0))
        screen.blit(four, (110, 0))
        # === Alien movement ===
        badmove1 += 1
        if badmove1 % 120 == 0:
            if badmovefunc1 == 0:
                badmovefunc1 = 1
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.x += 30
            elif badmovefunc1 == 1:
                badmovefunc1 = 2
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.y += 30
            elif badmovefunc1 == 2:
                badmovefunc1 = 3
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.x -= 30
            elif badmovefunc1 == 3:
                badmovefunc1 = 0
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.y -= 30

        if killcount == 60:
            level4end()
            lvl3 += 1

        pygame.display.update()
        clock.tick(FPS)


def looser():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        screen.fill("black")
        screen.blit(yourbad, (275, 200))
        screen.blit(yourbad2, (175, 500))
        if keys[pygame.K_z]:
            level1()
            y += 1
        pygame.display.update()
        clock.tick(FPS)


def level3end():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        screen.fill("black")
        screen.blit(level3endtext1, (165, 150))
        screen.blit(level2endtext2, (165, 400))
        if keys[pygame.K_x]:
            level4()
            y += 1
        pygame.display.update()
        clock.tick(FPS)


def level3():
    import random

    # === Game variables ===
    lvl3 = 0
    bullets = []
    bullet_speed = -7
    last_shot = 0
    shoot_delay = 300
    badmove1 = 0
    badmovefunc1 = 0
    GOODGUYSPEED = 4
    killcount = 0
    FPS = 60

    # Alien shooting
    alien_bullets = []
    ALIEN_BULLET_SPEED = 5  # moves downward
    alien_shoot_delay = 1000  # ms
    last_alien_shot = 0
    alien_bullet_img = pygame.Surface((5, 10))
    alien_bullet_img.fill((255, 255, 255))

    # === Alien Generation ===
    PurpleBaddies, GreenBaddies, RedBaddies = [], [], []

    # Purple
    startxp, startyp, pbycount = 107, 105, 0
    for i in range(20):
        PurpleBaddies.append(PurpleBaddie1.get_rect(midtop=(startxp, startyp)))
        startxp += 62
        pbycount += 1
        if pbycount == 10:
            startyp += 50
            startxp = 107

    # Green
    startxg, startyg, gbycount = 107, 205, 0
    for i in range(20):
        GreenBaddies.append(GreenBaddie1.get_rect(midtop=(startxg, startyg)))
        startxg += 62
        gbycount += 1
        if gbycount == 10:
            startyg += 50
            startxg = 107

    # Red
    startxr, startyr, rbycount = 107, 305, 0
    for i in range(20):
        RedBaddies.append(RedBaddie1.get_rect(midtop=(startxr, startyr)))
        startxr += 62
        rbycount += 1
        if rbycount == 10:
            startyr += 50
            startxr = 107

    while lvl3 == 0:
        screen.fill("black")

        # === Housekeeping ===
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            GOODGUYSPEED += 4
        if keys[pygame.K_a]:
            GOODGUYSPEED -= 4

        # === Player shooting ===
        now = pygame.time.get_ticks()
        GoodGuyrect = GoodGuy.get_rect(topleft=(GOODGUYSPEED, 670))
        if keys[pygame.K_w] and now - last_shot > shoot_delay:
            bullets.append(bullet_img.get_rect(midbottom=GoodGuyrect.midtop))
            last_shot = now

        # === Player bullets ===
        for bullet in bullets[:]:
            bullet.y += bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)
                continue

            # Bunker collision
            for block in bunkers[:]:
                if block.colliderect(bullet):
                    bullets.remove(bullet)
                    bunkers.remove(block)
                    break

            # Alien collision
            for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                for alien in alien_list[:]:
                    if alien.colliderect(bullet):
                        bullets.remove(bullet)
                        alien_list.remove(alien)
                        killcount += 1
                        break
                else:
                    continue
                break

        # === Alien shooting ===
        if now - last_alien_shot > alien_shoot_delay and (PurpleBaddies or GreenBaddies or RedBaddies):
            all_aliens = PurpleBaddies + GreenBaddies + RedBaddies
            shooter = random.choice(all_aliens)
            alien_bullets.append(pygame.Rect(shooter.centerx, shooter.bottom, 5, 10))
            last_alien_shot = now

        # === Alien bullets ===
        for bullet in alien_bullets[:]:
            bullet.y += ALIEN_BULLET_SPEED
            if bullet.top > HEIGHT:
                alien_bullets.remove(bullet)
                continue

            # Player collision
            if bullet.colliderect(GoodGuyrect):
                alien_bullets.remove(bullet)
                looser()
                # handle player life/game over here

            # Bunker collision
            for block in bunkers[:]:
                if block.colliderect(bullet):
                    alien_bullets.remove(bullet)
                    bunkers.remove(block)
                    break

        # === Draw bunkers ===
        for block in bunkers:
            pygame.draw.rect(screen, (0, 255, 0), block)

        # === Draw aliens ===
        for alien in PurpleBaddies:
            screen.blit(PurpleBaddie1, alien)
        for alien in GreenBaddies:
            screen.blit(GreenBaddie1, alien)
        for alien in RedBaddies:
            screen.blit(RedBaddie1, alien)

        # === Draw bullets ===
        for bullet in bullets:
            screen.blit(bullet_img, bullet)
        for bullet in alien_bullets:
            screen.blit(alien_bullet_img, bullet)

        # === Draw player ===
        screen.blit(GoodGuy, GoodGuyrect)
        screen.blit(leveltext, (10, 0))
        screen.blit(three, (110, 0))

        # === Alien movement ===
        badmove1 += 1
        if badmove1 % 120 == 0:
            if badmovefunc1 == 0:
                badmovefunc1 = 1
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.x += 30
            elif badmovefunc1 == 1:
                badmovefunc1 = 2
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.y += 30
            elif badmovefunc1 == 2:
                badmovefunc1 = 3
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.x -= 30
            elif badmovefunc1 == 3:
                badmovefunc1 = 0
                for alien_list in [PurpleBaddies, GreenBaddies, RedBaddies]:
                    for alien in alien_list:
                        alien.y -= 30

        if killcount == 60:
            level3end()
            lvl3 += 1

        pygame.display.update()
        clock.tick(FPS)


def shootback():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill('black')
        screen.blit(shootbacktext, (100, 150))
        screen.blit(level2endtext2, (165, 400))
        key = pygame.key.get_pressed()
        if key[pygame.K_x]:
            level3()
            y += 1

        pygame.display.update()
        clock.tick(FPS)


def shield():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill('black')
        screen.blit(shieldunlocktext1, (200, 150))
        screen.blit(shield_img, (350, 350))
        screen.blit(shieldunlocktext2, (165, 500))
        key = pygame.key.get_pressed()
        if key[pygame.K_z]:
            shootback()
            y += 1

        pygame.display.update()
        clock.tick(FPS)


def level2end():
    y = 0
    while y == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill('black')
        screen.blit(level2endtext1, (165, 150))
        screen.blit(level2endtext2, (165, 400))
        key = pygame.key.get_pressed()
        if key[pygame.K_x]:
            shield()
            y += 1

        pygame.display.update()
        clock.tick(FPS)


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
    MOVEON = 1
    # Alien Generation
    PurpleBaddies = []
    startxp = 107
    startyp = 105
    pbycount = 0
    for i in range(20):
        PurpleBaddies.append(PurpleBaddie1.get_rect(midtop=(startxp, startyp)))
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
        GreenBaddies.append(GreenBaddie1.get_rect(midtop=(startxg, startyg)))
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
        RedBaddies.append(RedBaddie1.get_rect(midtop=(startxr, startyr)))
        startxr += 62
        rbycount += 1
        if rbycount == 10:
            startyr += 50
            startxr = 107
    while lvl2 == 0:

        # Housekeeping
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill("black")

        # GoodGuy Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            GOODGUYSPEED += 4
        if keys[pygame.K_a]:
            GOODGUYSPEED -= 4

        # Bullet Generation
        now = pygame.time.get_ticks()
        if keys[pygame.K_w] and now - last_shot > shoot_delay:
            bullets.append(bullet_img.get_rect(midbottom=GoodGuyrect.midtop))
            last_shot = now

        # Bullet collision / bullet deletion
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
                    break
            else:
                for alien in GreenBaddies[:]:
                    if alien.colliderect(bullet):
                        bullets.remove(bullet)
                        GreenBaddies.remove(alien)
                        killcount += 1
                        break
                else:
                    for alien in RedBaddies[:]:
                        if alien.colliderect(bullet):
                            bullets.remove(bullet)
                            RedBaddies.remove(alien)
                            killcount += 1
                            break

        # Alien Drawing -> bullet drawing
        for alien in PurpleBaddies:
            screen.blit(PurpleBaddie1, alien)
        for alien in GreenBaddies:
            screen.blit(GreenBaddie1, alien)
        for alien in RedBaddies:
            screen.blit(RedBaddie1, alien)
        for bullet in bullets:
            screen.blit(bullet_img, bullet)
        GoodGuyrect = GoodGuy.get_rect(topleft=(GOODGUYSPEED, 670))
        screen.blit(GoodGuy, GoodGuyrect)
        screen.blit(leveltext, (10, 0))
        screen.blit(two, (110, 0))

        # Alien Movement
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
        if killcount == 60:
            lvl2 += 1
            level2end()
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
        screen.blit(level1endtext1, (165, 150))
        screen.blit(level1endtext2, (165, 400))
        key = pygame.key.get_pressed()
        if key[pygame.K_x]:
            level2()
            y += 1

        pygame.display.update()
        clock.tick(FPS)


def level1():
    MOVEON = 1
    GoodGuyrect = GoodGuy.get_rect(topleft=(0, 670))
    PurpleBaddie1rect = PurpleBaddie1.get_rect(midtop=(107, 105))
    PurpleBaddie2rect = PurpleBaddie1.get_rect(midtop=(169, 105))
    PurpleBaddie3rect = PurpleBaddie1.get_rect(midtop=(231, 105))
    PurpleBaddie4rect = PurpleBaddie1.get_rect(midtop=(293, 105))
    PurpleBaddie5rect = PurpleBaddie1.get_rect(midtop=(355, 105))
    PurpleBaddie6rect = PurpleBaddie1.get_rect(midtop=(417, 105))
    PurpleBaddie7rect = PurpleBaddie1.get_rect(midtop=(479, 105))
    PurpleBaddie8rect = PurpleBaddie1.get_rect(midtop=(541, 105))
    PurpleBaddie9rect = PurpleBaddie1.get_rect(midtop=(603, 105))
    PurpleBaddie10rect = PurpleBaddie1.get_rect(midtop=(665, 105))
    PurpleBaddie11rect = PurpleBaddie1.get_rect(midtop=(107, 155))
    PurpleBaddie12rect = PurpleBaddie1.get_rect(midtop=(169, 155))
    PurpleBaddie13rect = PurpleBaddie1.get_rect(midtop=(231, 155))
    PurpleBaddie14rect = PurpleBaddie1.get_rect(midtop=(293, 155))
    PurpleBaddie15rect = PurpleBaddie1.get_rect(midtop=(355, 155))
    PurpleBaddie16rect = PurpleBaddie1.get_rect(midtop=(417, 155))
    PurpleBaddie17rect = PurpleBaddie1.get_rect(midtop=(479, 155))
    PurpleBaddie18rect = PurpleBaddie1.get_rect(midtop=(541, 155))
    PurpleBaddie19rect = PurpleBaddie1.get_rect(midtop=(603, 155))
    PurpleBaddie20rect = PurpleBaddie1.get_rect(midtop=(665, 155))
    GreenBaddies = []
    startx = 107
    starty = 205
    gbycount = 0
    for i in range(20):
        GreenBaddies.append(GreenBaddie1.get_rect(midtop=(startx, starty)))
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
        RedBaddies.append(RedBaddie1.get_rect(midtop=(startx, starty)))
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
        screen.blit(leveltext, (10, 5))
        screen.blit(one, (110, 0))

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
                    alien.x += 20
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

        if killcount == 60:
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
    screen.blit(SISTARTTEXT, (400, 350))
    screen.blit(SISTARTTEXT2, (250, 400))

    for bullet in bullets:
        screen.blit(bullet_img, bullet)

    pygame.display.update()
    clock.tick(FPS)
