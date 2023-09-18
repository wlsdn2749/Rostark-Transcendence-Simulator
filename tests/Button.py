import os
import pygame

path = "/".join(os.path.abspath(__file__).split("/")[:-1])
pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Hello BUtton")

text_color = (255, 255, 255)
button_color = (0, 0, 170)
button_over_color = (255, 50, 50)

button_width = 100
button_height = 50

x = screen.get_width() / 2 - button_width / 2
y = screen.get_height() / 2 - button_height / 2
button_rect = [x, y, button_width, button_height]


game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.draw.rect(screen, button_color, button_rect)
    pygame.display.update()

pygame.quit()
