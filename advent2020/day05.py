from typing import NamedTuple, List

INPUTS = [
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL"
]

class Seat(NamedTuple):
    row: int
    col: int

    @property
    def seat_id(self) -> int:
        return self.row * 8 + self.col

def make_seat(raw: str) -> Seat:
    row, col = 0, 0

    val = 1
    for c in reversed(raw[:7]):
        row += {'B': 1, 'F': 0}[c] * val
        val *= 2
    
    val = 1
    for c in reversed(raw[7:]):
        col += {'R': 1, 'L': 0}[c] * val
        val *= 2
    
    return Seat(row, col)

def find_your_seat(seat_id_list: List[int]) -> int:
    i = min(seat_id_list)
    while True:
        if i not in seat_id_list:
            return i
        i += 1

print ([make_seat(raw).seat_id for raw in INPUTS])

with open("inputs/day05.txt") as f:
    lines = f.read().strip().split("\n")
    print (find_your_seat([make_seat(raw).seat_id for raw in lines]))

