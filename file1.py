from typing import List


def get_same_numbers(list_1: List[int], list_2: List[int]) -> List[int]:
    return [i for i in list_1 if i in list_2]


print(get_same_numbers([1, 2, 3, 4], [3, 4, 5, 6]))
