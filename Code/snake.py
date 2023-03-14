import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()
font = pygame.font.SysFont('arial', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

TEXT_COLOR = (255, 255, 255)
FRUIT_COLOR = (200,0,0)
SNAKE_COLOR_1 = (34, 149, 21)
SNAKE_COLOR_2 = (49, 220, 29)
FOND_COLOR = (0,0,0)

SHADOW_SIZE = 4  # 1 <= SHADOW_SIZE < BLOCK_SIZE
BLOCK_SIZE = 20
SPEED = 5

class SnakeGame:
    
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake pas AI pour l'instant")
        self.clock = pygame.time.Clock()
        
        # init game state
        self.direction = Direction.RIGHT
        
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        
        self.score = 0
        self.food = None
        self._place_food()
        
    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE 
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()
        
    def play_step(self):
        # 1. On récupère les entrées de l'utilisateur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
        
        # 2. On met à jour l'état du snake
        self._move(self.direction)        # update la tête
        self.snake.insert(0, self.head)
        
        # 3. On vérifie si le jeu est fini
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score
            
        # 4. On met une nouvelle bouffe si il l'a mangé
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
        
        # 5. On met à jour l'affichage
        self._update_ui(record)
        self.clock.tick(SPEED)

        # 6. On retourne l'état du jeu
        return game_over, self.score
    
    def _is_collision(self):
        # si on touche un mur
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True
        # si on touche la queue
        if self.head in self.snake[1:]:
            return True
        
        return False
        
    def _update_ui(self, record):
        DEMI_BLOCK_SIZE = int(BLOCK_SIZE/2)
        
        self.display.fill(FOND_COLOR)

        for pt in self.snake:
            pygame.draw.rect(self.display, SNAKE_COLOR_1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, SNAKE_COLOR_2, pygame.Rect(pt.x+(SHADOW_SIZE/2), pt.y+(SHADOW_SIZE/2), BLOCK_SIZE - SHADOW_SIZE, BLOCK_SIZE - SHADOW_SIZE))

        pygame.draw.circle(self.display, FRUIT_COLOR, [self.food.x + DEMI_BLOCK_SIZE, self.food.y + DEMI_BLOCK_SIZE], DEMI_BLOCK_SIZE)

        textScore = font.render(f"Score : {str(self.score)}", True, TEXT_COLOR)
        self.display.blit(textScore, [0, 0])

        textRecord = font.render(f"Record : {str(record)}", True, TEXT_COLOR)
        textRecord_rect = textRecord.get_rect()
        textRecord_pos = (self.display.get_width() - textRecord_rect.width, 0)
        self.display.blit(textRecord, textRecord_pos)

        pygame.display.flip()
        
    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
            
        self.head = Point(x, y)
            

if __name__ == '__main__':

    record = 0

    while True:
        game = SnakeGame()
        
        while True:
            game_over, score = game.play_step()
            
            if game_over == True:
                break
            
        if score > record:
            record = score

        print('Final Score', score)
        print('Record', record)
        
    pygame.quit()