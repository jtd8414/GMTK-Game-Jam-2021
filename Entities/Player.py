import pygame
import shared_variables
from pygame.locals import (
    K_a,
    K_d,
)


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super(Player, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.set_position(x, y)

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_a]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(10, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > shared_variables.SCREEN_WIDTH:
            self.rect.right = shared_variables.SCREEN_WIDTH

    def set_position(self, x, y):
        if x is not None:
            self.rect.x = x
        if y is not None:
            self.rect.y = y

    def handle_collision(self, left_wall, right_wall, ball):
        if self.rect.colliderect(left_wall.rect):
            self.rect.x = left_wall.rect.x + self.rect.width
        if self.rect.colliderect(right_wall.rect):
            self.rect.x = right_wall.rect.x - self.rect.width
        if self.rect.colliderect(ball.rect):
            ball.velocity[1] = -ball.velocity[1]
