from typing import Union
import pytest
import random


def rand(loop: Union[float, int], value: int):
    loop = int(loop)
    count = 0

    for _ in range(loop):
        rand = random.randint(0, 100)
        if rand <= value:
            count += 1
    result = count / loop
    return result


@pytest.mark.parametrize("loop,value", [(1e2, 50), (1e5, 50), (1e7, 50), (2e7, 50)])
def test_rand(loop: int, value: int):
    assert rand(loop, value) == 0.5


# pytest -n auto random_test.py
