import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
DARK_RED = (150, 30, 30)
TILE1 = (0, 51, 102)


class Tile(pygame.Rect):  # type: ignore
    """
    Class to create a new tile in pygame window
    """

    def __init__(self, *args: int, **kwargs: int) -> None:
        super().__init__(*args, **kwargs)
        self.enabled = False

    def create(self, surface: pygame.surface.Surface) -> None:
        pygame.draw.rect(surface, TILE1, self)  # 채우기
        pygame.draw.rect(surface, WHITE, self, 2)  # 하얀색으로 Boarding
        self.enabled = True  # 생성됬다고 표시

    def destroy(self, surface: pygame.surface.Surface) -> None:
        pygame.draw.rect(surface, BLACK, self)  # 검은색으로 -> 배경
        pygame.draw.rect(surface, WHITE, self, 2)  # 외곽선은 그대로
        self.enabled = False  # 파괴됬다고 표시


class Element:
    def __init__(self) -> None:
        pass


class Card(Element):
    def __init__(self) -> None:
        super().__init__()


# if __name__ == "__main__":
#     t = Tile(50, 50, 50, 50)
#     print(t)
