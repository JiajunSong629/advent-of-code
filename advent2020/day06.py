from collections import Counter

RAW = """abc

a
b
c

ab
ac

a
a
a
a

b"""

def count_yeses(raw: str) -> int:
    groups = raw.split("\n\n")
    num_yeses = 0
    for group in groups:
        num_yeses += len({c for person in group.split("\n") for c in person})
    return num_yeses

def count_yeses2(raw: str) -> int:
    groups = raw.split("\n\n")
    num_yeses = 0
    for group in groups:
        persons = group.split("\n")
        counter = Counter([c for person in persons for c in person])
        num_yeses += len([c for c, count in counter.items() if count == len(persons)])
    return num_yeses

assert count_yeses(RAW) == 3 + 3 + 3 + 1 + 1
assert count_yeses2(RAW) == 3 + 0 + 1 + 1 + 1


with open("inputs/day06.txt") as f:
    raw = f.read()
    print (count_yeses(raw))
    print (count_yeses2(raw))