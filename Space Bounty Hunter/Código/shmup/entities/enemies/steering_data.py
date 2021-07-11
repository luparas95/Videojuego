import pygame

class KinematicStatus:

    def __init__(self, position = pygame.math.Vector2(0.0, 0.0), orientation = 0.0 , velocity = pygame.math.Vector2(0.0, 0.0), rotation = 0.0,  speed = 0.0):
        self.position = position
        self.orientation = orientation
        self.velocity = velocity
        self.rotation = rotation
        self.speed = speed

class Steering:

    def __init__(self, linear = pygame.math.Vector2(0.0, 0.0), angular = 0.0):
        self.linear = linear
        self.angular = angular