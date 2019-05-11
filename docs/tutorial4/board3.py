"""Add color to the cells."""

import pygame
from pygame.locals import *
from pygamelib import *
import numpy as np

class BoardDemo(Game):
    """Draw cells in random colors."""
    def __init__(self):
        super(BoardDemo, self).__init__()
        Text('Color', size=48)
        Text('Add random colors', size=24)

        n, m = 10, 16
        b = Board(n, m, pos=(200, 10))
        b.color_list = [None, RED, GREEN, BLUE, YELLOW]
        b.colors = np.random.randint(0, 5, (n, m))
        b.T = b.colors

if __name__ == '__main__':
    BoardDemo().run()