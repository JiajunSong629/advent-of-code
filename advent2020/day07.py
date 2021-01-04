from typing import NamedTuple, Dict, List
from collections import defaultdict
import re

RAW = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

RAW2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


class Bag(NamedTuple):
    color: str
    contains: Dict[str, int]

BagMap= Dict[str, Dict[str, int]]

def parse_line(line: str) -> Bag:
    part1, part2 = line.split(" contain ")
    color = re.sub(r"bags", "", part1).strip()
    if part2 == "no other bags.":
        return Bag(color, {})
    
    contains = {}
    for subbag in part2.rstrip(".").split(", "):
        first_space = subbag.find(" ")
        subcount = int(subbag[:first_space])
        subcolor = re.sub(r"bags?", " ", subbag[first_space:]).strip()
        contains[subcolor] = subcount
    
    return Bag(color, contains)

def make_bags(raw: str) -> List[Bag]:
    return [parse_line(line) for line in raw.split("\n")]

def make_child_map(bags: List[Bag]) -> BagMap:
    child_map = defaultdict(defaultdict)
    for bag in bags:
        child_map[bag.color] = bag.contains
    return child_map

def make_parent_map(bags: List[Bag]) -> BagMap:
    parent_map = defaultdict(defaultdict)
    for bag in bags:
        for child_color, child_count in bag.contains.items():
            parent_map[child_color][bag.color] = child_count
    return parent_map

def can_contain(bags: List[Bag], color: str) -> List[str]:
    stack = [color]
    parent_map = make_parent_map(bags)
    can_contain_bags = set()

    while stack:
        child = stack.pop()
        for parent in parent_map.get(child, {}):
            stack.append(parent)
            can_contain_bags.add(parent)
    
    return list(can_contain_bags)

def contain_num_bags(bags: List[Bag], color: str) -> int:
    child_map = make_child_map(bags)
    if len(child_map.get(color, [])) == 0:
        return 0
    
    num_bags = 0
    for child_color, child_count in child_map[color].items():
        num_bags += child_count * (1 + contain_num_bags(bags, child_color))
    
    return num_bags


bags = make_bags(RAW)
bags2 = make_bags(RAW2)

assert len(can_contain(bags, 'shiny gold')) == 4
assert contain_num_bags(bags, 'shiny gold') == 32
assert contain_num_bags(bags2, 'shiny gold') == 126

with open("inputs/day07.txt") as f:
    raw = f.read()
    bags = make_bags(raw)
    print (len(can_contain(bags, 'shiny gold')))
    print (contain_num_bags(bags, 'shiny gold'))
