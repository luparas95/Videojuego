from shmup.assets.fonts.bitmap_font import BitmapFont
import pygame
import sys
from enum import Enum

from shmup.states.state import State
from shmup.assets.asset_manager import AssetManager, AssetType
from shmup.ui.label import UILabel
from shmup.ui.label_clickable import UILabelClickable
from shmup.config import Config
from shmup.assets.parallax import Parallax
from shmup.assets.sound_manager import SoundManager
from shmup.states.gameplay.world import World

class Actions(Enum):
    Restart = 0
    Menu = 1

class GameOver(State):

    def __init__(self):
        super().__init__()
        self.next_state = "GamePlay"

        self.__parallax = Parallax()
        self.__parallax.add_background(Config.space_name, 0, 0)
        self.__parallax.add_background(Config.stars_menu_name, 1, Config.stars_menu_speed)
        self.__parallax.add_background(Config.world_name, 2, 0)

        self.__sansation_font = AssetManager.instance().get(AssetType.Font, Config.sansation_font_name)
        spacemission_font = AssetManager.instance().get(AssetType.Font, Config.spacemission_font_name)
        retro_font = AssetManager.instance().get(AssetType.Font, Config.retro_font_name)

        self.__center_position = [x/2 for x in Config.screen_size]
        self.__label = UILabel((self.__center_position[0], 130), retro_font, "GAME OVER", (200, 60, 60))
        self.__start_button = UILabelClickable(self.__center_position, spacemission_font, "RESTART", (140, 140, 190), (200, 200, 250), action = Actions.Restart)
        self.__exit_button = UILabelClickable((self.__center_position[0], 350), spacemission_font, "MENU", (140, 140, 190), (200, 200, 250), action = Actions.Menu)


    def enter(self):
        self.done = False
        self.__parallax.add_background(Config.spaceship_fall_name, 3, Config.spaceship_fall_speed)
        self.__score_label = UILabel((self.__center_position[0], 170), self.__sansation_font, "SCORE: " + str(self.score), (255, 255, 255))
        
        SoundManager.instance().play_music(Config.gameover_theme_name)

    def exit(self):
        pass

    def handle_input(self, event):
        if self.__start_button.handle_input(event) == Actions.Restart or (event.type == pygame.KEYDOWN and (event.key == pygame.K_r or event.key == pygame.K_RETURN)):
            self.__parallax.del_background(3)
            self.done = True
        if self.__exit_button.handle_input(event) == Actions.Menu or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
            self.__parallax.del_background(3)
            self.next_state = "Intro"
            self.done = True

    def update(self, delta_time):
        self.__parallax.update(delta_time)

    def render(self, surface):
        self.__parallax.render(surface)
        self.__label.render(surface)
        self.__score_label.render(surface)
        self.__start_button.render(surface)
        self.__exit_button.render(surface)
