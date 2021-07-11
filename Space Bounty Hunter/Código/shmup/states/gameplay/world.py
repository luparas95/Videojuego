import pygame

from shmup.entities.rendergroup import RenderGroup
from shmup.entities.hero import Hero
from shmup.entities.projectile import Projectile, ProjectileType
from shmup.entities.explosion import Explosion
from shmup.entities.enemies.enemy import Enemy
from shmup.assets.sound_manager import SoundManager
from shmup.assets.parallax import Parallax
from shmup.states.gameplay.spawner import Spawner
from shmup.config import Config
from shmup.states.gameplay.events import game_over_event
from shmup.ui.label import UILabel
from shmup.assets.asset_manager import AssetManager, AssetType

class World:

    def __init__(self):
        self.__players = RenderGroup()
        self.__allied_bullets = RenderGroup()
        self.__enemy_bullets = RenderGroup()
        self.__explosions = RenderGroup()
        self.__enemies = RenderGroup()

    def init(self):
        self.__players.add(Hero(self))

        self.__parallax = Parallax()
        self.__parallax.add_background(Config.space_bg_name, 0, Config.space_bg_speed)
        self.__parallax.add_background(Config.stars_name, 1, Config.stars_speed)

        self.__score = 0
        self.__font = AssetManager.instance().get(AssetType.Font, Config.sansation_font_name)

        self.__spawner = Spawner(self)
        SoundManager.instance().play_music(Config.mission_theme_name)

    def handle_input(self, key, is_pressed):
        for game_object in self.__players:
            game_object.handle_input(key, is_pressed)

    def update(self, delta_time):
        self.__players.update(delta_time)
        self.__enemies.update(delta_time)
        self.__allied_bullets.update(delta_time)
        self.__enemy_bullets.update(delta_time)
        self.__explosions.update(delta_time)
        self.__parallax.update(delta_time)
        self.__spawner.update(delta_time)
        self.__label = UILabel((50, Config.screen_size[1] - 10), self.__font, "SCORE: " + str(self.__score), (255, 255, 255))

        for player in pygame.sprite.groupcollide(self.__players, self.__enemy_bullets, True, True).keys():
            self.spawn_explosion(player.position.xy, True)
            self.game_over()

        for enemy in pygame.sprite.groupcollide(self.__enemies, self.__allied_bullets, True, True).keys():
            self.spawn_explosion(enemy.body.status.position.xy, False)
            self.__score += 1

        for player in pygame.sprite.groupcollide(self.__players, self.__enemies, True, True).keys():
            self.spawn_explosion(player.position.xy, True)
            self.game_over()

    def render(self, surface):
        self.__parallax.render(surface)
        self.__players.draw(surface)
        self.__enemies.draw(surface)
        self.__allied_bullets.draw(surface)
        self.__enemy_bullets.draw(surface)
        self.__explosions.draw(surface)
        self.__spawner.render(surface)
        self.__label.render(surface)

    def quit(self):
        self.__players.empty()
        self.__enemies.empty()
        self.__allied_bullets.empty()
        self.__enemy_bullets.empty()
        self.__explosions.empty()
        self.__parallax = None
        self.__spawner = None

    def spawn_bullet(self, projectile_type, position, velocity):
        if projectile_type == ProjectileType.AlliedBullet:
            self.__allied_bullets.add(Projectile(projectile_type, position, velocity))
            SoundManager.instance().play_sound(Config.allied_gunfire_name)
        if projectile_type == ProjectileType.EnemyBullet:
            self.__enemy_bullets.add(Projectile(projectile_type, position, velocity))
            SoundManager.instance().play_sound(Config.enemy_gunfire_name)

    def spawn_explosion(self, position, is_hero):
        self.__explosions.add(Explosion(position))
        if is_hero:
            name = Config.explosion1_name
        else:
            name = Config.explosion2_name

        SoundManager.instance().play_sound(name)

    def spawn_enemy(self, enemy_type, spawn_point, end_point, waypoints):
        self.__enemies.add(Enemy(self, enemy_type, spawn_point, end_point, waypoints))

    def game_over(self):
        pygame.time.set_timer(game_over_event, Config.game_over_time, True)
        SoundManager.instance().stop_music(Config.game_over_time)

    def get_hero_pos(self):
        if len(self.__players) > 0:
            return self.__players.sprites()[0].get_pos()
        else:
            return pygame.math.Vector2(0.0, 0.0)
    
    def get_score(self):
        return self.__score