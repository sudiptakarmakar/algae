import math
import pytest

from unittest import mock

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


@pytest.mark.parametrize(
    "permutation, expected",
    [
        ([6, 2, 1, 5, 4, 3, 0], [6, 2, 3, 0, 1, 4, 5]),
        ([6, 2, 1, 5, 4, 3, 3, 3, 0], [6, 2, 3, 0, 1, 3, 3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 6, 5]),
        ([5, 4, 3, 2, 1, 0], []),
        ([5], []),
        ([5, 6], [6, 5]),
        ([9, 9, 9, 9], []),
    ],
)
def test_compute_next_permutation(permutation, expected):
    arrays.compute_next_permutation(permutation)
    assert permutation == expected


@pytest.mark.parametrize(
    "elements, size, random_indices, expected",
    [
        ([3, 7, 5, 11], 3, [1, 2, 3], [7, 5, 11, 3]),
        ([1, 2, 3, 4, 5, 6], 4, [5, 1, 3, 5], [6, 2, 4, 1, 5, 3]),
    ],
)
def test_sample_offline_data(elements, size, random_indices, expected):
    """This test kind of leaks implementation details here since we are relying
    on moderating the behavior and usage of the random module in the code. In
    reality, that library usage should be hidden behind the abstraction. However,
    I am not sure how to test the random expected output properly otherwise.
    """
    assert len(random_indices) >= size

    index = -1

    def randint(*args):
        nonlocal index
        index += 1
        return random_indices[index]

    with mock.patch(f"{arrays.__name__}.random.randint", randint):
        arrays.sample_offline_data(elements, size)
        assert elements == expected


@pytest.mark.parametrize(
    "elements, k, random_indices, expected",
    [
        ([3, 7, 5, 11], 3, [1], [3, 11, 5]),
        ([1, 2, 3, 4, 5, 6], 4, [5, 1], [1, 6, 3, 4]),
    ],
)
def test_sample_online_data(elements, k, random_indices, expected):
    """This test kind of leaks implementation details here since we are relying
    on moderating the behavior and usage of the random module in the code. In
    reality, that library usage should be hidden behind the abstraction. However,
    I am not sure how to test the random expected output properly otherwise.
    """
    assert len(random_indices) >= len(elements) - k

    index = -1

    def randint(*args):
        nonlocal index
        index += 1
        return random_indices[index]

    def sequence_generator():
        for i in elements:
            yield i

    sequence = sequence_generator()

    with mock.patch(f"{arrays.__name__}.random.randint", randint):
        assert arrays.sample_online_data(sequence, k) == expected


@pytest.mark.parametrize(
    "size, random_indices, expected",
    [
        (3, [1, 2, 2], [1, 2, 0]),
        (6, [2, 1, 5, 3, 5, 5], [2, 1, 5, 3, 0, 4]),
    ],
)
def test_compute_random_permutation(size, random_indices, expected):
    """This test kind of leaks implementation details here since we are relying
    on moderating the behavior and usage of the random module in the code. In
    reality, that library usage should be hidden behind the abstraction. However,
    I am not sure how to test the random expected output properly otherwise.
    """
    assert len(random_indices) >= size

    index = -1

    def randint(*args):
        nonlocal index
        index += 1
        return random_indices[index]

    with mock.patch(f"{arrays.__name__}.random.randint", randint):
        assert arrays.compute_random_permutation(size) == expected


