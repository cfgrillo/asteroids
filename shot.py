import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, position, radius):
        super().__init__(position.x, position.y, radius)
        self.shot_velocity = self.velocity * PLAYER_SHOOT_SPEED 

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)
    
    def update(self, dt):
        self.position += (self.velocity * dt)