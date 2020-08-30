import pygame, noise, colorsys
from pypresence import Presence
from time import time, perf_counter
from random import choice

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.DOUBLEBUF)
pygame.display.set_caption("2D MINE (Project World Generator)")
pygame.display.set_icon(pygame.image.load("icon.png"))

try:
    rpc = Presence(738768366801518622)
    rpc.connect()
except:
    pass

def exit():
    try:
        rpc.clear()
        rpc.close()
    except:
        pass
    quit()

def mainMenu():
    try:
        rpc.update(large_image="large", details="In main menu", start=time())
    except:
        pass
    # region definitions
    pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONUP])
    in_menu = True
    in_settings = False
    in_settings_before = False
    buttons_active = [False, False, False]
    buttons_active_settings = [False, False]
    settings_states = [False]
    # endregion
    menu_bg = pygame.image.load("MainMenu.png")
    screen.blit(menu_bg, [0, 0])
    pygame.display.flip()
    while in_menu:
        # region events_handling
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos_previous = [0, 0]
        if mouse_pos != mouse_pos_previous:
            if not in_settings:
                if 430 < mouse_pos[0] < 850:
                    if 250 < mouse_pos[1] < 300:
                        buttons_active = [True, False, False]
                    elif 320 < mouse_pos[1] < 370:
                        buttons_active = [False, True, False]
                    elif 390 < mouse_pos[1] < 440:
                        buttons_active = [False, False, True]
                    else:
                        buttons_active = [False, False, False]
                else:
                    buttons_active = [False, False, False]
            else:
                if 410 < mouse_pos[0] < 850 and 250 < mouse_pos[1] < 300:
                    buttons_active_settings = [True, False]
                elif 340 < mouse_pos[0] < 530 and 600 < mouse_pos[1] < 650:
                    buttons_active_settings = [False, True]
                else:
                    buttons_active_settings = [False, False]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if not in_settings:
                    if buttons_active[0]:
                        in_menu = False
                    elif buttons_active[1]:
                        in_settings = True;
                        buttons_active = [False, False, False]
                    elif buttons_active[2]:
                        exit()
                else:
                    if buttons_active_settings[0]:
                        settings_states[0] = not settings_states[0]
                        if settings_states[0]:
                            pygame.display.set_mode((1280, 720), pygame.FULLSCREEN | pygame.DOUBLEBUF)
                            menu_bg = pygame.image.load("Settings.png")
                            screen.blit(menu_bg, [0, 0])
                            pygame.display.flip()
                        else:
                            pygame.display.set_mode((1280, 720), pygame.DOUBLEBUF)
                            menu_bg = pygame.image.load("Settings.png")
                            screen.blit(menu_bg, [0, 0])
                            pygame.display.flip()
                    elif buttons_active_settings[1]:
                        in_settings = False
                        in_settings_before = True
                        buttons_active_settings = [False, False]
        # endregion
        # region draw_menu
        font = pygame.font.Font("Consolas.ttf", 42)
        if not in_settings:
            if in_settings_before:
                menu_bg = pygame.image.load("MainMenu.png")
                screen.blit(menu_bg, [0, 0])
                pygame.display.flip()
                in_settings_before = False
            if buttons_active[0]:
                b1 = pygame.draw.rect(screen, (85, 85, 85), (410, 250, 420, 50))
            else:
                b1 = pygame.draw.rect(screen, (128, 128, 128), (410, 250, 420, 50))
            if buttons_active[1]:
                b2 = pygame.draw.rect(screen, (85, 85, 85), (410, 320, 420, 50))
            else:
                b2 = pygame.draw.rect(screen, (128, 128, 128), (410, 320, 420, 50))
            if buttons_active[2]:
                b3 = pygame.draw.rect(screen, (85, 85, 85), (410, 390, 420, 50))
            else:
                b3 = pygame.draw.rect(screen, (128, 128, 128), (410, 390, 420, 50))

            text_play = font.render("Play", 1, (0, 0, 0))
            text_settings = font.render("Settings", 1, (0, 0, 0))
            text_exit = font.render("Exit", 1, (0, 0, 0))
            screen.blit(text_play, [590, 255])
            screen.blit(text_settings, [550, 325])
            screen.blit(text_exit, [590, 395])
            if mouse_pos != mouse_pos_previous or in_settings_before:
                pygame.display.update(b1)
                pygame.display.update(b2)
                pygame.display.update(b3)
        else:
            menu_bg = pygame.image.load("Settings.png")
            screen.blit(menu_bg, [0, 0])
            if settings_states[0]:
                if buttons_active_settings[0]:
                    b1 = pygame.draw.rect(screen, (0, 128, 0), (410, 250, 420, 50))
                else:
                    b1 = pygame.draw.rect(screen, (0, 200, 0), (410, 250, 420, 50))
            else:
                if buttons_active_settings[0]:
                    b1 = pygame.draw.rect(screen, (128, 0, 0), (410, 250, 420, 50))
                else:
                    b1 = pygame.draw.rect(screen, (200, 0, 0), (410, 250, 420, 50))

            if buttons_active_settings[1]:
                b2 = pygame.draw.rect(screen, (85, 85, 85), (340, 600, 190, 50))
            else:
                b2 = pygame.draw.rect(screen, (128, 128, 128), (340, 600, 190, 50))

            text_fullscreen = font.render("Fullscreen", 1, (0, 0, 0))
            text_back = font.render("Back", 1, (0, 0, 0))
            screen.blit(text_fullscreen, [505, 255])
            screen.blit(text_back, [390, 605])
            if not in_settings_before:
                pygame.display.flip()
                in_settings_before = True
            else:
                if mouse_pos != mouse_pos_previous:
                    pygame.display.update(b1)
                    pygame.display.update(b2)
        # endregion
        mouse_pos_previous = mouse_pos

