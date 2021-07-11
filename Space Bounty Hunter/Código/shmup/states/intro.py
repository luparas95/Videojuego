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

class Actions(Enum):
    Next_Level = 0
    Exit = 1

class Intro(State):

    def __init__(self):
        super().__init__()
        self.next_state = "GamePlay"

        self.__parallax = Parallax()
        self.__parallax.add_background(Config.space_name, 0, 0)
        self.__parallax.add_background(Config.stars_menu_name, 1, Config.stars_menu_speed)
        self.__parallax.add_background(Config.world_name, 2, 0)

        sansation_font = AssetManager.instance().get(AssetType.Font, Config.sansation_font_name)
        spacemission_font = AssetManager.instance().get(AssetType.Font, Config.spacemission_font_name)

        center_position = [x/2 for x in Config.screen_size]
        self.__title = BitmapFont(Config.game_title, (center_position[0],90))
        self.__label = UILabel((center_position[0], 130), sansation_font, "INTERESTELLAR ADVENTURE", (200, 60, 60))
        self.__start_button = UILabelClickable(center_position, spacemission_font, "START", (140, 140, 190), (200, 200, 250), action = Actions.Next_Level)
        self.__exit_button = UILabelClickable((center_position[0], 350), spacemission_font, "EXIT", (140, 140, 190), (200, 200, 250), action = Actions.Exit)

    def enter(self):
        self.done = False
        
        SoundManager.instance().play_music(Config.intro_theme_name)

    def exit(self):
        pass

    def handle_input(self, event):
        if self.__start_button.handle_input(event) == Actions.Next_Level or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
            self.done = True
        if self.__exit_button.handle_input(event) == Actions.Exit:
            pygame.quit()
            sys.exit()

    def update(self, delta_time):
        self.__parallax.update(delta_time)

    def render(self, surface):
        self.__parallax.render(surface)
        self.__title.render(surface)
        self.__label.render(surface)
        self.__start_button.render(surface)
        self.__exit_button.render(surface)
