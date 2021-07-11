from shmup.assets.background import Background

class Parallax:

    def __init__(self):
        self.__bgs = []

    def add_background(self, image_name, layer, speed):
        self.__bgs.append((layer, Background(image_name, layer, speed)))
        self.__bgs.sort()

    def del_background(self, layer):
        self.__bgs.pop(layer)

    def update(self, delta_time):
        for _, bg in self.__bgs:
            bg.update(delta_time)

    def render(self, surface):
        for _, bg in self.__bgs:
            bg.render(surface)