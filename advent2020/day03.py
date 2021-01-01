from __future__ import annotations
from typing import NamedTuple, List

RAW = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

class Point(NamedTuple):
    x: int
    y: int

class Slope(NamedTuple):
    right: int = 3
    down: int = 1

class Grid(NamedTuple):
    trees: List[Point]
    height: int
    width: int

    @staticmethod
    def parse(raw: str) -> Grid:
        lines = raw.strip().split("\n")
        height = len(lines)
        width = len(lines[0])

        trees = [
            Point(x, y)
            for y, row in enumerate(lines)
            for x, char in enumerate(row)
            if char == "#"
        ]

        return Grid(trees, height, width)


def count_trees(grid: Grid, slope: Slope) -> int:
    res = 0
    x = 0
    for y in range(0, grid.height, slope.down):
        res += Point(x, y) in grid.trees
        x = (x + slope.right) % grid.width
    return res

def tree_product(grid: Grid, slopes: List[Slope]) -> int:
    res = 1
    for slope in slopes:
        res *= count_trees(grid, slope)
    return res

slopes = [
    Slope(right = 1, down = 1),
    Slope(right = 3, down = 1),
    Slope(right = 5, down = 1),
    Slope(right = 7, down = 1),
    Slope(right = 1, down = 2)
]

grid = Grid.parse(RAW)
slope = Slope()
assert count_trees(grid, slope) == 7
assert tree_product(grid, slopes) == 336

with open("inputs/day03.txt") as f:
    raw = f.read()
    grid = Grid.parse(raw)
    print (count_trees(grid, slope))
    print (tree_product(grid, slopes))