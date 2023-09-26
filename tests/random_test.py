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


def rand_sample(init_value: int = 20):
    li = ["A", "B"]
    result = [random.choice(li) for i in range(init_value)]
    print(result)
    return result


@pytest.mark.parametrize("loop,value", [(1e2, 50), (1e5, 50)])
def test_rand(loop: int, value: int):
    assert rand(loop, value) == 0.5


@pytest.mark.parametrize("init_value", [20, 30, 40, 50])
def test_rand_sample(init_value: int):
    assert len(rand_sample(init_value)) == init_value


print(rand_sample())
if __name__ == "__main__":
    print(test_rand_sample(20))
# pytest -n auto random_test.py
