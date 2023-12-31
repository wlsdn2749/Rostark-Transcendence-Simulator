from typing import Any, List
import sys
import os
import pygame
import inspect

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# from pakeages.gameobject import Tile # noqa: E402
from pakeages.random_object import random_number_int, random_tile_select  # noqa: E402

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]  # 0: 아래쪽(남), 1: 오른쪽(동), 2: 위쪽(북), 3: 왼쪽(서)

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
    - 이름 : 낙뢰
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
    - 이름 : 용오름
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
    - 이름 : 업화
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


class BigExplosion(Element):
    """
    - 이름 : 대폭발
    - 등급 : 일반
    - 효과 : 선택한 석판 100% **타격**
    - 선택한 지점 기준대각선 모두 타격
    - 확률은 선택한 지점으로 부터 1칸 떨어질 때마다 -15% 씩 감소
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/bigexplosion.png")

    def effect_range(self, x: int, y: int) -> list[tuple[int, int, int]]:
        range_list = list()
        range_list.append((x, y, 100))  # 선택지점 100%
        for p in range(6):
            for i in range(4):
                range_list.append(
                    (x + p * diagonal_x[i], y + p * diagonal_y[i], 100 - p * 15)
                )
            # 대각선 한칸씩 50%

            # 상하좌우 두칸씩 50%

        return range_list


class RainStorm(Element):
    """
    - 이름 : 폭풍우
    - 등급 : 일반
    - 효과 : 선택한 석판 100% **타격**
    - 선택한 지점 기준대각선 모두 타격
    - 확률은 선택한 지점으로 부터 1칸 떨어질 때마다 -15% 씩 감소
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/rainstorm.jpg")

    def effect_range(self, x: int, y: int) -> list[tuple[int, int, int]]:
        range_list = list()
        range_list.append((x, y, 100))  # 선택한 지점 100%
        for p in range(6):
            for i in [0, 2]:
                range_list.append((x + p * dx[i], y + p * dy[i], 100 - p * 15))

            # 상하 모두 타격 한칸 떨어질때마다 -15% 씩 감소

        return range_list


class Tsunami(Element):
    """
    - 이름 : 해일
    - 등급 : 일반
    - 효과 : 선택한 석판 100% **타격**
    - 선택한 지점 기준 가로 세로 모두 타격
    - 확률은 선택한 지점으로 부터 1칸 떨어질 때마다 -15% 씩 감소
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/tsunami.jpg")

    def effect_range(self, x: int, y: int) -> list[tuple[int, int, int]]:
        range_list = list()
        range_list.append((x, y, 100))  # 선택한 지점 100%
        for p in range(6):
            for i in range(4):
                range_list.append((x + p * dx[i], y + p * dy[i], 100 - p * 15))

            # 상하 모두 타격 한칸 떨어질때마다 -15% 씩 감소

        return range_list


class Earthquakes(Element):
    """
    - 이름 : 지진
    - 등급 : 일반
    - 효과 : 선택한 석판 100% **타격**
    - 선택한 지점 기준 가로
    - 확률은 선택한 지점으로 부터 1칸 떨어질 때마다 -15% 씩 감소
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/earthquakes.jpg")

    def effect_range(self, x: int, y: int) -> list[tuple[int, int, int]]:
        range_list = list()
        range_list.append((x, y, 100))  # 선택한 지점 100%
        for p in range(6):
            for i in [1, 3]:
                range_list.append((x + p * dx[i], y + p * dy[i], 100 - p * 15))

            # 상하 모두 타격 한칸 떨어질때마다 -15% 씩 감소

        return range_list


