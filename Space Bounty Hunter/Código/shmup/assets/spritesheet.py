import pygame
from os import path
import json

class SpriteSheet:

    def __init__(self, image_filename, data_filename):
        image_filename_path = path.join(*image_filename)
        data_filename_path = path.join(*data_filename)

        if path.isfile(image_filename_path) and path.isfile(data_filename_path):
            with open(data_filename_path) as f:
                self.__dict = json.load(f)

            self.__image = pygame.image.load(image_filename_path).convert_alpha()
        else:
            self.__dict = {}
            self.__image = pygame.Surface((0,0))

    def get_image(self, image_name):
        if image_name in self.__dict:
            return self.__image, pygame.Rect(self.__dict[image_name])


    def get_clip(self, image_name):
        if image_name in self.__dict:
            return pygame.Rect(self.__dict[image_name])
        return pygame.Rect(0,0,0,0)
