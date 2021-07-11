import pygame

from shmup.config import Config
from shmup.assets.asset_manager import AssetType, AssetManager

class Background:
    def __init__(self, image_name, layer, speed):
        self.image_name = image_name
        self.layer = layer
        self.speed = speed

        _, clip = AssetManager.instance().get(AssetType.Image, self.image_name)
        self.__height = clip.height
        self.__y_1 = self.__init_y() + self.__height
        self.__y_2 = self.__init_y()

    def update(self, delta_time):
        self.__y_1 = self.__update_y(self.__y_1, delta_time, self.__y_2)
        self.__y_2 = self.__update_y(self.__y_2, delta_time, self.__y_1)

    def render(self, surface):
        image, clip = AssetManager.instance().get(AssetType.Image, self.image_name)
        self.__render_bg(self.__y_1, clip.copy(), image, surface)
        self.__render_bg(self.__y_2, clip.copy(), image, surface)

    def __update_y(self, y, delta_time, other_y):
        y += self.speed * delta_time
        if y > Config.screen_size[1] - 10:
            y = self.__init_y()
        return y

    def __init_y(self):
        return Config.screen_size[1] - self.__height - self.__height

    def __render_bg(self, y, clip, image, dest):
        is_rendered, render_rect, clip_rect = self.__calc_rects(y, clip)
        if is_rendered:
            dest.blit(image, render_rect, clip_rect)

    def __calc_rects(self, y, clip_rect):
        render_rect = pygame.Rect(0, 0, clip_rect.width, 0)
        if y + self.__height >= 0:
            if y > 0:
                render_rect.y = y
                render_rect.height = clip_rect.height = Config.screen_size[1] - y
                clip_rect.y = 0
            else:
                render_rect.y = 0
                render_rect.height = clip_rect.height = self.__height - y
                clip_rect.y = -y
            return True, render_rect, clip_rect

        return False, pygame.Rect(0,0,0,0), pygame.Rect(0,0,0,0)