import pygame
from typing import Any

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
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

    def get_image(self, path: str) -> pygame.Surface:
        self.image = pygame.image.load(path)
        return self.image

    def transform(self, width: int, height: int) -> None:
        self.image = pygame.transform.scale(self.image, (width, height))


class ThunderStroke(Element):
    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/thunderstroke.jpg")


class WaterSpout(Element):
    def __init__(self) -> None:
        super().__init__()
        self.image = self.get_image("./games/images/waterspout.png")


class Card:
    def __init__(self, name: str) -> None:
        self.name = name
        self.element: Any = None
        self.make()

    def make(self) -> None:
        if self.name == "thunderstroke":
            self.element = ThunderStroke()
        elif self.name == "waterspout":
            self.element = WaterSpout()


class Slot(pygame.Rect):  # type: ignore
    """
    Class to store two elements
    """

    def __init__(self, *args: int, **kwargs: int) -> None:
        super().__init__(*args, **kwargs)
        self.selected = False

    def create(self, surface: pygame.surface.Surface) -> None:
        # pygame.draw.rect(surface, TILE1, self)  # 채우기
        if not self.selected:
            pygame.draw.rect(surface, WHITE, self, 2)  # 하얀색으로 Boarding
        else:
            pygame.draw.rect(surface, YELLOW, self, 2)  # 노란색으로 Boarding

    def assign(self, surface: pygame.surface.Surface, card: Card) -> None:
        card.element.transform(self.width, self.height)
        surface.blit(card.element.image, self)
        self.create(surface)  # 테두리 다시 그려주기

    def toggle_select(self, surface: pygame.surface.Surface) -> None:
        self.selected = not self.selected
        self.create(surface)


# if __name__ == "__main__":
#     t = Tile(50, 50, 50, 50)
#     print(t)
