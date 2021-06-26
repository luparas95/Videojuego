import pygame
import math

import os

from shmup.config import Config

class Label:
    def __init__(self, window_size, font):
        self.__font = font
        self.__image = pygame.image.load(os.path.join(*Config.scroll_font_filename)).convert_alpha()    

        self.__letters = {
            " ": self.__image.subsurface((0  * Config.letter_size[0], 0 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "!": self.__image.subsurface((1  * Config.letter_size[0], 0 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "´": self.__image.subsurface((7  * Config.letter_size[0], 0 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "(": self.__image.subsurface((8  * Config.letter_size[0], 0 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            ")": self.__image.subsurface((9  * Config.letter_size[0], 0 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            ",": self.__image.subsurface((12 * Config.letter_size[0], 0 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "-": self.__image.subsurface((13 * Config.letter_size[0], 0 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            ".": self.__image.subsurface((14 * Config.letter_size[0], 0 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "0": self.__image.subsurface((16 * Config.letter_size[0], 0 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "1": self.__image.subsurface((17 * Config.letter_size[0], 0 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "2": self.__image.subsurface((18 * Config.letter_size[0], 0 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "3": self.__image.subsurface((19 * Config.letter_size[0], 0 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "4": self.__image.subsurface((0  * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "5": self.__image.subsurface((1  * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "6": self.__image.subsurface((2  * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "7": self.__image.subsurface((3  * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "8": self.__image.subsurface((4  * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "9": self.__image.subsurface((5  * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            ":": self.__image.subsurface((6  * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "?": self.__image.subsurface((11 * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "a": self.__image.subsurface((13 * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "b": self.__image.subsurface((14 * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "c": self.__image.subsurface((15 * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "d": self.__image.subsurface((16 * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "e": self.__image.subsurface((17 * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "f": self.__image.subsurface((18 * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "g": self.__image.subsurface((19 * Config.letter_size[0], 1 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "h": self.__image.subsurface((0  * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "i": self.__image.subsurface((1  * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "j": self.__image.subsurface((2  * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "k": self.__image.subsurface((3  * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "l": self.__image.subsurface((4  * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "m": self.__image.subsurface((5  * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "n": self.__image.subsurface((6  * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "o": self.__image.subsurface((7  * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "p": self.__image.subsurface((8  * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "q": self.__image.subsurface((9  * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "r": self.__image.subsurface((10 * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "s": self.__image.subsurface((11 * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "t": self.__image.subsurface((12 * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "u": self.__image.subsurface((13 * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "v": self.__image.subsurface((14 * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "w": self.__image.subsurface((15 * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "x": self.__image.subsurface((16 * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "y": self.__image.subsurface((17 * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
            "z": self.__image.subsurface((18 * Config.letter_size[0], 2 * Config.letter_size[1]), (Config.letter_size[0], Config.letter_size[1])),
        }

        self.__letter_count = 1
        self.__letter_marker = 0

        self.__position = pygame.math.Vector2(window_size[0], window_size[1]/2 - Config.letter_size[1]/2)        

    def update(self, delta, window_size):
        move = pygame.math.Vector2(0.0, 0.0)

        move.x -= Config.label_speed

        self.__position += move * delta

        if self.__position.x < window_size[0] - Config.letter_size[0]:
            self.__position.x = window_size[0]

            if self.__letter_count <= window_size[0] / Config.letter_size[0]:
                self.__letter_count += 1

            self.__letter_marker += 1
            if self.__letter_marker >= len(Config.label_message):
                self.__letter_marker = 0

    def render(self, screen):
        for i in range(self.__letter_count):
            screen.blit(self.__letters[Config.label_message[self.__letter_marker - i].lower()], 
                (self.__position.x - Config.letter_size[0] * i, self.__position.y))

        n_letters = self.__font.render(f"Letras instanciadas: {self.__letter_count}", True, 
            Config.fps_foreground_color, Config.fps_background_color)
            
        screen.blit(n_letters, (Config.screen_size[0] - 250,0))

    def release(self):
        pass