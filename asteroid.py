import pygame
import random
from constants import *
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(new_angle)
            velocity2 = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            smaller1 = Asteroid(self.position[0], self.position[1], new_radius)
            smaller1.velocity = velocity1 * 1.2
            smaller2 = Asteroid(self.position[0], self.position[1], new_radius)
            smaller2.velocity = velocity2 * 1.2
