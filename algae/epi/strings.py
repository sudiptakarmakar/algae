def integer_to_string(n: int) -> str:
    """Implement string/integer inter-conversion functions"""
    negative = True if n < 0 else False
    if negative:
        n = -n
    result = []
    zero_ascii = ord("0")
    while True:
        result.append(chr(zero_ascii + n % 10))
        n = n // 10
        if n == 0:
            break
    if negative:
        result.append("-")
    return "".join(reversed(result))


def string_to_integer(s: str) -> int:
    """Implement string/integer inter-conversion functions."""
    negative = True if s.startswith("-") else False
    index = 1 if negative else 0
    result = 0
    zero_ascii = ord("0")
    for ch in s[index:]:
        result = 10 * result + ord(ch) - zero_ascii
    return -result if negative else result


def convert_base(s: str, b1: int, b2: int) -> str:
    """Write a program that performs base conversion. The input is a string, an
    integer b1,and another integer b2. The string represents is an integer in
    base b1. The output should be the string representing the integer in base b2.
    Assume 16 >= b1,b2 >= 2.
    """

    def integer_to_other_base(n: int, base: int) -> str:
        pass
