import pygame
import math

import os

from shmup.config import Config

class BitmapFont:
    def __init__(self, text, position):
        self.text = text
        self.x = position[0]
        self.y = position[1]

        if len(self.text) % 2 == 0:
            self.x -= (Config.bitmap_font_size * len(self.text) / 2)
        else:
            self.x -= (Config.bitmap_font_size * len(self.text) / 2) - Config.bitmap_font_size / 2

        self.__font = pygame.image.load(os.path.join(*Config.bitmap_font_image_filename)).convert_alpha()   

        self.__letters = {
            " ": self.__font.subsurface((0  * Config.bitmap_font_size, 0 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "!": self.__font.subsurface((1  * Config.bitmap_font_size, 0 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "´": self.__font.subsurface((7  * Config.bitmap_font_size, 0 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "(": self.__font.subsurface((8  * Config.bitmap_font_size, 0 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            ")": self.__font.subsurface((9  * Config.bitmap_font_size, 0 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            ",": self.__font.subsurface((12 * Config.bitmap_font_size, 0 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "-": self.__font.subsurface((13 * Config.bitmap_font_size, 0 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            ".": self.__font.subsurface((14 * Config.bitmap_font_size, 0 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "0": self.__font.subsurface((16 * Config.bitmap_font_size, 0 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "1": self.__font.subsurface((17 * Config.bitmap_font_size, 0 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "2": self.__font.subsurface((18 * Config.bitmap_font_size, 0 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "3": self.__font.subsurface((19 * Config.bitmap_font_size, 0 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "4": self.__font.subsurface((0  * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "5": self.__font.subsurface((1  * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "6": self.__font.subsurface((2  * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "7": self.__font.subsurface((3  * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "8": self.__font.subsurface((4  * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "9": self.__font.subsurface((5  * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            ":": self.__font.subsurface((6  * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "?": self.__font.subsurface((11 * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "a": self.__font.subsurface((13 * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "b": self.__font.subsurface((14 * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "c": self.__font.subsurface((15 * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "d": self.__font.subsurface((16 * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "e": self.__font.subsurface((17 * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "f": self.__font.subsurface((18 * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "g": self.__font.subsurface((19 * Config.bitmap_font_size, 1 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "h": self.__font.subsurface((0  * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "i": self.__font.subsurface((1  * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "j": self.__font.subsurface((2  * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "k": self.__font.subsurface((3  * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "l": self.__font.subsurface((4  * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "m": self.__font.subsurface((5  * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "n": self.__font.subsurface((6  * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "o": self.__font.subsurface((7  * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "p": self.__font.subsurface((8  * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "q": self.__font.subsurface((9  * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "r": self.__font.subsurface((10 * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "s": self.__font.subsurface((11 * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "t": self.__font.subsurface((12 * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "u": self.__font.subsurface((13 * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "v": self.__font.subsurface((14 * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "w": self.__font.subsurface((15 * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "x": self.__font.subsurface((16 * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "y": self.__font.subsurface((17 * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
            "z": self.__font.subsurface((18 * Config.bitmap_font_size, 2 * Config.bitmap_font_size), (Config.bitmap_font_size, Config.bitmap_font_size)),
        }

    def update(self):
        pass

    def render(self, surface):
        for i in range(len(self.text)):
            surface.blit(self.__letters[self.text[i].lower()], (self.x + Config.bitmap_font_size * i, self.y))