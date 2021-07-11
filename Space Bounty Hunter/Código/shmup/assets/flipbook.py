import pygame
from os import path

class FlipBook:

    def __init__(self, image_filename, rows, cols):
        image_filename_path = path.join(*image_filename)

        if path.isfile(image_filename_path):
            self.__image = pygame.image.load(image_filename_path).convert_alpha()
            rect_width = self.__image.get_size()[0] / cols
            rect_height = self.__image.get_size()[1] / rows
            rect = pygame.Rect(0, 0, rect_width, rect_height)
            self.__sequences = []
            for row in range(rows):
                rect.y = row * rect_height
                for col in range(cols):
                    rect.x = col * rect_width
                    self.__sequences.append(rect.copy())
        else:
            self.__image = pygame.Surface((0,0))
            self.__sequences = []

    def get_image(self, sequence = 0):
        if sequence <= len(self.__sequences):
            return self.__image, self.__sequences[sequence]
        return self.__image, pygame.Rect(0,0,0,0)
