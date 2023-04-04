from enum import Enum
from collections import namedtuple
import snake
import time
import os

TIME_KEY = time.strftime("%Y-%m-%d;%H-%M-%S")

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    
Point = namedtuple('Point', 'x, y')

# UI
FOND_COLOR = (230, 230, 230)
TEXT_COLOR = (0, 0, 0)
FRUIT_COLOR = (200,0,0)
SNAKE_COLOR_BODY = (49, 220, 29)
SNAKE_COLOR_SHADOW = (34, 149, 21)
SNAKE_COLOR_EYES = (0, 50, 255)

# Game
BLOCK_SIZE = 20
SHADOW_SIZE = 4
SPEED = 1000

# Agent
POSITIVE_REWARD = 10
NEGATIVE_REWARD = -10

# Model
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
VITESSE_APPRENTISSAGE = 0.001
EPSILON_NB_GAMES = 80
GAMMA_DISCOUNT_RATE = 0.9
HIDDEN_SIZE = 256

# Tests des meilleurs hyperparamètres
if __name__ == "__main__":
    if not os.path.exists("entrainement"):
        os.makedirs("entrainement")

    with open(f"entrainement/{TIME_KEY}.txt", "w") as f:
        f.write(TIME_KEY)
                            
    gamma_values = [0.8, 0.9, 0.95]
    learning_rate_values = [0.001, 0.01]
    epsilon_nb_games_values = [80, 100]
    hidden_size_values = [256, 512]

    for epsilon_nb_games in epsilon_nb_games_values:
        for gamma in gamma_values:
                for learning_rate in learning_rate_values:
                    for hidden_size in hidden_size_values:

                        with open(f"entrainement/{TIME_KEY}.txt", "a") as f:
                            f.write(f"gamma={gamma}, learning_rate={learning_rate}, epsilon_nb_games={epsilon_nb_games}, hidden_size={hidden_size}")
                        
                        GAMMA_DISCOUNT_RATE = gamma
                        VITESSE_APPRENTISSAGE = learning_rate
                        EPSILON_NB_GAMES = epsilon_nb_games
                        HIDDEN_SIZE = hidden_size
                        
                        start_time = time.time()
                        
                        print(f"Running experiment with parameters: gamma={gamma}, learning_rate={learning_rate}, epsilon_nb_games={epsilon_nb_games}, hidden_size={hidden_size}")
                        snake.trainAgent()
                        total_time = time.time() - start_time
                        print(f"Experiment took {total_time} seconds")
                        with open(f"entrainement/{TIME_KEY}.txt", "a") as f:
                            f.write(f"total_time={total_time}")