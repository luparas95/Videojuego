#!/usr/bin/env python3

import pygame

from shmup.config import Config
from shmup.assets.asset_manager import AssetManager, AssetType

class FPSStats:

    def __init__(self):
        self.__update_time = 0
        self.__render_frames = 0
        self.__logic_frames = 0
        self.__set_fps_surface()

    def render_stats(self, surface):
        surface.blit(self.__fps, Config.fps_stats_pos)

    def update_render(self):
        self.__render_frames += 1

    def update_logic(self, delta):
        self.__update_time += delta
        self.__logic_frames += 1

        if self.__update_time >= Config.refresh_stats_time:
            self.__set_fps_surface()

            self.__update_time -= Config.refresh_stats_time
            self.__logic_frames = 0
            self.__render_frames = 0

    def __set_fps_surface(self):
        font = AssetManager.instance().get(AssetType.Font, Config.sansation_font_name)
        self.__fps = font.render(f"Logic {self.__logic_frames} fps - Render {self.__render_frames} fps", True, (255,255,255), (0,0,0))
