import pygame

from shmup.states.state import State
from shmup.states.gameplay.world import World
from shmup.states.gameplay.events import game_over_event
from shmup.assets.sound_manager import SoundManager
from shmup.assets.asset_manager import AssetManager, AssetType
from shmup.config import Config

class GamePlay(State):

    def __init__(self):
        super().__init__()
        self.next_state = "GameOver"
        self.__world = World()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            self.__world.handle_input(event.key, True)
        if event.type == pygame.KEYUP:
            self.__world.handle_input(event.key, False)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.__world.handle_input(None, True)
        if event.type == pygame.MOUSEBUTTONUP:
            self.__world.handle_input(None, False)
        if event.type == game_over_event:
            self.score = self.__world.get_score()
            self.done = True

    def update(self, delta_time):
        self.__world.update(delta_time)

    def render(self, surface):
        self.__world.render(surface)

    def enter(self):
        self.done = False
        self.__world.init()

    def exit(self):
        self.__world.quit()