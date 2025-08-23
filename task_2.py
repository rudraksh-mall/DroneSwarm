import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Task 2: Player & Enemy")

WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)

class Player:
    def __init__(self, x, y, width=40, height=40, speed=5):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect)


class Enemy:
    def __init__(self, x, y, width=40, height=40, speed=3):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:  # Respawn at top
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = -self.rect.height

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)


player = Player(WIDTH//2, HEIGHT-60)
enemy = Enemy(random.randint(0, WIDTH-40), -40)
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    keys = pygame.key.get_pressed()
    player.update(keys)
    enemy.update()

    # Collision check
    if player.rect.colliderect(enemy.rect):
        print("Collision!")
        running = False  
        
    # Draw
    player.draw(screen)
    enemy.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
