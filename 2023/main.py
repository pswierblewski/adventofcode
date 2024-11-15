import re

def replace_combined_digits(line: str) -> str:
    combined = {
        "oneight": "18",
        "twone": "21",
        "threeight": "38",
        "fiveight": "58",
        "sevenine": "79",
        "eightwo": "82",
        "eighthree": "83",
        "nineight": "98"
    }

    for key, value in combined.items():
        line = line.replace(key, value)
    return line

def replace_verbal_digits(line: str) -> str:
    verbal_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for key, value in verbal_digits.items():
        line = line.replace(key, value)
    return line

def replace_non_digits(line: str) -> str:
    return re.sub(r"[^0-9]", "", line)

def take_calibration_values(line: str) -> int:
    line = replace_combined_digits(line)
    line = replace_verbal_digits(line)
    line = replace_non_digits(line)
    first_digit = line[0]
    last_digit = line[-1]
    result = int(f'{first_digit}{last_digit}')
    return result


def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    sum = 0
    for line in lines:
        sum += take_calibration_values(line)
    print(sum)

if __name__ == "__main__":
    main()