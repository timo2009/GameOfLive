from world import World
import pygame

CELL_SIZE = 2
SIZE = 750
FPS = 10
RANDOM = True
DENSITY = 0.05


def render(screen, world, zoom, offset_x, offset_y):
    screen.fill((0, 0, 0))

    for x, y in world.alive:
        sx = int((y * CELL_SIZE * zoom) + offset_x)
        sy = int((x * CELL_SIZE * zoom) + offset_y)

        size = max(1, int(CELL_SIZE * zoom))

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (sx, sy, size, size)
        )

    draw_zoom_bar(screen, zoom)

    pygame.display.flip()


def draw_zoom_bar(screen, zoom):
    screen_width, screen_height = screen.get_size()

    bar_width = 200
    bar_height = 10

    x = 20
    y = screen_height - 30

    # Hintergrund
    pygame.draw.rect(screen, (60, 60, 60), (x, y, bar_width, bar_height))

    # Zoom normalisieren (logisch begrenzt)
    min_zoom = 0.1
    max_zoom = 20

    normalized = (zoom - min_zoom) / (max_zoom - min_zoom)
    normalized = max(0, min(1, normalized))

    # Füllung
    pygame.draw.rect(
        screen,
        (0, 200, 0),
        (x, y, int(bar_width * normalized), bar_height)
    )


pygame.init()

screen = pygame.display.set_mode((SIZE * CELL_SIZE, SIZE * CELL_SIZE))

world = World(SIZE, RANDOM, DENSITY)

running = True
clock = pygame.time.Clock()

zoom = 1.0
offset_x = 0
offset_y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEWHEEL:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            world_x = (mouse_x - offset_x) / zoom
            world_y = (mouse_y - offset_y) / zoom

            factor = 1.1 if event.y > 0 else 0.9
            new_zoom = zoom * factor
            new_zoom = max(0.1, min(new_zoom, 20))

            offset_x = mouse_x - world_x * new_zoom
            offset_y = mouse_y - world_y * new_zoom

            zoom = new_zoom

    world.step()
    render(screen, world, zoom, offset_x, offset_y)

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