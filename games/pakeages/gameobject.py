import pygame
from typing import Optional, Tuple


class Tile(pygame.Rect):  # type: ignore
    """
    Class to create a new tile in pygame window
    """

    def __init__(self, *args: int, **kwargs: int) -> None:
        super().__init__(*args, **kwargs)

    def draw(
        self,
        surface: pygame.surface.Surface,
        color: Tuple[int, int, int],  # RGB
        width: Optional[int] = 0,
    ) -> None:
        pygame.draw.rect(surface, color, self, width)


# if __name__ == "__main__":
#     t = Tile(50, 50, 50, 50)
#     print(t)
