from constants import *
from settings import *
from classes import *


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

fontn = pygame.font.Font(None, 80)

menu_surface = pygame.Surface((WIDTH, HEIGHT))

back_menu = pygame.image.load(KpssM)


player = Player(50, 600)
level = Level_01(player)
player.level = level
active_sprites = pygame.sprite.Group()
active_sprites.add(player)

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
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a): player.go_left()
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d): player.go_right()
                    if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE: player.jump()
            if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_d, pygame.K_a): player.stop()

    screen.fill(BLACK)

    if level_r:
        print(player.rect.x)
        if level1_r:
            active_sprites.update()

            # ЛОГИКА КАМЕРЫ:
            # Если игрок подходит к правой границе (на 1/4 экрана)
            if player.rect.right >= 800:
                diff = player.rect.right - 800
                player.rect.right = 800
                level.shift_world_x(-diff)

            # Если игрок подходит к левой границе
            if player.rect.left <= 400:
                diff = 400 - player.rect.left
                player.rect.left = 400
                level.shift_world_x(diff)

            if player.rect.y <= 200:
                 diff = 200 - player.rect.y
                 player.rect.y = 200
                 level.shift_world_y(diff)

            if player.rect.y >= 600:
                 diff = player.rect.y - 600
                 player.rect.y = 600
                 level.shift_world_y(-diff)


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
        text_namegame = fontn.render("ПИСЮНЫ", True, (255, 255, 255))
        screen.blit(text_namegame, (510, 150))
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()