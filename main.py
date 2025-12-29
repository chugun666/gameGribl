from constants import *
from settings import *
from classes.button import *

import pygame

pygame.init()

pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("писюны")
clock = pygame.time.Clock()
icon_surface = pygame.image.load(icon)
pygame.display.set_icon(icon_surface)
running = True
menu = True
level = False
pause = False
settings = False

font = pygame.font.Font(None, 36)

menu_surface = pygame.Surface((WIDTH, HEIGHT))

back_menu = pygame.image.load(KpssM)


start_button = button(pb,"Начало", SEAGREEN)
settings_button = button(sb,"Настройки", SEAGREEN)
quit_button = button(qb,"Кончало", SEAGREEN)

while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if start_button.is_clicked(event):
            menu = False
            level = True
        if settings_button.is_clicked(event):
            print("а нету")
        if quit_button.is_clicked(event):
            running = False

    screen.fill(BLACK)

    if menu:
        screen.blit(menu_surface, (0, 0))
        screen.blit(back_menu, (0, 0))
        # Отрисовка кнопок
        start_button.draw(screen)
        settings_button.draw(screen)
        quit_button.draw(screen)

        text_autor = font.render("made by chugun_666_", True, (255, 255, 255))
        screen.blit(text_autor, (20, 680))
    
    if level:
        pass
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()