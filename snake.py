import pygame
import sys
from pygame.math import Vector2
class Snake:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        self.move_direction = Vector2(1, 0)
        self.snake_body = [Vector2(7,10), Vector2(6, 10), Vector2(5, 10)]
    
    def update(self):
        body_copy = self.snake_body[:-1]
        if self.move_direction.x == 1 and self.snake_body[0].x >= self.settings.number_widths - 1:
            body_copy.insert(0, Vector2(0, self.snake_body[0].y))        
        elif self.move_direction.x == -1 and self.snake_body[0].x <= 0:
            body_copy.insert(0, Vector2(self.settings.number_widths - 1, self.snake_body[0].y)) 
        elif self.move_direction.y == 1 and self.snake_body[0].y >= self.settings.number_rows - 1:
            body_copy.insert(0, Vector2(self.snake_body[0].x, 0)) 
        elif self.move_direction.y == -1 and self.snake_body[0].y <= 0:
            body_copy.insert(0, Vector2(self.snake_body[0].x, self.settings.number_rows - 1)) 
        else:
             body_copy.insert(0, self.snake_body[0] + self.move_direction)
        self.snake_body = body_copy

    def insert_tail(self):
        body_copy = self.snake_body[:]
        body_copy.insert(0, self.snake_body[0] + self.move_direction)
        self.snake_body = body_copy

    def draw_snake(self):
        # for body in self.snake_body:
        #     rect = pygame.Rect(body.x * self.settings.cell_size, body.y * self.settings.cell_size, self.settings.cell_size , self.settings.cell_size)
        #     pygame.draw.rect(self.screen, (0, 0, 255), rect)
        for key in range(len(self.snake_body)):
            body = self.snake_body[key]
            rect = pygame.Rect(body.x * self.settings.cell_size, body.y * self.settings.cell_size, self.settings.cell_size , self.settings.cell_size)
            if key != len(self.snake_body) - 1: rem = self.snake_body[key+1] - self.snake_body[key]
            else: rem = self.snake_body[key] - self.snake_body[key - 1]
            if key == 0:
                if rem == Vector2(0, 1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/head_up.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif rem == Vector2(0, -1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/head_down.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif rem == Vector2(1, 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/head_left.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif rem == Vector2(-1, 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/head_right.png').convert_alpha()
                    self.screen.blit(image, rect)
            elif key == len(self.snake_body) - 1:
                if rem == Vector2(0, 1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/tail_down.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif rem == Vector2(0, -1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/tail_up.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif rem == Vector2(1, 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/tail_right.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif rem == Vector2(-1, 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/tail_left.png').convert_alpha()
                    self.screen.blit(image, rect)
            else:
                pre_rem = self.snake_body[key] - self.snake_body[key - 1]
                suf_rem = self.snake_body[key + 1] - self.snake_body[key]
                if pre_rem == Vector2(-1, 0) and suf_rem == Vector2(0, self.settings.number_rows - 1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_topright.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(1, 0) and suf_rem == Vector2(0, self.settings.number_rows - 1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_topleft.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(-1, 0) and suf_rem == Vector2(0, -(self.settings.number_rows - 1)):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_bottomright.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(1, 0) and suf_rem == Vector2(0, -(self.settings.number_rows - 1)):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_bottomleft.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, 1) and suf_rem == Vector2(self.settings.number_widths - 1, 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_topleft.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, -1) and suf_rem == Vector2(self.settings.number_widths - 1, 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_bottomleft.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, 1) and suf_rem == Vector2(-self.settings.number_widths - 1, 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_topright.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, -1) and suf_rem == Vector2(-self.settings.number_widths - 1, 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_bottomright.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, -(self.settings.number_rows - 1)) and suf_rem == Vector2(-1, 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_topleft.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, -(self.settings.number_rows - 1)) and suf_rem == Vector2(1, 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_topright.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, self.settings.number_rows - 1) and suf_rem == Vector2(-1, 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_bottomleft.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, self.settings.number_rows - 1) and suf_rem == Vector2(1, 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_bottomright.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, -1) and suf_rem == Vector2(-(self.settings.number_widths - 1), 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_bottomright.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, 1) and suf_rem == Vector2(-(self.settings.number_widths - 1), 0):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_topright.png').convert_alpha()
                    self.screen.blit(image, rect)


                elif pre_rem == Vector2(self.settings.number_widths - 1, 0) and suf_rem == Vector2(0, 1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_bottomright.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(self.settings.number_widths - 1, 0) and suf_rem == Vector2(0, -1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_topright.png').convert_alpha()
                    self.screen.blit(image, rect)

                elif pre_rem == Vector2(-(self.settings.number_widths - 1), 0) and suf_rem == Vector2(0, 1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_bottomleft.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(-(self.settings.number_widths - 1), 0) and suf_rem == Vector2(0, -1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_topleft.png').convert_alpha()
                    self.screen.blit(image, rect)

                elif pre_rem == Vector2(0, 1) and suf_rem == Vector2(1, 0) or pre_rem == Vector2(-1, 0) and suf_rem == Vector2(0, -1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_topright.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, -1) and suf_rem == Vector2(1, 0) or pre_rem == Vector2(-1, 0) and suf_rem == Vector2(0, 1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_bottomright.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, 1) and suf_rem == Vector2(-1, 0) or pre_rem == Vector2(1, 0) and suf_rem == Vector2(0, -1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_topleft.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif pre_rem == Vector2(0, -1) and suf_rem == Vector2(-1, 0) or pre_rem == Vector2(1, 0) and suf_rem == Vector2(0, 1):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_bottomleft.png').convert_alpha()
                    self.screen.blit(image, rect)
                elif (suf_rem == Vector2(1, 0) or suf_rem == Vector2(-1, 0)) or (pre_rem == Vector2(1, 0) or pre_rem == Vector2(-1, 0)):
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_horizontal.png').convert_alpha()
                    self.screen.blit(image, rect)
                else: 
                    image = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/body_vertical.png').convert_alpha()
                    self.screen.blit(image, rect)

