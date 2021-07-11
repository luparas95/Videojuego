import pygame
from enum import Enum

from shmup.entities.gameobject import GameObject
from shmup.entities.enemies.body import Body
from shmup.entities.enemies.mind import Mind
from shmup.config import Config

class EnemyType(Enum):
    Raptor = 0,
    Avenger = 1

class Enemy(GameObject):

    def __init__(self, world, enemy_type, spawn_point, end_point, waypoints):
        super().__init__()

        if enemy_type == EnemyType.Avenger:
            self.__enemy_name = Config.red_enemy_name
        if enemy_type == EnemyType.Raptor:
            self.__enemy_name = Config.blue_enemy_name

        self.body = Body(world, self, self.__enemy_name, spawn_point, end_point, waypoints)
        self.mind = Mind(world, self.body)
        self.rect = self.body.rect

    def update(self, delta):
        self.mind.update(delta)
        self.body.update(delta)
        self.rect = self.body.rect

    def render(self, surface):
        self.body.render(surface)

    def release(self):
        self.kill()