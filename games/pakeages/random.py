import random


def is_destroy(value: int) -> bool:
    rand = random.randint(1, 100)  # [1, 100]
    if rand <= value:  # value %
        return True

    return False
