import pygame

from shmup.entities.gameobject import GameObject
from shmup.assets.asset_manager import AssetManager, AssetType
from shmup.config import Config

class Explosion(GameObject):

    def __init__(self, position):
        super().__init__()
        self.__current_sequence = 0
        _, clip = AssetManager.instance().get(AssetType.FlipBook, Config.explosion_name, sequence = 0)

        self.position = pygame.math.Vector2(position[0], position[1])
        self.render_rect = clip.copy()
        self._center()
        self.__current_time = 0.0
        self.__total_sequences = Config.explosion_size[0] * Config.explosion_size[1]

    def update(self, delta_time):
        if self.__current_time + delta_time > Config.explosion_time_per_sequence:
            self.__current_time = 0
            self.__current_sequence += 1
            if self.__current_sequence >= self.__total_sequences:
                self.kill()
        else:
            self.__current_time += delta_time

    def render(self, surface):
        image, clip = AssetManager.instance().get(AssetType.FlipBook, Config.explosion_name, sequence = self.__current_sequence)
        surface.blit(image, self.render_rect, clip)
