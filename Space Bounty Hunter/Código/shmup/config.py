#!/usr/bin/env python3

class Config:

    screen_size = (480, 640)
    game_title = "Space Bounty Hunter"
    background_color = (0, 0, 0)

    spaceship_name = "spaceship"
    spaceship_image_filename = ["shmup", "assets", "images", "spaceship.png"]
    spaceship_data_filename = ["shmup", "assets", "images", "spaceship.json"]
    enemies_name = "enemies"
    enemies_image_filename = ["shmup", "assets", "images", "enemies.png"]
    enemies_data_filename = ["shmup", "assets", "images", "enemies.json"]

    explosion_name = "explosion"
    explosion_image_filename = ["shmup", "assets", "images", "explosion.png"]
    explosion_size = (4,4)
    explosion_time_per_sequence = 40

    space_bg_name = "space_bg"
    space_bg_image_filename = ["shmup", "assets", "images", "space_bg.jpg"]
    space_bg_speed = 0.05
    stars_name = "stars"
    stars_image_filename = ["shmup", "assets", "images", "stars.png"]
    stars_speed = 0.08
    space_name = "space"
    space_image_filename = ["shmup", "assets", "images", "space.jpg"]
    stars_menu_name = "stars_menu"
    stars_menu_image_filename = ["shmup", "assets", "images", "stars_menu.png"]
    stars_menu_speed = 0.02
    world_name = "world"
    world_image_filename = ["shmup", "assets", "images", "world.png"]
    spaceship_fall_name = "spaceship_fall"
    spaceship_fall_image_filename = ["shmup", "assets", "images", "spaceship_fall.png"]
    spaceship_fall_speed = 0.01

    bitmap_font_name = "bitmap_font"
    bitmap_font_image_filename = ["shmup", "assets", "images", "bitmap_font.png"]
    bitmap_font_size = 16

    hero_entity_name = "hero"
    hero_left_entity_name = "hero_left"
    hero_right_entity_name = "hero_right"
    hero_down_entity_name = "hero_down"
    hero_up_entity_name = "hero_up"
    hero_left_up_entity_name = "hero_left_up"
    hero_right_up_entity_name = "hero_right_up"
    hero_left_down_entity_name = "hero_left_down"
    hero_right_down_entity_name = "hero_right_down"
    hero_bullet_entity_name = "hero_bullet"
    enemy_bullet_entity_name = "enemy_bullet"

    sansation_font_name = "sansation"
    sansation_font_filename = ["shmup", "assets", "fonts", "Sansation.ttf"]
    spacemission_font_name = "spacemission"
    spacemission_font_filename = ["shmup", "assets", "fonts", "SpaceMission.otf"]
    retro_font_name = "retro"
    retro_font_filename = ["shmup", "assets", "fonts", "Retro.ttf"]

    allied_gunfire_name = "allied_gunfire"
    allied_gunfire_filename = ["shmup", "assets", "sfx", "allied_gunfire.wav"]
    enemy_gunfire_name = "enemy_gunfire"
    enemy_gunfire_filename = ["shmup", "assets", "sfx", "enemy_gunfire.wav"]
    explosion1_name = "explosion1"
    explosion1_filename = ["shmup", "assets", "sfx", "explosion1.wav"]
    explosion2_name = "explosion2"
    explosion2_filename = ["shmup", "assets", "sfx", "explosion2.wav"]

    mission_theme_name = "mission"
    mission_theme_filename = ["shmup", "assets", "music", "mission.ogg"]
    intro_theme_name = "intro"
    intro_theme_filename = ["shmup", "assets", "music", "intro.ogg"]
    gameover_theme_name = "gameover"
    gameover_theme_filename = ["shmup", "assets", "music", "gameover.ogg"]

    hero_speed = 0.25
    hero_fire_cooldown = 300
    allied_bullet_velocity = (0.0, -0.3)

    fps = 60
    time_per_frame = 1000.0 / fps
    refresh_stats_time = 1000.0
    fps_stats_pos = (0, 2)

    debug = False
    debug_collider_color = (0, 255, 255)
    debug_render_color = (0, 0, 255)
    debug_way_point_color = (0,255,0)

    waypoints_area = (screen_size[0], screen_size[1] / 2)
    waypoints_separation = (120, 100)

    red_enemy_name = "red_enemy"
    blue_enemy_name = "blue_enemy"

    enemies_spawn_probability = 0.01
    enemies_max_waypoints = 5
    enemies_projectile_speed_range = (0.1, 0.4)
    enemies_kamikaze_probability = 0.3
    enemies_data = {
        "blue_enemy" : { "fire_rate" : 0.005, "speed" : 0.1, "acceleration" : 0.005},
        "red_enemy" : { "fire_rate" : 0.01, "speed" : 0.12, "acceleration" : 0.005} }

    enemies_spawn_points = [(-100, 0),
                            (100, -100),
                            (screen_size[0]/2, -100),
                            (screen_size[0] - 100 , -100),
                            (screen_size[0] + 100, 0)]

    enemies_end_points = [(-100, 0),
                            (100, -100),
                            (-100, screen_size[1]),
                            (100, screen_size[1] + 100),
                            (screen_size[0]/2, screen_size[1] + 100),
                            (screen_size[0] - 100 , screen_size[1] + 100),
                            (screen_size[0] + 100, screen_size[1])]

    game_over_time = 5000

    def __init__(self):
        pass
