from typing import Any
import random

from pakeages.element import get_all_elements


def is_destroy(value: int) -> bool:
    rand = random.randint(1, 100)  # [1, 100]
    if rand <= value:  # value %
        return True

    return False


def random_slots_element_init(init_value: int = 20) -> list[Any]:  # 초기값 기본 20
    elements = get_all_elements()
    # print(elements)
    random_slots = [random.choice(elements) for i in range(init_value)]
    return random_slots
