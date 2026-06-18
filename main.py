from world import World
import pygame

CELL_SIZE = 10
SIZE = 100
FPS = 7
RANDOM = True
DENSITY = 0.1

def render(screen, world):
    screen.fill((0, 0, 0))

    for x, y in world.alive:
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )

    pygame.display.flip()


pygame.init()

screen = pygame.display.set_mode((SIZE * CELL_SIZE, SIZE * CELL_SIZE))

world = World(SIZE, RANDOM, DENSITY)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world.step()
    render(screen, world)

    clock.tick(FPS)

pygame.quit()


# from world import World
# import pygame
#
# CELL_SIZE = 10
# SIZE = 1000
# FPS = 7
# RANDOM = True
# START_POINTS = []
#
# def render(screen, world):
#     screen.fill((0, 0, 0))
#
#     for x in range(len(world.matrix)):
#         for y in range(len(world.matrix[x])):
#             color = (255, 255, 255) if world.matrix[x][y] == 1 else (30, 30, 30)
#
#             pygame.draw.rect(
#                 screen,
#                 color,
#                 (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
#             )
#
#     pygame.display.flip()
#
# pygame.init()
#
# screen = pygame.display.set_mode((SIZE * CELL_SIZE, SIZE * CELL_SIZE))
#
# world = World(SIZE, RANDOM, START_POINTS)
#
# running = True
# clock = pygame.time.Clock()
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     world.step()
#     render(screen, world)
#
#     clock.tick(FPS)
#
# pygame.quit()