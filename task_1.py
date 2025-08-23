import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Moving Player")

class Player:
    def __init__(self,x,y,width = 20,height = 20,speed = 5):
        self.rect = pygame.Rect(x,y,width,height)
        self.speed = speed
    
    def update(self,keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        
        self.rect.x = max(0,min(self.rect.x,600 - self.rect.width))
        self.rect.y = max(0,min(self.rect.y,800 - self.rect.height))

    def draw(self,surface):
        pygame.draw.rect(surface,(0,0,255),self.rect)

player = Player(300,400)
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
    
    keys = pygame.key.get_pressed()
    player.update(keys)

    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