class materials:
    air = 0
    grass_block = 1
    dirt = 2
    stone = 3
    coal = 4
    iron = 5
    gold = 6
    diamond = 7
    trunk = 8
    leaves = 9
    grass = 10
    rose = 11
    berry_bush = 12

def generateWorld():
    try:
        rpc.update(large_image="large", details="Generating world", start=time())
    except:
        pass
    bg = pygame.image.load("generating.png")
    screen.blit(bg, [0, 0])
    pygame.display.flip()

    global world
    world = [[materials.air for row in range(600)] for col in range(5000)]
    maxG = 500
    minG = 100
    maxGS = 5+3
    offsetG = choice(range(850000))
    offsetS = choice(range(850000))

    for i in range(len(world)):
        if i % 10 == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

        heightG = round((noise.pnoise1((i + offsetG) / 900, 5, 0.5, 2, 900000)+1)*(maxG-minG)/3) + minG
        heightS = heightG - 3 - round((noise.pnoise1((i + offsetS) / 600, 1, 0.5, 2, 900000) + 2) * maxGS / 1.5)

        # print(heightG, ' ', heightS)

        for j in range(heightS):
            # diamonds
            if world[i - 1][j] == materials.diamond or world[i][j - 1] == materials.diamond:
                if choice(range(1, 4)) == 3:
                    world[i][j] = materials.diamond
                else:
                    world[i][j] = materials.stone
            elif j <= 60 and choice(range(1, 650)) == 649:
                world[i][j] = materials.diamond

            # gold
            elif world[i - 1][j] == materials.gold or world[i][j - 1] == materials.gold:
                if choice(range(1, 4)) == 3:
                    world[i][j] = materials.gold
                else:
                    world[i][j] = materials.stone
            elif j <= 70 and choice(range(1, 600)) == 599:
                world[i][j] = materials.gold

            # iron
            elif world[i - 1][j] == materials.iron or world[i][j - 1] == materials.iron:
                if choice(range(1, 6)) >= 4:
                    world[i][j] = materials.iron
                else:
                    world[i][j] = materials.stone
            elif j <= 85 and choice(range(1, 500)) == 499:
                world[i][j] = materials.iron

            # coal
            elif world[i - 1][j] == materials.coal or world[i][j - 1] == materials.coal:
                if choice(range(1, 6)) > 3:
                    world[i][j] = materials.coal
                else:
                    world[i][j] = materials.stone
            elif choice(range(1, 450)) == 449:
                world[i][j] = materials.coal
            else:
                world[i][j] = materials.stone

        for j in range(heightS, heightG):
            world[i][j] = materials.dirt
        world[i][heightG] = materials.grass_block
        if choice(range(1, 60)) == 59 and world[i - 1][heightG] == materials.grass_block and world[i - 1][heightG + 2] != materials.trunk and i > 2 and i < 4997:
            increment = 1
            treetemp = choice(range(4, 7))
            while increment <= treetemp:
                if increment == treetemp:
                    world[i][heightG + increment - 1] = materials.leaves
                    world[i][heightG + increment] = materials.leaves
                    world[i][heightG + increment + 1] = materials.leaves
                    world[i][heightG + increment + 2] = materials.leaves
                    world[i - 1][heightG + increment + 1] = materials.leaves
                    world[i + 1][heightG + increment + 1] = materials.leaves
                    world[i - 1][heightG + increment] = materials.leaves
                    world[i - 2][heightG + increment] = materials.leaves
                    world[i + 1][heightG + increment] = materials.leaves
                    world[i + 2][heightG + increment] = materials.leaves
                    world[i - 1][heightG + increment - 1] = materials.leaves
                    world[i - 2][heightG + increment - 1] = materials.leaves
                    world[i + 1][heightG + increment - 1] = materials.leaves
                    world[i + 2][heightG + increment - 1] = materials.leaves
                else:
                    world[i][heightG + increment] = materials.trunk
                increment += 1
        elif world[i - 1][heightG + 1] == materials.grass and choice(range(1, 3)) == 2:
            world[i][heightG + 1] = materials.grass
        elif choice(range(1, 25)) == 24:
            world[i][heightG + 1] = materials.grass
        elif world[i-1][heightG + 1] == materials.rose and choice(range(1, 4)) == 3:
            world[i][heightG + 1] = materials.grass
        elif choice(range(1, 15)) == 14 and world[i - 1][heightG + 1] == materials.grass:
            world[i][heightG + 1] = materials.rose
        elif choice(range(1, 120)) == 119:
            world[i][heightG + 1] = materials.rose
        elif world[i - 1][heightG + 1] == materials.rose and world[i - 2][heightG + 1] == materials.air:
            world[i][heightG + 1] = materials.grass
        if world[i - 1][heightG + 1] == materials.trunk and choice(range(1, 10)) == 9:
            world[i][heightG + 1] = materials.berry_bush
        if world[i - 1][heightG + 1] == materials.trunk and choice(range(1, 10)) == 9 and world[i - 1][heightG] == materials.grass_block:
            world[i - 2][heightG + 1] = materials.berry_bush

    # print(world)

