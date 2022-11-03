import pygame
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *


def init():

    WIDTH = 1920
    HEIGHT = 1080

    window = Window(WIDTH, HEIGHT)

    window.set_title("ShipInsane")

    window.set_background_color([0, 0, 0])

    #Carrega os sprites de cada objeto do jogo
    island = Sprite("../assets/island2.png", 1)
    sea = Sprite("../assets/mar.png", 1)
    enemy_pirate_1 = Sprite("../assets/enemy1.png", 1)
    enemy_pirate_2 = Sprite("../assets/enemy2.png", 1)
    player = Sprite("../assets/player.png", 1)
    enemy_ship_1 = Sprite("../assets/enemy_ship1.png")
    enemy_ship_2 = Sprite("../assets/enemy_ship2.png")
    cannon1 = Sprite("../assets/cannon1.png")
    cannon2 = Sprite("../assets/cannon2.png")
    cannon3 = Sprite("../assets/cannon3.png")
    cannon4 = Sprite("../assets/cannon4.png")

    keyboard = Window.get_keyboard()

    #Configura as posiçoes dos elementos do jogo

    island.x = WIDTH / 2 - island.width / 2
    island.y = HEIGHT / 2 - island.height / 2

    enemy_ship_1.x = 5 * WIDTH / 6
    enemy_ship_1.y = island.x / 2 - 40

    enemy_ship_2.x = island.x / 2 - 40
    enemy_ship_2.y = 5 * HEIGHT / 7 

    enemy_pirate_1.x = island.x + island.width / 2 
    enemy_pirate_1.y = island.y + 50

    enemy_pirate_2.x = island.x + island.width / 2 - 70
    enemy_pirate_2.y = island.y + 80

    player.x = island.x + island.width / 2 + 120
    player.y = island.y + island.height / 2 - 60

    cannon1.x = island.x + island.width / 2 - 25
    cannon1.y = island.y + 20

    cannon2.x = island.x + island.width / 2 + 130
    cannon2.y = island.y + island.height / 2 - 70

    cannon3.x = island.x + island.width / 2 - 50
    cannon3.y = island.y + island.height - 50  

    cannon4.x = island.x
    cannon4.y = island.y + island.height / 2

    img0 = cannon1.image
    rect0 = cannon1.image.get_rect()
    rect0.center=(cannon1.x + cannon1.width, cannon2.y - cannon1.height)

    def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

    angle=0
    while(True):
        
        sea.draw()
        island.draw()
        enemy_pirate_1.draw()
        enemy_pirate_2.draw()
        enemy_ship_1.draw()
        enemy_ship_2.draw()
        cannon2.draw()
        cannon3.draw()
        cannon4.draw()
        player.draw()

        if keyboard.key_pressed("A"):
            angle += 1
        if keyboard.key_pressed("D"):
            angle -= 1
        img1=pygame.transform.rotate(img0, angle)
        rect1=img1.get_rect()
        rect1.center=rect0.center

        window.get_screen().blit(img1, rect1)

        # if keyboard.key_pressed("A") and test == 1:
        #     test = 0
        #     cannon1.image, cannon1.rect = rot_center(cannon1.image, cannon_1_rect, 15)      
        # if keyboard.key_pressed("D") and test == 0:
        #     test = 1
        #     cannon1.image, cannon1.rect = rot_center(cannon1.image, cannon_1_rect, -15)
        


        # window.get_screen().blit(cannon1.image, cannon1.rect)

        # if keyboard.key_pressed("A") and test == 1:
        #     test = 0
        #     cannon1.image = pygame.transform.rotate(cannon1.image, 15)        
        # if keyboard.key_pressed("D") and test == 0:
        #     test = 1
        #     cannon1.image = pygame.transform.rotate(cannon1.image, -15)

        # cannon1.draw()
        window.update()
        window.set_background_color([0, 0, 0,])
