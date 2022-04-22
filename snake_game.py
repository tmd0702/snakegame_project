import pygame
import sys
from settings import Setting
from pygame.math import Vector2
from fruit import Fruit
from snake import Snake
from pygame.locals import *
class SnakeGame:
    def __init__(self):
        pygame.init()
        self.settings = Setting()
       
        # self.screen = pygame.display.set_mode((self.bg_size, self.bg_size))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.number_rows = self.screen.get_rect().height // self.settings.cell_size
        self.settings.number_widths = self.screen.get_rect().width // self.settings.cell_size

        self.snake = Snake(self)
        self.fruit = Fruit(self)
        self.clock = pygame.time.Clock()
        self.crunch_sound = pygame.mixer.Sound('C:/Users/mduc0/Documents/CODE/python_work/Snake/sound/glasscrunch.wav')
    
    def _update_snake(self):
        self._check_collision()
        self.snake.update()
        self._check_eat_fruit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self._draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self._draw_score()
        pygame.display.flip()
    
    def _reset_game(self):
        self.snake = Snake(self)

    def _keydown_action(self, event):
        if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.snake.move_direction.x != -1:
            self.snake.move_direction = Vector2(1, 0)
        elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.snake.move_direction.x != 1:
            self.snake.move_direction = Vector2(-1, 0)
        elif (event.key == pygame.K_UP or event.key == pygame.K_w) and self.snake.move_direction.y != 1:
            self.snake.move_direction = Vector2(0, -1)
        elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.snake.move_direction.y != -1:
            self.snake.move_direction = Vector2(0, 1)
        elif event.key == pygame.K_SPACE:
            if not self.settings.pause_game:
                self.settings.pause_game = True
            else:
                self.settings.pause_game = False
        elif event.key == 27:
            pygame.quit()
            sys.exit()

    def _check_eat_fruit(self): 
        if self.snake.snake_body[0] == self.fruit.fruit_pos:
            self.crunch_sound.play()
            self.snake.insert_tail()
            self.fruit = Fruit(self)

    def _check_collision(self):
        for pos in self.snake.snake_body[1:]:
            if pos == self.snake.snake_body[0]:
                self._reset_game()

    def _draw_grass(self):
        for row in range(self.settings.number_rows):
            if row % 2 == 0:
                pos_x = row * self.settings.cell_size
                for col in range(self.settings.number_widths):
                    if col % 2 == 0:
                        pos_y = col * self.settings.cell_size
                        grass_rect = pygame.Rect(pos_y, pos_x, self.settings.cell_size , self.settings.cell_size)
                        pygame.draw.rect(self.screen, self.settings.grass_color, grass_rect)
            else:
                pos_x = row * self.settings.cell_size
                for col in range(self.settings.number_widths):
                    if col % 2 != 0:
                        pos_y = col * self.settings.cell_size
                        grass_rect = pygame.Rect(pos_y, pos_x, self.settings.cell_size , self.settings.cell_size)
                        pygame.draw.rect(self.screen, self.settings.grass_color, grass_rect)

    def _draw_score(self):
        score = str(len(self.snake.snake_body) - 3)
        game_font = pygame.font.Font('C:/Users/mduc0/Documents/CODE/python_work/Snake/font/PoetsenOne-Regular.ttf', 25)
        score_surface = game_font.render(score, True, (56, 74, 12))
        score_x = 60
        score_y = 100
        score_rect = score_surface.get_rect(center = (score_y, score_x))
        apple = pygame.image.load('C:/Users/mduc0/Documents/CODE/python_work/Snake/image/apple.png').convert_alpha()
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        
        self.screen.blit(score_surface, score_rect)
        self.screen.blit(apple, apple_rect)



    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_action(event)

    def run_game(self):
        while True:
            self._check_event()
            if not self.settings.pause_game:
                self._update_snake()
                self._update_screen()        
            self.clock.tick(10)

if __name__ == '__main__':
    ai = SnakeGame()
    ai.run_game()