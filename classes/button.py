import pygame

class button():
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