def pausemenu():
    try:
        rpc.update(large_image="large", details="In pause menu...", start=time())
    except:
        pass
    ssrect = pygame.Rect(0, 0, 1280, 720)
    ss = pygame.Surface((1280, 720))
    ss.blit(screen, ssrect)
    inPauseMenu = True
    while inPauseMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                inPauseMenu = False
        
        screen.fill((0, 0, 0))
        screen.blit(ss, [0, 0])
        darkglass = pygame.Surface((1280, 720))
        darkglass.set_alpha(200)
        darkglass.fill((0, 0, 0))
        screen.blit(darkglass, [0, 0])
        pygame.display.flip()
        clock.tick(30)


font = pygame.font.Font("Consolas.ttf", 30)
def updateFPSmeter():
    global FPStext
    global timeClockMins
    hours = int(timeClockMins / 60)
    mins = int(timeClockMins % 60)
    hoursstring = str(hours)
    if len(hoursstring) == 1:
        hoursstring = "0" + hoursstring
    minsstring = str(mins)
    if len(minsstring) == 1:
        minsstring = "0" + minsstring
    
    timestring = hoursstring + ":" + minsstring
    
    FPStext = font.render(timestring + "; " + str(int(clock.get_fps()))+"FPS", 1, (255, 0, 165))

