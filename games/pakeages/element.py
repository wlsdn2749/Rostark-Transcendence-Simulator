from typing import Any
import pygame
import inspect

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

diagonal_y = [-1, 1, -1, 1]  # 대각선 x : 1, 5, 7, 11
diagonal_x = [-1, 1, 1, -1]  # 대각선 y : 1, 5, 7, 11


class Element:
    def __init__(self) -> None:
        pass

    def get_image(self, path: str) -> pygame.Surface:
        self.image = pygame.image.load(path)
        return self.image

    def transform(self, width: int, height: int) -> None:
        self.image = pygame.transform.scale(self.image, (width, height))


class ThunderStroke(Element):
    """
    - 등급 : 일반
    - 효과 : 선택한 석판 100% **타격**, 가로 세로 1칸 50% **타격**
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/thunderstroke.jpg")

    def effect_range(self, x: int, y: int) -> list[tuple[int, int, int]]:
        range_list = list()
        range_list.append((x, y, 100))  # 상하좌우 100%
        for i in range(4):
            range_list.append((x + dx[i], y + dy[i], 50))  # 상하좌우 한칸씩 50%

        return range_list


class WaterSpout(Element):
    """
    - 등급 : 일반
    - 효과 : 선택한 석판 100% **타격**, 대각선 1칸 50% **타격**
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/waterspout.png")

    def effect_range(self, x: int, y: int) -> list[tuple[int, int, int]]:
        range_list = list()
        range_list.append((x, y, 100))  # 상하좌우 100%
        for i in range(4):
            range_list.append((x + diagonal_x[i], y + diagonal_y[i], 50))
            # 대각선 한칸씩 50%

        return range_list


class HellFire(Element):
    """
    - 등급 : 일반
    - 효과 : 선택한 석판 100% **타격**, 대각선 1칸 50% **타격** 가로 세로 2칸씩 50% 타격
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/hellfire.jpg")

    def effect_range(self, x: int, y: int) -> list[tuple[int, int, int]]:
        range_list = list()
        range_list.append((x, y, 100))  # 상하좌우 100%
        for i in range(4):
            range_list.append((x + diagonal_x[i], y + diagonal_y[i], 50))
            # 대각선 한칸씩 50%

            range_list.append((x + dx[i], y + dy[i], 50))
            # 상하좌우 한칸씩 50%

            range_list.append((x + 2 * dx[i], y + 2 * dy[i], 50))
            # 상하좌우 두칸씩 50%

        return range_list


def get_all_elements() -> list[Any]:
    current_module = inspect.getmodule(inspect.currentframe())
    elements = []
    for name, obj in inspect.getmembers(current_module):
        if inspect.isclass(obj) and obj.__name__ != "Element":
            elements.append(obj)

    return elements


# if __name__ == "__main__":
#     cls = get_all_elements()
#     for c in cls:
#         print(c.__name__, c)
