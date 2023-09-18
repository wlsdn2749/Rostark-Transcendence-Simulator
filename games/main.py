import pygame
import sys
import os
from typing import List

# 절대 경로 참조
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pakeages.gameobject import Tile  # noqa: E402

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
TILE1 = (0, 51, 102)

# Total Window
screen = pygame.display.set_mode((600, 800))

# Title and Icon
pygame.display.set_caption("ROSTARK Transcendence Simulator")


game_over = False

screen.fill(BLACK)
# 아래 칸 남겨놓기 (정령, 정령 수납 칸)
pygame.draw.line(screen, WHITE, (0, 600), (600, 600), 5)

# 타일 프레임 그리기
r1 = Tile(50, 50, 500, 500)
r1.draw(screen, RED, 10)


# 타일 그리기
tiles: List[Tile] = [[] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        tiles[i].append(Tile(50 + i * 100, 50 + j * 100, 100, 100))

for i in range(5):
    for j in range(5):
        target_tile = tiles[i][j]
        tiles[i][j].draw(screen, TILE1)
        tiles[i][j].draw(screen, WHITE, 2)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            try:
                target_tile = tiles[(x - 50) // 100][(y - 50) // 100]
                target_tile.draw(screen, RED)
                target_tile.draw(screen, WHITE, 2)
                print(x, y)
            except Exception as e:
                print(e)

    # 그린 선 반영
    pygame.display.update()


pygame.quit()
