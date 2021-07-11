import pygame
import random

from shmup.config import Config
from shmup.entities.projectile import ProjectileType

class Mind:

    def __init__(self, world, body):
        self.__world = world
        self.__body = body
        self.__fire_rate = Config.enemies_data[self.__body.enemy_name]['fire_rate']

    def update(self, delta_time):
        if random.random() <= self.__fire_rate:
            projectile_velocity = (0, random.uniform(Config.enemies_projectile_speed_range[0], Config.enemies_projectile_speed_range[1]))
            self.__world.spawn_bullet(ProjectileType.EnemyBullet, self.__body.status.position, pygame.math.Vector2(projectile_velocity))