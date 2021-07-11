import pygame
from os import path
from enum import Enum

from shmup.assets.spritesheet import SpriteSheet
from shmup.assets.flipbook import FlipBook

class AssetType(Enum):
    Image = 0,
    SpriteSheet = 1,
    FlipBook = 2,
    Font = 3,
    Sound = 4,
    Music = 5

class AssetManager:

    _instance = None

    @staticmethod
    def instance():
        if AssetManager._instance is None:
            AssetManager()
        return AssetManager._instance

    def __init__(self):
        if AssetManager._instance is None:
            AssetManager._instance = self

            self.__assets = {}
        else:
            raise "Asset Manager doesn't Allow Multiple Instances"

    def load(self, asset_type, asset_name, asset_filename, data_filename = None, font_size = 0, rows = 0, cols = 0):
        asset_filename_path = path.join(*asset_filename)
        if data_filename is not None:
            data_filename_path = path.join(*data_filename)

        if asset_name not in self.__assets and path.isfile(asset_filename_path):
            if asset_type == AssetType.Image:
                self.__assets[asset_name] = pygame.image.load(asset_filename_path).convert_alpha()
            elif asset_type == AssetType.SpriteSheet:
                self.__assets[asset_name] = SpriteSheet(asset_filename, data_filename)
            elif asset_type == AssetType.FlipBook:
                self.__assets[asset_name] = FlipBook(asset_filename, rows, cols)
            elif asset_type == AssetType.Font:
                self.__assets[asset_name] = pygame.font.Font(asset_filename_path, font_size)
            elif asset_type == AssetType.Sound:
                self.__assets[asset_name] = pygame.mixer.Sound(asset_filename_path)
            elif asset_type == AssetType.Music:
                self.__assets[asset_name] = asset_filename_path
        return

    def set(self, asset_name, asset):
        if asset_name not in self.__assets:
            self.__assets[asset_name] = asset

    def get(self, asset_type, asset_name, sheet_name = None, sequence = 0):
        if asset_type == AssetType.SpriteSheet:
            if sheet_name in self.__assets:
                return self.__assets[sheet_name].get_image(asset_name)
            return None, pygame.Rect(0,0,0,0)
        elif asset_type == AssetType.FlipBook:
            if asset_name in self.__assets:
                return self.__assets[asset_name].get_image(sequence)
        elif asset_type == AssetType.Image:
            if asset_name in self.__assets:
                return self.__assets[asset_name], self.__assets[asset_name].get_rect()
            return None, pygame.Rect(0,0,0,0)
        else:
            if asset_name in self.__assets:
                return self.__assets[asset_name]
            return None

    def clean(self):
        self.__assets = {}
