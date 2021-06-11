import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super(Wall, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.set_position(x, y)

    def set_position(self, x, y):
        if x is not None:
            self.rect.x = x
        if y is not None:
            self.rect.y = y

    def get_position(self):
        return self.rect.x, self.rect.y