skyV = 100
skyMode = 0
timeClockMins = 12 * 60
def skyColor(tempV):
    global skyV
    global timeClockMins
    if skyMode == 1:
        skyV = tempV + 0.0025
    else:
        skyV = tempV - 0.0025

    timeClockMins += 0.018
    
    if skyV < 0:
        tempV = 0
    if skyV > 100:
        tempV = 100

    if int(timeClockMins / 60) == 24:
        timeClockMins = 0

    if tempV == 0:
        print("MIDNIGHT", int(timeClockMins / 60), ":", int(timeClockMins % 60))
    elif tempV == 100:
        print("NOON", int(timeClockMins / 60), ":", int(timeClockMins % 60))

    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(202 / 360, 0.82, tempV / 100))

mainMenu()
generateWorld()

global clock
clock = pygame.time.Clock()

try:
    rpc.update(large_image="large", details="Playing a game", start=time())
except:
    pass

textures = {
    materials.grass_block: pygame.image.load("textures/grass_block.png").convert(),
    materials.dirt: pygame.image.load("textures/dirt.png").convert(),
    materials.stone: pygame.image.load("textures/stone.png").convert(),
    materials.diamond: pygame.image.load("textures/diamond.png").convert(),
    materials.gold: pygame.image.load("textures/gold.png").convert(),
    materials.coal: pygame.image.load("textures/coal.png").convert(),
    materials.iron: pygame.image.load("textures/iron.png").convert(),
    materials.trunk: pygame.image.load("textures/trunk.png").convert(),
    materials.leaves: pygame.image.load("textures/leaves.png").convert(),
    materials.grass: pygame.image.load("textures/grass.png"),
    materials.rose: pygame.image.load("textures/rose.png"),
    materials.berry_bush: pygame.image.load("textures/berry_bush.png")
}
pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONUP, pygame.KEYDOWN, pygame.KEYUP])

texH = 48
texW = 48
wx = choice(range(2000, 3000))
temph = 599
skyColorTuple = skyColor(skyV)
while world[wx + int((1280 / texW) / 2)][temph] != materials.grass_block:
    temph -= 1
    
wy = 600 - temph - int(texH / 720) - 12
clock = pygame.time.Clock()
time_move = perf_counter()
time_events = perf_counter()
updateFPSmeter()
while True:
    if skyV <= 0 and skyMode == 0:
        skyMode = 1
    elif skyV >= 100 and skyMode == 1:
        skyMode = 0
    
    if perf_counter() - time_events >= 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pausemenu()
        skyColorTuple = skyColor(skyV)

    if perf_counter() - time_move >= 0.05:
        time_move = perf_counter()
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            if wy > 0:
                wy -= 1

        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            if wy < 599 - int(720 / texH):
                wy += 1

        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            if wx > 0:
                wx -= 1

        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            if wx < 4999 - int(1280 / texW):
                wx += 1
        updateFPSmeter()
    

    screen.fill(skyColorTuple)

    for y in range(int(720 / texH) + 1):
        for x in range(int(1280 / texW)+1):
            if world[wx+x][599-wy-y] != materials.air:
                screen.blit(textures[world[wx+x][599-wy-y]], [x*texW, y*texH])
    
    screen.blit(FPStext, [0, 0])
    pygame.display.flip()
    clock.tick()
