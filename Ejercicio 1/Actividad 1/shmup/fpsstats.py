#!/usr/bin/env python3

import pygame

from shmup.config import Config

class FPSStats:

    def __init__(self, font):
        self.__font = font
        self.__render_fps = 0
        self.__logic_fps = 0
        self.__update_time = 0
        self.__update_fps()

    def update_render(self):
        self.__render_fps += 1

    def update_logic(self, delta):
        self.__logic_fps +=1
        self.__update_time += delta

        if self.__update_time >= Config.refresh_time:
            self.__update_fps()

            self.__update_time -= Config.refresh_time
            self.__render_fps = 0
            self.__logic_fps = 0

    def __update_fps(self):
        self.__fps = self.__font.render(f"Logic {self.__logic_fps} fps  Render {self.__render_fps} fps", True, Config.fps_foreground_color, Config.fps_background_color)

    def render_stats(self, screen):
        screen.blit(self.__fps, (0,0))