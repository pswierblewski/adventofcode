from pathlib import Path
import re


def read_file() -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'input.txt'
    file = file_location.open()
    f = file.read()
    return f.split("\n")

def all_increasing(line: list[int]) -> bool:
    return all(line[i] < line[i + 1] for i in range(len(line) - 1))

def all_decreasing(line: list[int]) -> bool:
    return all(line[i] > line[i + 1] for i in range(len(line) - 1))

def valid_difference(line: list[int]) -> bool:
    minimum = 1
    maximum = 3
    return all(minimum <= abs(line[i] - line[i + 1]) <= maximum for i in range(len(line) - 1))

def validate_safe(line: list[int]) -> bool:
    return (all_increasing(line) or all_decreasing(line)) and valid_difference(line)

def is_safe(line: str) -> bool:
    line_split = re.sub(r"\s+", ";", line).split(";")
    line_int = [int(item) for item in line_split]
    is_safe = validate_safe(line_int)
    if is_safe:
        return True
    
    for i in range(len(line_int)):
        line_int_copy = line_int.copy()
        line_int_copy.pop(i)
        if validate_safe(line_int_copy):
            return True
    
    return False

def to_is_safe_list(lines: list[str]) -> list[bool]:
    return [is_safe(line) for line in lines]

def main():
    lines = read_file()
    is_safe_list = to_is_safe_list(lines)
    safe_count = is_safe_list.count(True)
    print(safe_count)

if __name__ == "__main__":
    main()