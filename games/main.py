import pygame
import sys
import os
from collections import deque
from typing import List

# 절대 경로 참조
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pakeages.gameobject import Tile, Slot, Card  # noqa: E402
from pakeages.random import is_destroy  # noqa : E402


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLACK = (69, 69, 69)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
DARK_RED = (150, 30, 30)
TILE1 = (0, 51, 102)

# Total Window
screen = pygame.display.set_mode((600, 800))

# Title and Icon
pygame.display.set_caption("ROSTARK Transcendence Simulator")


game_over = False

screen.fill(LIGHT_BLACK)
# 아래 칸 남겨놓기 (정령, 정령 수납 칸)
pygame.draw.line(screen, WHITE, (0, 600), (600, 600), 5)

# 타일 프레임 그리기
# r1 = Tile(50, 50, 500, 500)
# r1.draw(screen, RED, 10)


# 타일 그리기
tiles: List[Tile] = [[] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        tiles[i].append(Tile(50 + i * 100, 50 + j * 100, 100, 100))  # 위치 지정

for i in range(5):
    for j in range(5):
        target_tile = tiles[i][j]
        target_tile.create(screen)

# 정령 보관 슬롯 그리기
slots: List[Slot] = []
slots.append(Slot(300, 625, 100, 125))  # (300, 625) ~ (400, 750)
slots.append(Slot(425, 625, 100, 125))  # (425, 625) ~ (525, 750)
slots[0].create(screen)
slots[1].create(screen)

# 다음 정령 슬롯 그리기

next_slots: deque[Slot] = deque()
next_slots.appendleft(Slot(50, 700, 60, 75))
next_slots.appendleft(Slot(125, 700, 60, 75))
next_slots.appendleft(Slot(200, 700, 60, 75))
next_slots[0].create(screen)
next_slots[1].create(screen)
next_slots[2].create(screen)

# 슬롯에 정령 할당하기
thunderstroke_card = Card(name="thunderstroke")
slots[0].assign(screen, thunderstroke_card)

waterspout_card = Card(name="waterspout")
slots[1].assign(screen, waterspout_card)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 50 <= x <= 550 and 50 <= y <= 550:  # Tile Event
                x, y = (x - 50) // 100, (y - 50) // 100
                if slots[0].selected:
                    effect_range = slots[0].card.element.effect_range(x, y)
                if slots[1].selected:
                    effect_range = slots[1].card.element.effect_range(x, y)

                if effect_range:
                    for x, y, value in effect_range:
                        if 0 <= x <= 4 and 0 <= y <= 4:
                            if tiles[x][y].enabled:
                                if is_destroy(value):
                                    tiles[x][y].destroy(screen)

                # target_tile = tiles[(x - 50) // 100][(y - 50) // 100]
                # target_tile.destroy(screen)

                # print(x, y, value, tiles[x][y].enabled)
            elif 300 <= x <= 400 and 625 <= y <= 725:  # ! Slot 0
                slots[0].toggle_select(screen)
                if slots[1].selected:
                    slots[1].toggle_select(screen)
            elif 425 <= x <= 525 and 625 <= y <= 725:  # ! Slot 1
                slots[1].toggle_select(screen)
                if slots[0].selected:
                    slots[0].toggle_select(screen)

            else:
                print(x, y)
                print("바깥쪽")

    # 슬롯이 골라졌을때 마우스가 타일 위로 올라감을 감지
    effect_range = None
    if slots[0].selected or slots[1].selected:
        mouse_pos = pygame.mouse.get_pos()

        # 마우스가 특정 타일 위로 올라갔을 경우 특정 타일과 그 인접 타일 위치를 저장
        for i in range(5):
            for j in range(5):
                if tiles[i][j].collidepoint(mouse_pos) and tiles[i][j].enabled:
                    if slots[0].selected:
                        effect_range = slots[0].card.element.effect_range(i, j)
                    if slots[1].selected:
                        effect_range = slots[1].card.element.effect_range(i, j)

                # 모든 타일을 갱신
                if tiles[i][j].enabled:
                    tiles[i][j].create(screen)
                else:
                    tiles[i][j].destroy(screen)

        # 표시해야할 타일이 있을 경우 그 위치를 퍼센트 표시
        if effect_range:
            for x, y, value in effect_range:
                if 0 <= x <= 4 and 0 <= y <= 4:
                    if tiles[x][y].enabled:
                        tiles[x][y].show(screen, value)
                        print(x, y, value)

    # 그린 선 반영
    pygame.display.update()


pygame.quit()