class Shockwave(Element):
    """
    - 이름 : 충격파
    - 등급 : 일반
    - 효과 : 선택한 석판 100% **타격**
    - 대각선 1칸 75% **타격** 가로 세로 1칸씩 75% 타격
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/shockwavestomp.jpg")

    def effect_range(self, x: int, y: int) -> list[tuple[int, int, int]]:
        range_list = list()
        range_list.append((x, y, 100))  # 지점 100%
        for i in range(4):
            range_list.append((x + diagonal_x[i], y + diagonal_y[i], 75))
            # 대각선 한칸씩 75%

            range_list.append((x + dx[i], y + dy[i], 75))
            # 상하좌우 한칸씩 75%

        return range_list


class Yggdrasil_resonance(Element):
    """
    - 이름 : 세계수의 공명
    - 등급 : 일반
    - 효과 : 선택한 석판 100% **타격**
    - 가로 세로 2칸씩 100% 타격
    - "정령이 머무른 석판: 신비" 파괴시 일정 확률로 등장
    - 강화되지 않는 정령효과
    - "왜곡된 고대 석판"의 효과를 무시하고 파괴가능
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/yggdrasil_resonance.jpeg")

    def effect_range(self, x: int, y: int) -> list[tuple[int, int, int]]:
        range_list = list()
        range_list.append((x, y, 100))  # 지점 100%
        for i in range(4):
            range_list.append((x + dx[i], y + dy[i], 100))
            # 상하좌우 한칸씩 100%

            range_list.append((x + 2 * dx[i], y + 2 * dy[i], 100))
            # 상하좌우 두칸씩 100%

        return range_list


class Eruption(Element):
    """
    - 이름 : 분출
    - 등급 : 일반
    - 효과 : 선택한 석판 100% **타격**
    - "정령이 머무른 석판: 신비" 파괴시 일정 확률로 등장
    - 강화되지 않는 정령효과
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/eruption.jpg")

    def effect_range(self, x: int, y: int) -> list[tuple[int, int, int]]:
        range_list = list()
        range_list.append((x, y, 100))  # 100%

        return range_list


class Cleanse(Element):
    """
    - 이름 : 정화
    - 등급 : 일반
    - 효과 : 선택한 석판 100% **타격**, 양 옆 석판 50% 파괴
    - "왜곡된 고대 석판"의 효과를 무시하고 파괴가능
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/cleanse.jpg")

    def effect_range(self, x: int, y: int) -> list[tuple[int, int, int]]:
        range_list = list()
        range_list.append((x, y, 100))  # 100%
        for i in [1, 3]:
            range_list.append((x + dx[i], y + dy[i], 50))  # 양 옆 50%

        return range_list


class LightningBolt(Element):
    """
    - 이름 : 벼락
    - 등급 : 일반
    - 효과 : 선택한 석판 100% 타격->무작위 석판 0~2개 파괴 ->무작위 석판 0~1개 재생성


    - effect_range 구하는 프로세스
    - 1. 0~2를 랜덤으로 정함 확률은 uniform_random(확률 동일)
    - 2. 선택된 타일 제외 부서지지 않은 타일을 랜덤으로 1에서 정한 만큼 타격(확률 동일)
    - 3. 2에서 부서진 타일 포함 아직 부서지지 않은 타일 1개 50% 확률로 재생성
        = (0~1) 랜덤과 같음
    """

    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/lightningbolt.jpeg")

    def effect_range(
        self, x: int, y: int, tiles: List[Any]
    ) -> tuple[
        list[tuple[int, int, str]],
        list[tuple[int, int, int]],
        list[tuple[int, int, int]],
    ]:  # effect, break, restore
        range_list = list()

        # 1. Part
        break_number = random_number_int(0, 2)  # 0~2 랜덤
        restore_number = random_number_int(0, 1)  # 0~1 랜덤
        # 2. Part
        break_candidate_tiles = []
        restore_candidate_tiles = [(x, y)]  # 자기도 부셔질 수 있다.
        for i in range(len(tiles)):
            for j in range(len(tiles[i])):
                if x == i and y == j:  # 선택된 타일은 무조건 깨지므로 랜덤에 안넣음
                    continue
                if tiles[i][j].enabled is True:
                    break_candidate_tiles.append((i, j))
                    range_list.append((i, j, "?"))  # 표시를 위함

                else:
                    restore_candidate_tiles.append((i, j))

        break_tiles = random_tile_select(
            break_candidate_tiles, break_number
        )  # 부셔야할 좌표 x,y 반환

        def convert(tup: tuple[int, int]) -> tuple[int, int, int]:
            return tup[0], tup[1], 100  # 하는 함수 x, y -> x,y,100

        break_tiles = list(map(convert, break_tiles))

        break_tiles.append((x, y, 100))  # 선택한 지점 포함
        range_list.append((x, y, "100"))  # 100% 선택한 지점은 100%

        restore_tiles = random_tile_select(
            restore_candidate_tiles, restore_number
        )  # 생성되야할 좌표 x,y
        restore_tiles = list(map(convert, restore_tiles))

        return range_list, break_tiles, restore_tiles  # 범위


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
