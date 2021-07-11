from shmup.entities.enemies.steering_data import KinematicStatus, Steering

class Seek:

    def __init__(self, acceleration):
        self.__acceleration = acceleration
        self.needs_orientation = True

    def calculate(self, character = KinematicStatus(), target = KinematicStatus()):
        result = Steering()
        #acceleration towards the target
        result.linear = (target.position - character.position).normalize() * self.__acceleration
        result.angular = 0.0   #no angular

        return result