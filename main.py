import pygame
from pygame.locals import (
    K_a,
    K_d,
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

import shared_variables
import Entities.Player as Player
import Entities.Ball as Ball
import Entities.Wall as Wall
import Entities.Block as Block
import Utilities.screen_utility as screen_utility


def create_block_row(blocks, all_sprites, number_of_blocks, distance_between_blocks, height, color, block_type):
    first_block = None
    last_block = None
    prev_block = None

    for i in range(number_of_blocks):
        block = Block.Block(color, block_type)
        if i == 0:
            block.setPosition((shared_variables.SCREEN_WIDTH / 2)
                              - block.rect.width * (number_of_blocks // 2)
                              - (distance_between_blocks * ((number_of_blocks // 2) - 1))
                              - distance_between_blocks / 2,
                              height)
            first_block = block
        if i != 0 and prev_block is not None:
            block.setPosition((prev_block.rect.x) + block.rect.width + distance_between_blocks, height)

        if i == number_of_blocks - 1:
            last_block = block

        prev_block = block
        all_sprites.add(block)
        blocks.append(block)

    return first_block, last_block


def main():
    pygame.init()
    clock = pygame.time.Clock()
    infoObject = pygame.display.Info()

    displayIndex = 4
    DISPLAYS = [(1024, 576), (1152, 648), (1280, 720), (1600, 900), (1920, 1080), (2560, 1440), (3440, 1440)]
    shared_variables.SCREEN_WIDTH = DISPLAYS[displayIndex][0]
    shared_variables.SCREEN_HEIGHT = DISPLAYS[displayIndex][1]

    shared_variables.ASPECT_RATIO = screen_utility.calculate_aspect(shared_variables.SCREEN_WIDTH, shared_variables.SCREEN_HEIGHT)
    print(f"Resolution - Width: {shared_variables.SCREEN_WIDTH}, Height: {shared_variables.SCREEN_HEIGHT}")
    print(f"Aspect Ratio - {shared_variables.ASPECT_RATIO}")
    print(f"Screen size - ({infoObject.current_w}, {infoObject.current_h})")

    shared_variables.WHITE = (255, 255, 255)
    shared_variables.RED = (154, 0, 0)
    shared_variables.PURPLE = (255, 0, 255)
    shared_variables.BLACK = (0, 0, 0)
    shared_variables.ORANGE = (199, 128, 0)
    shared_variables.GREEN = (12, 129, 26)
    shared_variables.YELLOW = (197, 196, 0)
    shared_variables.BLUE = (1, 93, 144)

    shared_variables.BLOCK_WIDTH = shared_variables.SCREEN_WIDTH / 45.8
    shared_variables.BLOCK_HEIGHT = shared_variables.SCREEN_HEIGHT / 55
    screen = pygame.display.set_mode((shared_variables.SCREEN_WIDTH, shared_variables.SCREEN_HEIGHT), pygame.RESIZABLE)

    # instantiate the entities
    player = Player.Player(shared_variables.BLUE,
                           shared_variables.BLOCK_WIDTH * 2,
                           shared_variables.BLOCK_HEIGHT,
                           (shared_variables.SCREEN_WIDTH / 2) - (shared_variables.BLOCK_WIDTH / 2),
                           shared_variables.SCREEN_HEIGHT - 100)

    SCREEN_RATIO = shared_variables.SCREEN_HEIGHT / shared_variables.SCREEN_WIDTH

    ball = Ball.Ball(shared_variables.WHITE,
                     shared_variables.SCREEN_WIDTH / 275,
                     shared_variables.SCREEN_HEIGHT / (275 * SCREEN_RATIO),
                     (shared_variables.SCREEN_WIDTH / 2) - shared_variables.SCREEN_WIDTH / 275,
                     shared_variables.SCREEN_HEIGHT / 2)

    all_sprites = pygame.sprite.Group()

    blocks = []
    distance_between_blocks = 10
    number_of_blocks = 14
    blocks_start_y_pos = shared_variables.SCREEN_HEIGHT / 6

    first_block, last_block = create_block_row(blocks,
                                               all_sprites,
                                               number_of_blocks,
                                               distance_between_blocks,
                                               blocks_start_y_pos,
                                               shared_variables.RED,
                                               Block.BlockType.LVL_4)

    left_wall_x_position = first_block.rect.x - first_block.rect.width
    right_wall_x_position = last_block.rect.x + last_block.rect.width

    leftWall = Wall.Wall(shared_variables.WHITE, shared_variables.SCREEN_WIDTH / 50, shared_variables.SCREEN_HEIGHT, left_wall_x_position, None)
    rightWall = Wall.Wall(shared_variables.WHITE, shared_variables.SCREEN_WIDTH / 50, shared_variables.SCREEN_HEIGHT, right_wall_x_position, None)

    first_block, last_block = create_block_row(blocks, all_sprites, number_of_blocks, distance_between_blocks, first_block.rect.y + first_block.rect.height + distance_between_blocks, shared_variables.RED, Block.BlockType.LVL_4)
    first_block, last_block = create_block_row(blocks, all_sprites, number_of_blocks, distance_between_blocks, first_block.rect.y + first_block.rect.height + distance_between_blocks, shared_variables.ORANGE, Block.BlockType.LVL_3)
    first_block, last_block = create_block_row(blocks, all_sprites, number_of_blocks, distance_between_blocks, first_block.rect.y + first_block.rect.height + distance_between_blocks, shared_variables.ORANGE, Block.BlockType.LVL_3)
    first_block, last_block = create_block_row(blocks, all_sprites, number_of_blocks, distance_between_blocks, first_block.rect.y + first_block.rect.height + distance_between_blocks, shared_variables.GREEN, Block.BlockType.LVL_2)
    first_block, last_block = create_block_row(blocks, all_sprites, number_of_blocks, distance_between_blocks, first_block.rect.y + first_block.rect.height + distance_between_blocks, shared_variables.GREEN, Block.BlockType.LVL_2)
    first_block, last_block = create_block_row(blocks, all_sprites, number_of_blocks, distance_between_blocks, first_block.rect.y + first_block.rect.height + distance_between_blocks, shared_variables.YELLOW, Block.BlockType.LVL_1)
    first_block, last_block = create_block_row(blocks, all_sprites, number_of_blocks, distance_between_blocks, first_block.rect.y + first_block.rect.height + distance_between_blocks, shared_variables.YELLOW, Block.BlockType.LVL_1)

    all_sprites.add(leftWall)
    all_sprites.add(rightWall)
    all_sprites.add(player)
    all_sprites.add(ball)

    points = 0

    myfont = pygame.font.SysFont('Comic Sans MS', int(shared_variables.BLOCK_HEIGHT * 5))
    myfont = pygame.font.Font("Fonts\\font.ttf", int(shared_variables.BLOCK_HEIGHT * 5))

    running = True
    # Main loop
    while running:
        clock_delta = clock.tick(120)
        screen.fill(shared_variables.BLACK)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses
        player.update(pressed_keys)
        ball.update()

        player.handle_collision(leftWall, rightWall, ball)

        for block in blocks:
            points += block.handle_collision(ball, blocks)

        ball.handle_collision(leftWall, rightWall)

        score_obj = myfont.render(f'{points}', False, shared_variables.WHITE)
        screen.blit(score_obj, (leftWall.rect.x + leftWall.rect.width * 2, leftWall.rect.width))

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pygame.display.flip()

    pygame.quit()
    print(f"Points: {points}")


main()
