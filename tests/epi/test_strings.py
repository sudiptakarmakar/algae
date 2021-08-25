import pytest

from algae.epi import strings


@pytest.mark.parametrize(
    "integer, expected",
    [(1337, "1337"), (-1337, "-1337"), (0, "0"), (10, "10")],
)
def test_integer_to_string(integer, expected):
    assert strings.integer_to_string(integer) == expected


@pytest.mark.parametrize(
    "s, expected",
    [("1337", 1337), ("-1337", -1337), ("0", 0), ("10", 10)],
)
def test_string_to_integer(s, expected):
    assert strings.string_to_integer(s) == expected