@pytest.mark.parametrize(
    "numbers, probabilities, random_number, expected",
    [
        (
            [11, 7, 5, 2, 1, 8, 3, 9, 4, 10, 6],
            [
                0.16556963839877675,
                0.04730561097107907,
                0.03010357061795941,
                0.11037975893251784,
                0.03311392767975535,
                0.08278481919938838,
                0.04139240959969419,
                0.0662278553595107,
                0.3311392767975535,
                0.03679325297750594,
                0.05518987946625892,
            ],
            0.6778096183417303,
            4,
        ),
        (
            [4, 3, 1, 5, 6, 2],
            [
                0.1020408163265306,
                0.2040816326530612,
                0.06802721088435373,
                0.08163265306122448,
                0.4081632653061224,
                0.13605442176870747,
            ],
            0.21562658466805384,
            3,
        ),
        (
            [6, 10, 5, 3, 9, 7, 1, 2, 4, 8],
            [
                0.17070857607370274,
                0.042677144018425685,
                0.11380571738246849,
                0.04877387887820078,
                0.056902858691234244,
                0.03414171521474055,
                0.3414171521474055,
                0.0682834304294811,
                0.037935239127489494,
                0.08535428803685137,
            ],
            0.9104018862495027,
            4,
        ),
        (
            [8, 3, 2, 4, 1, 7, 9, 6, 5],
            [
                0.044185720297376906,
                0.35348576237901524,
                0.08837144059475381,
                0.17674288118950762,
                0.05891429372983587,
                0.03927619581989058,
                0.07069715247580305,
                0.11782858745967174,
                0.050497966054145034,
            ],
            0.25517286996144783,
            3,
        ),
    ],
)
def test_generate_nonuniform_random_number(numbers, probabilities, random_number, expected):
    """This test kind of leaks implementation details here since we are relying
    on moderating the behavior and usage of the random module in the code. In
    reality, that library usage should be hidden behind the abstraction. However,
    I am not sure how to test the random expected output properly otherwise.
    """
    assert len(numbers) == len(probabilities)
    assert math.isclose(sum(probabilities), 1.0, rel_tol=1e-5)

    with mock.patch(f"{arrays.__name__}.random.random", return_value=random_number):
        assert arrays.generate_nonuniform_random_number(numbers, probabilities) == expected


@pytest.mark.parametrize(
    "sudoku_rows, expected",
    [
        (
            [
                "530070000",
                "600195000",
                "098000060",
                "800060003",
                "400803001",
                "700020006",
                "060000280",
                "000419005",
                "000080079",
            ],
            True,
        ),
        (
            [
                "530070000",
                "600195000",
                "098050060",
                "800060003",
                "400803001",
                "700020006",
                "060000280",
                "000419005",
                "000080079",
            ],
            False,
        ),
    ],
)
def test_sudoku_checker(sudoku_rows, expected):
    assert len(sudoku_rows) == 9
    assert all(len(row) == 9 for row in sudoku_rows)
    sudoku = [[int(i) for i in row] for row in sudoku_rows]
    assert arrays.sudoku_checker(sudoku) == expected


@pytest.mark.parametrize(
    "matrix, expected",
    [
        (
            [[1]],
            [1],
        ),
        (
            [[1, 2], [3, 4]],
            [1, 2, 4, 3],
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
        ),
    ],
)
def test_spiral_ordering_2d_array(matrix, expected):
    assert len(matrix) == len(matrix[0])
    assert arrays.spiral_ordering_2d_array(matrix) == expected


@pytest.mark.parametrize(
    "matrix, expected",
    [
        (
            [[1]],
            [[1]],
        ),
        (
            [[1, 2], [3, 4]],
            [[3, 1], [4, 2]],
        ),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
        (
            [
                [1, 2, 3, 4, 5, 6, 7, 8],
                [9, 10, 11, 12, 13, 14, 15, 16],
                [17, 18, 19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30, 31, 32],
                [33, 34, 35, 36, 37, 38, 39, 40],
                [41, 42, 43, 44, 45, 46, 47, 48],
                [49, 50, 51, 52, 53, 54, 55, 56],
                [57, 58, 59, 60, 61, 62, 63, 64],
            ],
            [
                [57, 49, 41, 33, 25, 17, 9, 1],
                [58, 50, 42, 34, 26, 18, 10, 2],
                [59, 51, 43, 35, 27, 19, 11, 3],
                [60, 52, 44, 36, 28, 20, 12, 4],
                [61, 53, 45, 37, 29, 21, 13, 5],
                [62, 54, 46, 38, 30, 22, 14, 6],
                [63, 55, 47, 39, 31, 23, 15, 7],
                [64, 56, 48, 40, 32, 24, 16, 8],
            ],
        ),
    ],
)
def test_rotate_2d_array(matrix, expected):
    assert len(matrix) == len(matrix[0])
    arrays.rotate_2d_array(matrix)
    assert matrix == expected
