import pygame
import os

from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

path = "/".join(os.path.abspath(__file__).split("/")[:-1])
# print(path)
pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)
sprite1 = pygame.image.load(f"{path}/images/butterfly.png")
sprite1 = pygame.transform.scale(sprite1, (50, 50))
spriteWidth = sprite1.get_width()
spriteHeight = sprite1.get_height()


pygame.display.set_caption("Hello REsize")

game_over = False

x, y = (0, 0)

clock = pygame.time.Clock()

while not game_over:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos

            x -= spriteWidth / 2
            y -= spriteHeight / 2

    pressed = pygame.key.get_pressed()
    if pressed[K_UP]:
        y -= 0.5 * dt
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    screen.fill((0, 0, 0))
    screen.blit(sprite1, (x, y))
    pygame.display.update()

pygame.quit()
