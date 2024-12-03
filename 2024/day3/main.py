from pathlib import Path
import re


def read_file() -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'input.txt'
    file = file_location.open()
    f = file.read()
    return f.split("\n")

def get_first_mul_expressions(lines: list[str]) -> list[str]:
    return [re.findall(r"mul\((\d+,\d+)\).*?do((n't)?)\(\)", line)[0][0] for line in lines]

def get_mul_expressions(lines: list[str]) -> list[str]:
    mul_expressions = []
    do_regex = re.compile(r"((do\(\))|(don't\(\)))")
    muls_regex = re.compile(r"mul\((\d+,\d+)\)")
    for line in lines:
        s = do_regex.split(line)
        beginning = s.pop(0)
        mul_expressions.extend(muls_regex.findall(beginning))
        for i in range(0, len(s), 4):
            if s[i] == "don't()":
                continue
            content = s[i+3]
            muls = muls_regex.findall(content)
            mul_expressions.extend(muls)
    return mul_expressions

def flat_list(mul_expressions: list[list[str]]) -> list[str]:
    return [num for sublist in mul_expressions for num in sublist]

def to_int_list(flat_mul_expressions: list[str]) -> list[int]:
    return [list(map(int, expression.split(","))) for expression in flat_mul_expressions]

def get_product(int_list: list[list[int]]) -> int:
    result = 0
    for a, b in int_list:
        result += a * b
    return result

def main():
    lines = read_file()
    combined_lines = ["".join(lines)]
    # mul_expressions = get_first_mul_expressions(lines)
    mul_expressions = get_mul_expressions(combined_lines)
    int_list = to_int_list(mul_expressions)
    sum = get_product(int_list)
    print(sum)

if __name__ == "__main__":
    main()