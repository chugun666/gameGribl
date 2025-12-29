import pygame
from constants import *
from settings import *
from classes import *

class Level1(Level):
    def __init__(self, surface):
        level_data = [
            '                            ',
            '                            ',
            '       XXXXX                ',
            '  P              XXXX       ',
            'XXXXXX         XXXXXXX      ',
            'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        ]
        super().__init__(surface)