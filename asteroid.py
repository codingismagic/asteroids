import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

         
    def draw(self, screen):
         pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self,asteroids):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        random_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(random_angle) * 1.2
        new_vector2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_vector1
        asteroids.add(asteroid1)

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_vector2
        asteroids.add(asteroid2)