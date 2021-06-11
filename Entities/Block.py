import pygame
import shared_variables
from enum import Enum


class Block(pygame.sprite.Sprite):
    def __init__(self, color, block_type):
        super(Block, self).__init__()
        self.surf = pygame.Surface((shared_variables.BLOCK_WIDTH, shared_variables.BLOCK_HEIGHT))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.type = "red"
        self.block_type = block_type

    def setPosition(self, x, y):
        if x is not None:
            self.rect.x = x
        if y is not None:
            self.rect.y = y

    def getPosition(self):
        return self.rect.x, self.rect.y

    def handle_collision(self, ball, blocks):
        if self.rect.colliderect(ball.rect):
            ball.velocity[1] = -ball.velocity[1]
            self.kill()
            blocks.remove(self)
            return self.get_points()
        return 0

    def get_points(self):
        if self.block_type == BlockType.LVL_1:
            return 1
        if self.block_type == BlockType.LVL_2:
            return 3
        if self.block_type == BlockType.LVL_3:
            return 5
        if self.block_type == BlockType.LVL_4:
            return 7


class BlockType(Enum):
    LVL_1 = 1
    LVL_2 = 2
    LVL_3 = 3
    LVL_4 = 4
