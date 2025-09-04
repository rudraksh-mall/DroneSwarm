import pygame
import random
import math

WIDTH, HEIGHT = 800, 600
NUM_DRONES = 200       
MAX_SPEED = 3         
NEIGHBOR_DIST = 40   
SEPARATION_FORCE = 0.07  

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drone Swarm - Separation Rule")
clock = pygame.time.Clock()

class Drone(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((12, 12), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (200, 50, 255), (6, 6), 6)
        self.rect = self.image.get_rect(center=(x, y))
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))

    def update(self, swarm):
        steer = pygame.math.Vector2(0, 0)
        for other in swarm:
            if other == self:
                continue
            dist = self.pos.distance_to(other.pos)
            if dist < NEIGHBOR_DIST and dist > 0: 
                diff = self.pos - other.pos
                diff /= dist   
                steer += diff

        self.vel += steer * SEPARATION_FORCE

        if self.vel.length() > MAX_SPEED:
            self.vel = self.vel.normalize() * MAX_SPEED

        self.pos += self.vel

        if self.pos.x < 0: self.pos.x = WIDTH
        if self.pos.x > WIDTH: self.pos.x = 0
        if self.pos.y < 0: self.pos.y = HEIGHT
        if self.pos.y > HEIGHT: self.pos.y = 0

        self.rect.center = self.pos

drones = pygame.sprite.Group()
for _ in range(NUM_DRONES):
    d = Drone(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    drones.add(d)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for d in drones:
        d.update(drones)

    screen.fill((25, 25, 25))
    drones.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
