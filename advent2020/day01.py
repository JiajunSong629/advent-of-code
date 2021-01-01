from typing import List

inputs = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]

def find_product(inputs: List[int]) -> int:
    """
    find two elements that add up to 2020,
    return their product
    """
    d = {}
    for num in inputs:
        if num not in d:
            d[2020 - num] = True
        else:
            return num * (2020 - num)

def find_product2(inputs: List[int]) -> int:
    """
    find three elements that add up to 2020,
    return their product
    """
    for i in range(len(inputs)):
        d = {}
        for j in range(i+1, len(inputs)):
            if inputs[j] not in d:
                d[2020 - inputs[i] - inputs[j]] = True
            else:
                return inputs[i] * inputs[j] * (2020-inputs[i]-inputs[j])

assert find_product(inputs) == 514579
assert find_product2(inputs) == 241861950

with open("inputs/day01.txt") as f:
    print (find_product2([int(line.strip()) for line in f]))