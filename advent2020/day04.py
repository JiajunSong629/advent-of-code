from __future__ import annotations
from typing import Dict, List
import re

RAW = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

Passport = Dict[str, str]

def make_passport(raw: str) -> Passport:
    lines = raw.strip().split("\n")
    lines = [line.strip() for line in lines if line.strip()]

    passport = {}
    for line in lines:
        for chunk in line.split(" "):
            key, value = chunk.split(":")
            passport[key] = value
        
    return passport

def make_passports(raws: str) -> List[Passport]:
    raws = raws.split("\n\n")
    return [make_passport(raw) for raw in raws]

DEFAULT_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

def is_valid(passport: Passport, require_fields: List[str] = DEFAULT_FIELDS)-> bool:
    return all(field in passport for field in require_fields)

def is_valid_height(hgt: str) -> bool:
    if hgt.endswith("cm"):
        hgt = hgt.replace("cm", "")
        return 150 <= int(hgt) <= 193
    elif hgt.endswith("in"):
        hgt = hgt.replace("in", "")
        return 59 <= int(hgt) <= 76
    return False

def is_valid2(passport: Passport) -> bool:
    checks = [
        1902 <= int(passport.get('byr', -1)) <= 2002,
        2010 <= int(passport.get('iyr', -1)) <= 2020,
        2020 <= int(passport.get('eyr', -1)) <= 2030,
        is_valid_height(passport.get('hgt', "")),
        re.match(r"^#[0-9a-f]{6}$", passport.get('hcl', "")),
        passport.get('ecl', "") in ['amb','blu','brn','gry','grn','hzl','oth'],
        re.match(r"^[0-9]{9}$", passport.get('pid', "")),
    ]

    return all(checks)



passports = make_passports(RAW)
print ([is_valid(passport) for passport in passports])
print ([is_valid2(passport) for passport in passports])

with open("inputs/day04.txt") as f:
    raw = f.read()
    passports = make_passports(raw)
    print (sum(is_valid(passport) for passport in passports))
    print (sum(is_valid2(passport) for passport in passports))    