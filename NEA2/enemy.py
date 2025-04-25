import pygame

class Enemy:
    def __init__(self, camera_pos, map_width, map_height):
        # Calculate the opposite position
        self.x = map_width - camera_pos.x
        self.y = map_height - camera_pos.z
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        # Update enemy logic here
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)