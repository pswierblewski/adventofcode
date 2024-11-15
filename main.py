import re

def take_calibration_values(line: str) -> int:
    digits = re.sub(r"[^0-9]", "", line)
    first_digit = digits[0]
    last_digit = digits[-1]
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