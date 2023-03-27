from enum import Enum
from collections import namedtuple

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

# UI
TEXT_COLOR = (0, 0, 0)
FRUIT_COLOR = (200,0,0)
SNAKE_COLOR_BODY = (49, 220, 29)
SNAKE_COLOR_SHADOW = (34, 149, 21)
FOND_COLOR = (255, 255, 255)

# Game
SPEED = 1
BLOCK_SIZE = 20
SHADOW_SIZE = 4  
# 1 <= SHADOW_SIZE < BLOCK_SIZE

# Agent
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

# Model