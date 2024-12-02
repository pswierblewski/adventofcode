from pathlib import Path
import re

def split_into_lists(input: list[str]) -> tuple[list[int], list[int]]:
    result: tuple[list[int], list[int]] = ([], [])
    for line in input:
        line_split = re.sub(r"\s+", ";", line).split(";")
        result[0].append(int(line_split[0]))
        result[1].append(int(line_split[1]))
    return result

def sort_lists(left: list[int], right: list[int]) -> tuple[list[int], list[int]]:
    return (sorted(left), sorted(right))

def calculate_distance(left: list[int], right: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))

def count_element_in_list(left: list[int], right: list[int]) -> int:
    simalirity_score = 0
    for item in left:
        simalirity_score += item * right.count(item)
    return simalirity_score

def main():
    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'input.txt'
    file = file_location.open()
    f = file.read()
    lines = f.split("\n")
    left, right = split_into_lists(lines)
    left, right = sort_lists(left, right)
    distance = calculate_distance(left, right)
    count = count_element_in_list(left, right)
    print(distance)
    print(count)

if __name__ == "__main__":
    main()