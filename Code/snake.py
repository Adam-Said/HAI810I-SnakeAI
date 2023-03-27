import pygame
import random
from variables import *
import agent as agentIA

pygame.init()
font = pygame.font.SysFont('arial', 25)

class SnakeGame:
    
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake pas AI pour l'instant")
        self.clock = pygame.time.Clock()
        self.reset()


    def reset(self):
        # reset game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0
        

    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE 
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()
        

    def play_step(self, action):
        # 1. On récupère les entrées de l'utilisateur
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         quit()
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             self.direction = Direction.LEFT
        #         elif event.key == pygame.K_RIGHT:
        #             self.direction = Direction.RIGHT
        #         elif event.key == pygame.K_UP:
        #             self.direction = Direction.UP
        #         elif event.key == pygame.K_DOWN:
        #             self.direction = Direction.DOWN
        self.frame_iteration += 1
        # 1. On laisse jouer l'agent
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # 2. On met à jour l'état du snake
        self._move(action) # update de la tête
        self.snake.insert(0, self.head)
        
        # 3. On vérifie si le jeu est fini
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score
            
        # 4. On met une nouvelle bouffe si il l'a mangé
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()
        
        # 5. On met à jour l'affichage
        self._update_ui(record)
        self.clock.tick(SPEED)

        # 6. On retourne l'état du jeu
        return reward, game_over, self.score
    

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # si on touche un mur
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        # si on touche la queue
        print(pt, "*****", self.snake[1:])
        input()
        return pt in self.snake[1:]
        

    def _update_ui(self, record):
        DEMI_BLOCK_SIZE = int(BLOCK_SIZE/2)
        
        self.display.fill(FOND_COLOR)

        for pt in self.snake:
            pygame.draw.rect(self.display, SNAKE_COLOR_SHADOW, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, SNAKE_COLOR_BODY, pygame.Rect(pt.x+(SHADOW_SIZE/2), pt.y+(SHADOW_SIZE/2), BLOCK_SIZE - SHADOW_SIZE, BLOCK_SIZE - SHADOW_SIZE))

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

    try:
        record = int([record for record in open("record.txt", "r")][0])
    except:
        record = 0
    game = SnakeGame()
    agent = agentIA.Agent()
    while True:
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)
        reward, game_over, score = game.play_step(final_move)
        state_new = agent.get_state(game)
        
        if game_over:
            game.reset()
            agent.n_games += 1
        
            if score > record:
                record = score
                with open("record.txt", "w") as f:
                    f.write(str(record))

            print('Final Score', score)
            print('Record', record)