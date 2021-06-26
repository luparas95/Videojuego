import pygame
import math

import os

from shmup.config import Config

class Walker:
    def __init__(self, window_size):
        self.__image = pygame.image.load(os.path.join(*Config.walker_filename)).convert_alpha()    

        self.__is_moving = False
        self.__look_right = True

        self.__stop_count = 0
        self.__move_count = 1

        self.__position = pygame.math.Vector2(0, window_size[1] - Config.walker_size[1])        

    def update(self, delta, window_size):
        move = pygame.math.Vector2(0.0, 0.0)
        
        if self.__is_moving:
            if self.__look_right:
                if self.__position.x < window_size[0] - Config.walker_size[0]:
                    move.x += Config.walker_speed
                    self.__move_count += Config.walker_speed * 0.5

                    if self.__move_count >= 10:
                        self.__move_count = 1
                else:
                    self.__is_moving = False
                    self.__look_right = False
            else:
                if self.__position.x > 0:
                    move.x -= Config.walker_speed
                    self.__move_count += Config.walker_speed * 0.5

                    if self.__move_count >= 10:
                        self.__move_count = 1
                else:
                    self.__is_moving = False
                    self.__look_right = True
        else:
            self.__stop_count += Config.walker_speed * 5

            if self.__stop_count > Config.fps:
                self.__stop_count = 0
                self.__is_moving = True
                self.__move_count = 1

        self.__position += move * delta

    def render(self, dest):
        surface_row = 1
        surface_col = 0

        decimal, entero = math.modf(self.__move_count)

        if self.__is_moving:
            surface_col = entero

        if self.__look_right:
            surface_row = 0            

        dest.blit(self.__image, self.__position.xy, (Config.walker_size[0] * surface_col, 
            Config.walker_size[1] * surface_row, Config.walker_size[0], Config.walker_size[1]))

    def release(self):
        pass