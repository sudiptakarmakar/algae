import string
import pytest

from algae.epi import arrays


@pytest.mark.parametrize(
    "numbers, index",
    [
        ([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], 1),
        ([0, 0, 2, 0, 2, 2, 1, 2, 1, 1, 1, 0], 6),
        ([0, 0, 2, 0, 2, 2, 1, 2, 1, 1, 1, 0], 4),
        ([2, 1, 2, 0, 2, 0, 0, 1, 1, 2, 0, 1], 6),
        ([5, 4, 0, 3, 2, 9, 1, 8, 7, 6], 3),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 10),
    ],
)
def test_dutch_national_flag(numbers, index):
    pivot = numbers[index]
    arrays.dutch_national_flag(numbers, index)
    l_index = numbers.index(pivot)
    r_index = len(numbers) - numbers[::-1].index(pivot)
    assert all([n < pivot for n in numbers[:l_index]])
    assert all([n == pivot for n in numbers[l_index:r_index]])
    assert all([n > pivot for n in numbers[r_index:]])


@pytest.mark.parametrize(
    "digits, expected",
    [
        ([], [1]),
        ([0], [1]),
        ([1, 2, 3], [1, 2, 4]),
        ([1, 2, 9], [1, 3, 0]),
        ([9, 9, 9, 9], [1, 0, 0, 0, 0]),
    ],
)
def test_increment_arbitrary_precision_int(digits, expected):
    arrays.increment_arbitrary_precision_int(digits)
    assert digits == expected


@pytest.mark.parametrize(
    "steps, expected",
    [
        ([3, 3, 1, 0, 2, 0, 1], True),
        ([3, 2, 0, 0, 2, 0, 1], False),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1], True),
        ([6, 5, 4, 3, 2, 1, 0], False),
    ],
)
def test_advance_through_array(steps, expected):
    assert arrays.advance_through_array(steps) is expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([2, 3, 5, 5, 7, 11, 11, 11, 13], 6),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 10),
    ],
)
def test_delete_duplicates_from_sorted_array(numbers, expected):
    assert arrays.delete_duplicates_from_sorted_array(numbers) == expected


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([310, 315, 275, 295, 260, 270, 290, 230, 255, 250], 30),
    ],
)
def test_buy_sell_stock_once(prices, expected):
    assert arrays.buy_sell_stock_once(prices) == expected


# @pytest.mark.parametrize(
#     "prices, expected",
#     [
#         ([12, 11, 13, 9, 12, 8, 14, 13, 15], 10),
#     ],
# )
# def test_buy_sell_stock_twice(prices, expected):
#     assert arrays.buy_sell_stock_twice(prices) == expected


@pytest.mark.parametrize(
    "limit, expected",
    [
        (17, [2, 3, 5, 7, 11, 13, 17]),
        (1, []),
        (2, [2]),
        (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
    ],
)
def test_enumerate_primes(limit, expected):
    assert arrays.enumerate_primes(limit) == expected


@pytest.mark.parametrize(
    "elements, permutation, expected",
    [
        (["a", "b", "c", "d"], [2, 0, 1, 3], ["b", "c", "a", "d"]),
        (
            [
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g",
                "h",
                "i",
                "j",
                "k",
                "l",
                "m",
                "n",
                "o",
                "p",
                "q",
                "r",
                "s",
                "t",
                "u",
                "v",
                "w",
                "x",
                "y",
                "z",
            ],
            [
                18,
                21,
                15,
                9,
                3,
                8,
                13,
                2,
                14,
                4,
                11,
                1,
                24,
                20,
                25,
                17,
                16,
                7,
                5,
                22,
                12,
                23,
                0,
                10,
                6,
                19,
            ],
            [
                "w",
                "l",
                "h",
                "e",
                "j",
                "s",
                "y",
                "r",
                "f",
                "d",
                "x",
                "k",
                "u",
                "g",
                "i",
                "c",
                "q",
                "p",
                "a",
                "z",
                "n",
                "b",
                "t",
                "v",
                "m",
                "o",
            ],
        ),
    ],
)
def test_permute_array_elements(elements, permutation, expected):
    assert arrays.permute_array_elements(elements, permutation) == expected
