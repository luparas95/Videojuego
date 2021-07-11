import pygame
from enum import Enum
import math
import random

from shmup.assets.asset_manager import AssetType, AssetManager
from shmup.entities.enemies.steering_data import KinematicStatus
from shmup.entities.enemies.seek import Seek
from shmup.config import Config

class State(Enum):
    PathFollow = 0,
    ToEnd = 1,
    Kamikaze = 2

class Body:

    def __init__(self, world, enemy, enemy_name, spawn_point, end_point, waypoints):
        self.__world = world
        self.__enemy = enemy

        self.__end_point = pygame.math.Vector2(end_point)
        self.__waypoints = waypoints.copy()

        self.status = KinematicStatus(pygame.math.Vector2(spawn_point))
        self.__behavior = Seek(Config.enemies_data[enemy_name]['acceleration'])
        self.__state = State.PathFollow

        self.__current_waypoint = 0
        self.__current_target = KinematicStatus(self.__waypoints[self.__current_waypoint])

        self.enemy_name = enemy_name
        self.__max_speed = Config.enemies_data[enemy_name]['speed']
        _, clip = AssetManager.instance().get(AssetType.Image, enemy_name)
        self.rect = clip.copy()
        self.render_rect = clip.copy()

    def update(self, delta_time):
        if self.arrived(self.__current_target.position, 20):
            if self.__state == State.PathFollow:
                self.__current_waypoint += 1
                if self.__current_waypoint >= len(self.__waypoints):
                    if random.random() < Config.enemies_kamikaze_probability:
                        self.__state = State.Kamikaze
                        self.__current_target.position = self.__world.get_hero_pos()
                    else:
                        self.__state = State.ToEnd
                        self.__current_target.position = self.__end_point
                else:
                    self.__current_target.position = self.__waypoints[self.__current_waypoint]
            elif self.__state == State.ToEnd:
                self.__enemy.release()
            elif self.__state == State.Kamikaze:
                self.__world.spawn_explosion(self.status.position, False)
                self.__enemy.release()

        steer = self.__behavior.calculate(self.status, self.__current_target)
        self.update_steer(steer, delta_time)
        if self.__behavior.needs_orientation:
            self.set_orientation()

    def render(self, surface):
        image, _ = AssetManager.instance().get(AssetType.Image, self.enemy_name)

        image = pygame.transform.rotate(image, -self.status.orientation-90)
        self.render_rect = image.get_rect(center = self.status.position.xy)
        self.rect = self.render_rect.copy()
        self.rect.inflate_ip(self.rect.width * -0.3, self.rect.height * -0.3)
        surface.blit(image, self.render_rect)

        if Config.debug:
            pygame.draw.rect(surface, Config.debug_collider_color, self.rect, 1)
            pygame.draw.rect(surface, Config.debug_render_color, self.render_rect, 1)

    def arrived(self, target, delta):
        dist = (target - self.status.position).length()
        if dist <= delta:
            return True

        return False

    def keep_in_speed(self):
        if self.status.velocity.length() > self.__max_speed:
            self.status.velocity = self.status.velocity.normalize() * self.__max_speed

    def update_steer(self, steer, delta_time):
        self.status.velocity += steer.linear
        self.status.position += self.status.velocity * delta_time
        self.status.rotation += steer.angular
        self.status.orientation += self.status.rotation * delta_time

        self.keep_in_speed()

    def set_orientation(self):
        if self.status.velocity.length_squared() > 0:
            self.status.orientation = math.degrees(math.atan2(self.status.velocity.y, self.status.velocity.x))
