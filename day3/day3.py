import re
import os

input_file = "input.txt"

def main_day_3_answer():
    regex_1 = r'mul\(\d{1,3}\,\d{1,3}\)'
    regex_2 = r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)"

    part_1 = calculate_total_mul(find_regex_matches_from_file(regex_1, input_file))
    part_2 = calculate_total_enabled_mul(find_regex_matches_from_file(regex_2, input_file))
    
    print(f"Part 1: {part_1}\nPart 2: {part_2}")

def find_regex_matches_from_file(regex, file_name):
    all_valid = []

    with open(file_name) as file:
        for line in file:
            all_valid.extend(re.findall(regex, line))

    return all_valid

def calculate_total_mul(match_list):
    total = 0

    for match in match_list:
        total += get_mul_value(match)

    return total

def calculate_total_enabled_mul(match_list):
    total = 0
    do = True

    for match in match_list:
        if match == "do()":
            do = True
        if match == "don't()":
            do = False
        if match.startswith("mul") and do:
            total += get_mul_value(match)

    return total

def get_mul_value(mul_string):
    item = mul_string.strip("mul()").split(",")
    return int(item[0]) * int(item[1])


if __name__ == "__main__":
    main_day_3_answer()
