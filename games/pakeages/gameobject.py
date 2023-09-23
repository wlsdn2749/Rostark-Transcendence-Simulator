import pygame
from typing import Any
from pakeages.element import ThunderStroke, WaterSpout  # noqa: E402

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARK_RED = (150, 30, 30)
TILE1 = (0, 51, 102)
TILE_SELECTED = (33, 134, 202)

pygame.font.init()
font = pygame.font.Font("./games/fonts/HeirofLightBold.ttf", 25)


class Tile(pygame.Rect):  # type: ignore
    """
    Class to create a new tile in pygame window
    """

    def __init__(self, *args: int, **kwargs: int) -> None:
        super().__init__(*args, **kwargs)
        self.enabled = False
        self.selected = False

    def create(self, surface: pygame.surface.Surface) -> None:
        pygame.draw.rect(surface, TILE1, self)  # 채우기
        pygame.draw.rect(surface, WHITE, self, 2)  # 하얀색으로 Boarding
        self.enabled = True  # 생성됬다고 표시

    def destroy(self, surface: pygame.surface.Surface) -> None:
        pygame.draw.rect(surface, BLACK, self)  # 검은색으로 -> 배경
        pygame.draw.rect(surface, WHITE, self, 2)  # 외곽선은 그대로
        self.enabled = False  # 파괴됬다고 표시

    def show(self, surface: pygame.surface.Surface, value: int) -> None:
        # font.render(text, 안티엘리어싱, 색 지정(rgb), 텍스트 배경색(rgb))

        pygame.draw.rect(surface, TILE_SELECTED, self)  # TILE_SELECTED으로 Boarding
        pygame.draw.rect(surface, WHITE, self, 2)  # 하얀색으로 Boarding

        text_surface = font.render(f"{value}%", True, WHITE)

        # CHATGPT
        text_width, text_height = text_surface.get_size()

        # Calculate the position to center the text within the rectangle
        text_x = self.x + (self.width - text_width) // 2
        text_y = self.y + (self.height - text_height) // 2

        surface.blit(text_surface, (text_x, text_y))

        # CHATGPT_END


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
        self.card: Card = card  # card 등록
        surface.blit(card.element.image, self)
        self.create(surface)  # 테두리 다시 그려주기

    def toggle_select(self, surface: pygame.surface.Surface) -> None:
        self.selected = not self.selected
        self.create(surface)


# if __name__ == "__main__":
#     t = Tile(50, 50, 50, 50)
#     print(t)
