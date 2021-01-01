from typing import NamedTuple

PASSWORDS = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]

class Password(NamedTuple):
    lo: int
    hi: int
    char: str
    password: str

    def is_valid(self):
        return self.lo <= self.password.count(self.char) <= self.hi
    
    def is_valid2(self):
        return (self.password[self.lo - 1] == self.char) != (self.password[self.hi - 1] == self.char)

    @staticmethod
    def parse(line):
        limits, char, password = line.strip().split(" ")
        lo, hi = limits.split("-")
        char = char[0]
        return Password(int(lo), int(hi), char, password)
    

print ([Password.parse(pw).is_valid2() for pw in PASSWORDS])

with open("inputs/day02.txt") as f:
    print (sum(Password.parse(line).is_valid2() for line in f))
