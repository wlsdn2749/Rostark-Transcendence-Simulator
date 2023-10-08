from typing import Any, List
import random


def is_destroy(value: int) -> bool:
    rand = random.randint(1, 100)  # [1, 100]
    if rand <= value:  # value %
        return True

    return False


def is_create(value: int) -> bool:
    rand = random.randint(1, 100)  # [1, 100]
    if rand <= value:  # value %
        return True

    return False


def random_number_int(range_from: int, range_to: int) -> int:
    number = random.randint(range_from, range_to)
    return number


def random_tile_select(
    candidate_tiles: List[tuple[int, int]], break_number: int
) -> List[tuple[int, int]]:
    if len(candidate_tiles) >= break_number:
        # tile이 항상 count보다 많아야 샘플 추출이 가능
        selected_tile = random.sample(candidate_tiles, break_number)
    else:
        selected_tile = []

    return selected_tile


def random_slots_element_init(
    init_value: int = 20, elements: List[Any] = []
) -> List[Any]:  # 초기값 기본 20
    # print(elements)
    random_slots = [random.choice(elements) for i in range(init_value)]
    return random_slots
