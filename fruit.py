import pygame
from random import randint
from pygame.math import Vector2
class Fruit:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.fruit_x = randint(0, ai_game.settings.number_widths - 1)
        self.fruit_y = randint(0, ai_game.settings.number_rows - 1)
        while True:
            for body in ai_game.snake.snake_body[1:]:
                if body == Vector2(self.fruit_y, self.fruit_x):
                    self.fruit_x = randint(0, ai_game.settings.number_widths - 1)
                    self.fruit_y = randint(0, ai_game.settings.number_rows - 1)
                    continue
            break
        self.fruit_pos = Vector2(self.fruit_x, self.fruit_y )
        self.rect = pygame.Rect(self.fruit_pos.x * ai_game.settings.cell_size, self.fruit_pos.y * ai_game.settings.cell_size, ai_game.settings.cell_size , ai_game.settings.cell_size)
        self.image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/apple.png').convert_alpha()
        # self.image = pygame.transform.scale(self.image, (ai_game.settings.cell_size, ai_game.settings.cell_size))
    def draw_fruit(self):
        # pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
        self.screen.blit(self.image, self.rect)