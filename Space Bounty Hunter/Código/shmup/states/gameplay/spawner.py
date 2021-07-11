import pygame
import random

from shmup.config import Config
from shmup.entities.enemies.enemy import EnemyType

class Spawner:

    def __init__(self, world):
        self.__world = world
        self.__spawn_points = Config.enemies_spawn_points
        self.__end_points = Config.enemies_end_points
        self.__waypoints = []

        rows = int(Config.waypoints_area[1] / Config.waypoints_separation[1])
        cols =  int(Config.waypoints_area[0] / Config.waypoints_separation[0])
        for row in range(rows):
            row_cols = cols + 1 if row % 2 == 0 else cols
            x = 0 if row % 2 == 0 else Config.waypoints_separation[0]/2
            for col in range(row_cols):
                self.__waypoints.append((x + (col * Config.waypoints_separation[0]), row * Config.waypoints_separation[1]))
        self.flag = True

    def update(self, delta_time):
        if random.random() <= Config.enemies_spawn_probability:
            enemy_type = EnemyType.Avenger if random.randint(0,1) == 0 else EnemyType.Raptor
            spawn_point = self.__spawn_points[random.randint(0, len(self.__spawn_points)-1)]
            end_point = self.__end_points[random.randint(0, len(self.__end_points)-1)]
            n_waypoints = random.randint(1, Config.enemies_max_waypoints)
            waypoints = []
            for i in range(n_waypoints):
                waypoint = self.__waypoints[random.randint(0, len(self.__waypoints)-1)]
                waypoints.append(waypoint)
            self.__world.spawn_enemy(enemy_type, spawn_point, end_point, waypoints)

    def render(self, surface):
        if Config.debug:
            for point in self.__waypoints:
                pygame.draw.circle(surface, Config.debug_way_point_color, point , 2)