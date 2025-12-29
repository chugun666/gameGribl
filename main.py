from constants import *
from settings import *
from classes import *
from LEVELS.level1 import *


import pygame

pygame.init()

pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("писюны")
clock = pygame.time.Clock()
icon_surface = pygame.image.load(icon)
pygame.display.set_icon(icon_surface)
running = True
menu_r = True
level_r = False
pause_r = False
settings_r = False


level1_r = True

font = pygame.font.Font(None, 36)

menu_surface = pygame.Surface((WIDTH, HEIGHT))

back_menu = pygame.image.load(KpssM)


player = Player(50, 500)
level = Level_01(player)
player.level = level
active_sprites = pygame.sprite.Group()
active_sprites.add(player)
camera = Camera(50, 500)

start_button = Button(pb,"Начало", SEAGREEN)
settings_button = Button(sb,"Настройки", SEAGREEN)
quit_button = Button(qb,"Кончало", SEAGREEN)

while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if menu_r:
            if start_button.is_clicked(event):
                menu_r = False
                level_r = True
            if settings_button.is_clicked(event):
                print("а нету")
            if quit_button.is_clicked(event):
                running = False
        if level_r:
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT: player.go_left()
                    if event.key == pygame.K_RIGHT: player.go_right()
                    if event.key == pygame.K_UP: player.jump()
            if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT): player.stop()

    screen.fill(BLACK)

    if level_r:
        if level1_r:
            camera.update(player)
            for block in level.platform_list:
                screen.blit(block.image, camera.apply(block))
            active_sprites.update()
            level.draw(screen)
            active_sprites.draw(screen)
    elif menu_r:
        screen.blit(menu_surface, (0, 0))
        screen.blit(back_menu, (0, 0))
        # Отрисовка кнопок
        start_button.draw(screen)
        settings_button.draw(screen)
        quit_button.draw(screen)

        text_autor = font.render("made by chugun_666_", True, (255, 255, 255))
        screen.blit(text_autor, (20, 680))
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()