import pygame
from constants import *
from settings import *

class Button():
    def __init__(self,poss, text, color, font_size=30, action=None):
        self.rect = pygame.Rect(poss)
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, font_size) # Используем стандартный шрифт
        self.action = action # Функция, которая будет вызываться при нажатии

    def draw(self, screen):
        # Меняем цвет при наведении
        mouse_pos = pygame.mouse.get_pos()
        current_color = (self.color[0]+30, self.color[1]+30, self.color[2]+30) if self.rect.collidepoint(mouse_pos) else self.color
        
        # Рисуем прямоугольник кнопки
        pygame.draw.rect(screen, current_color, self.rect, border_radius=10)
        
        # Отрисовка текста по центру
        text_surf = self.font.render(self.text, True, (255,255,255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 50])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.change_x = 0
        self.change_y = 0
        self.level = None

    def update(self):
        self.calc_grav()
        
        # Движение по горизонтали
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        # Движение по вертикали
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.change_y = 0
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
                self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35

    def jump(self):
        # Проверка, стоит ли игрок на чем-то
        self.rect.y += 8
        hit = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 8
        if len(hit) > 0:
            self.change_y = -10

    def go_left(self): self.change_x = -7
    def go_right(self): self.change_x = 7
    def stop(self): self.change_x = 0

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(100, 100, 100)):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Level:
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.player = player
        self.world_shift = 0  # На сколько сдвинут мир

    def shift_world(self, shift_x):
        self.world_shift += shift_x
        for platform in self.platform_list:
            platform.rect.x += shift_x

    def update(self):
        self.platform_list.update()

    def draw(self, screen):
        screen.fill((200, 200, 255))
        # Рисуем платформы с учетом их текущего rect.x (который меняется в shift_world)
        self.platform_list.draw(screen)

class Level_01(Level):
    def __init__(self, player):
        super().__init__(player)
        
        # Список платформ: [x, y, ширина, высота]
        level_layout = [
            [0, 550, 800, 50],
            [200, 450, 150, 20],
            [450, 350, 150, 20],
            [100, 250, 150, 20]
        ]

        for plat in level_layout:
            block = Block(plat[0], plat[1], plat[2], plat[3])
            self.platform_list.add(block)
