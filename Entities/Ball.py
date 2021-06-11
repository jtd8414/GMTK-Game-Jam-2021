import pygame
import shared_variables
from random import randint


class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height, x, y):
        # Call the parent class (Sprite) constructor
        super(Ball, self).__init__()

        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.surf = pygame.Surface([width, height])
        self.surf.fill(shared_variables.BLACK)
        self.surf.set_colorkey(shared_variables.BLACK)
        self.rect = self.surf.get_rect()
        self.set_position(x, y)

        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.surf, color, [0, 0, width, height])

        # todo need to make this variable on the screen size
        self.velocity = [randint((shared_variables.SCREEN_WIDTH // 500), (shared_variables.SCREEN_WIDTH // 500) + 5),
                         randint(-(shared_variables.SCREEN_HEIGHT // 500), (shared_variables.SCREEN_HEIGHT // 500))]
        self.velocity = [randint(4, 8), randint(-8, 8)]

        # Fetch the rectangle object that has the dimensions of the image.

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def set_position(self, x, y):
        if x is not None:
            self.rect.x = x
        if y is not None:
            self.rect.y = y

    def handle_collision(self, left_wall, right_wall):
        if self.rect.colliderect(left_wall.rect):
            self.velocity[0] = -self.velocity[0]
        if self.rect.colliderect(right_wall.rect):
            self.velocity[0] = -self.velocity[0]

        if self.rect.y > (shared_variables.SCREEN_HEIGHT - 10):
            self.velocity[1] = -self.velocity[1]
        if self.rect.y < 0:
            self.velocity[1] = -self.velocity[1]