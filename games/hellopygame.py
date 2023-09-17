import pygame

pygame.init()

screen = pygame.display.set_mode((640, 840), 0, 32)
pygame.display.set_caption("Hello Pygame")
screen.fill((0, 0, 0))
game_over = False

# while not game_over:
#     for event in pygame.event.get() :
#         if event.type == pygame.QUIT:
#             game_over = True


pygame.quit()


# def add_two_tuples(x: tuple(), y: list) -> str:
#     x1, x2 = x

#     y = y[0]
#     return y + x1 + x2


# add_two_tuples(1, 2, 3)
