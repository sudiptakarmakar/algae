import bisect
import itertools
import math
import random

from typing import List, Any, Generator


def dutch_national_flag(numbers: List[int], index: int):
    """Write a program that takes an array A and an index i into A, and
    rearranges the elements such that all elements less than A[i] (the "pivot")
    appear first, followed by elements equal to the pivot, followed by elements
    greater than the pivot."""
    pivot = numbers[index]
    less, equal, more = 0, 0, len(numbers)
    while equal < more:
        if numbers[equal] < pivot:
            numbers[less], numbers[equal] = numbers[equal], numbers[less]
            less += 1
            equal += 1
        elif numbers[equal] > pivot:
            more -= 1
            numbers[more], numbers[equal] = numbers[equal], numbers[more]
        else:
            equal += 1


def increment_arbitrary_precision_int(digits: List[int]):
    """Write a program which takes as input an array of digits encoding a
    decimal number D and updates the array to represent the number D + 1.
    For example, if the input is (1,2,9) then you should update the array to
    (1,3,0). Your algorithm should work even if it is implemented in a language
    that has finite-precision arithmetic.
    """
    index = len(digits) - 1
    carry = 1
    while carry > 0 and index >= 0:
        total = digits[index] + carry
        digits[index] = total % 10
        carry = total // 10
        index -= 1
    if carry:
        digits.insert(0, carry)


def multiply_arbitrary_precision_int(one: List[int], two: List[int]):
    """Write a program that takes two arrays representing integers, and returns
    an integer representing their product.
    For example, since 193707721 X -761838257287 = -147573952589676412927, if
    the inputs are [1,9,3,7,0,7,7,2,1] and <-7,6,1,8,3,8,2,5,7,2,8,7>, your
    function should return (-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7).
    """


def advance_through_array(steps: List[int]):
    """Write a program which takes an array of n integers, where A[i] denotes
    the maximum you can advance from index i, and returns whether it is possible
    to advance to the last index starting from the beginning of the array.
    """
    max_reach = 0
    for position, reach in enumerate(steps):
        if position > max_reach:
            return False
        max_reach = max(max_reach, position + reach)
    return max_reach >= len(steps)


def delete_duplicates_from_sorted_array(numbers: List[int]):
    """Write a program which takes as input a sorted array and updates it so
    that all duplicates have been removed and the remaining elements have been
    shifted left to fill the emptied indices. Return the number of valid
    elements. Many languages have library functions for performing this
    operation - you cannot use these functions.
    """
    uniq = 0
    current = 0
    while current < len(numbers):
        if numbers[current] > numbers[uniq]:
            uniq += 1
            numbers[uniq] = numbers[current]
        current += 1
    return uniq + 1


def buy_sell_stock_once(prices: List[int]):
    """Write a program that takes an array denoting the daily stock price, and
    returns the maximum profit that could be made by buying and then selling
    one share of that stock.
    """
    min_price = math.inf
    max_profit = -math.inf
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


def buy_sell_stock_twice(prices):
    """Write a program that computes the maximum profit that can be made by
    buying and selling a share at most twice. The second buy must be made on
    another date after the first sale.
    """


def enumerate_primes(limit: int):
    """Write a program that takes an integer argument and returns all the primes
    between 1 and that integer inclusive.
    For example, if the input is 18, you should return (2,3,5,7,11,13,17).
    """
    if limit < 2:
        return []
    size = 1 + (limit - 3) // 2  # odd numbers starting from 3
    primes = [2]
    is_prime = [True] * size  # is_prime[i] represents whether (2i + 3) is prime
    for i in range(size):
        if is_prime[i]:
            prime = (i * 2) + 3
            primes.append(prime)
            # Sieving prime starting from prime**2 because all the multiples of
            # prime less than prime should have already been sieved those lesser
            # multiples. The index of this value in is_prime is
            # (prime * prime - 3) // 2 because is_prime[i] represents 2i + 3
            prime_index_start = (prime * prime - 3) // 2
            for prime_index in range(prime_index_start, size, prime):
                is_prime[prime_index] = False
    return primes


def permute_array_elements(elements: List[Any], permutation: List[int]):
    """Given an array A of n elements and a permutation P, apply P to A.

    For example, the array (2,0,1,3) represents the permutation that maps the
    element at location 0 to location 2, the element at location 1 to location
    0, the element at location 2 to location 1, and keep the element at location
    3 unchanged. A permutation can be applied to an array to reorder the array.

    For example, the permutation (2,0,1,3) applied to A = (a,b,c,d) yields the
    array (b,c,a,d).
    """
    result = [None] * len(elements)
    for i, n in enumerate(permutation):
        result[n] = elements[i]
    return result


def compute_next_permutation(permutation: List[int]):
    """Write a program that takes as input a permutation, and returns the next
    permutation under dictionary ordering. If the permutation is the last
    permutation, return the empty array.
    For example, if the input is (1, 0, 3, 2) your function should return
    (1, 2, 0, 3). If the input is (3, 2, 1, 0), return ()
    """
    # find inflexion point
    prev = permutation[-1]
    index = len(permutation) - 2
    while index >= 0:
        current = permutation[index]
        if current < prev:
            break
        prev = current
        index -= 1
    if index < 0:
        permutation.clear()
        return

    # index is right before the last non increasing suffix, swap it with the
    # smallest number larger than it to its right
    small_index = index
    while index < len(permutation) and permutation[index] >= permutation[small_index]:
        index += 1
    permutation[small_index], permutation[index - 1] = (
        permutation[index - 1],
        permutation[small_index],
    )

    # reverse the rightmost sorted subsection to order it ascending
    left = small_index + 1
    right = len(permutation) - 1
    while left < right:
        permutation[left], permutation[right] = permutation[right], permutation[left]
        left += 1
        right -= 1


def sample_offline_data(elements: List[int], size: int):
    """Implement an algorithm that takes as input an array of distinct elements
    and a size, and returns a subset of the given size of the array elements.
    All subsets should be equally likely. Return the result in input array itself.
    """
    for i in range(size):
        index = random.randint(i, len(elements) - 1)
        elements[i], elements[index] = elements[index], elements[i]


def sample_online_data(sequence: Generator, k: int):
    """Design a program that takes as input a size k, and reads packets from a
    sequence generator, continuously maintaining a uniform random subset of size
    k of the read packets.
    """
    sample_k = [next(sequence) for _ in range(k)]
    count = k

    for element in sequence:
        index = random.randint(0, count)
        if index < k:
            sample_k[index] = element
        count += 1

    return sample_k


def compute_random_permutation(size: int):
    """Design an algorithm that creates uniformly random permutations of
    (0, 1,..., n-1). You are given a random number generator that returns
    integers in the set (0, 1,..., n-1) with equal probability; use as few calls
    to it as possible.
    """
    elements = list(range(size))
    for i in range(size):
        index = random.randint(i, size - 1)  # randint is inclusive of range
        elements[i], elements[index] = elements[index], elements[i]
    return elements


def compute_random_subset(n: int):
    """Write a program that takes as input a positive integer n and a size
    k < n, and returns a size-k subset of {0,1, 2,..., n - 1}. The subset should
    be represented as an array. All subsets should be equally likely and, in
    addition, all permutations of elements of the array should be equally
    likely. You may assume you have a function which takes as input a non-negative
    integer t and returns an integer in the set {0, 1, . . . , t - 1} with uniform
    probability.
    """


def generate_nonuniform_random_number(numbers: List[int], probabilities: List[float]) -> int:
    """You are given n numbers and corresponding probabilities P0, P1,..., Pn-1
    - which sum up to 1. Given a random number generator that produces values in
    [0,1] uniformly, how would you generate one of the n numbers according to
    the specified probabilities?
    For example, if the numbers are 3, 5, 7, 11, and the probabilities are 9/18,
    6/18, 2/18, 1/18, then in 1000000 calls to your program, 3 should appear
    roughly 500000 times, 5 should appear roughly 333333 times, 7 should appear
    roughly 111111 times, and 11 should appear roughly 55555 times.
    """
    prefix_sum = list(itertools.accumulate(probabilities))
    weighted_index = bisect.bisect(prefix_sum, random.random())
    return numbers[weighted_index]


def sudoku_checker(sudoku: List[List[int]]) -> bool:
    """Check whether a 9 X 9 2D array representing a partially completed Sudoku
    is valid. Specifically, check that no row, column, or 3 X 3 2D subarray
    contains duplicates. A 0-value in the 2D array indicates that entry is blank;
    every other entry is in [1,9].
    """
    blk_size = int(math.sqrt(len(sudoku)))

    # counter = collections.Counter(
    #     k
    #     for r, row in enumerate(sudoku)
    #     for c, el in enumerate(row)
    #     if el != 0
    #     for k in (("r", r, el), ("c", c, el), ("b", r // blk_size, c // blk_size, el))
    # )

    # counter = collections.Counter()
    # for row, row_values in enumerate(sudoku):
    #     for col, value in enumerate(row_values):
    #         if value == 0:
    #             continue
    #         counter[(f"row-{row}", value)] += 1
    #         counter[(f"col-{col}", value)] += 1
    #         counter[(f"block-{row//blk_size}-{col//blk_size}", value)] += 1

    # return max(counter.values(), default=0) <= 1

    memo = set()
    for row, row_values in enumerate(sudoku):
        for col, value in enumerate(row_values):
            if value == 0:
                continue
            r = (f"row-{row}", value)
            c = (f"col-{col}", value)
            b = (f"block-{row//blk_size}-{col//blk_size}", value)
            if r in memo or c in memo or b in memo:
                return False
            memo.update([r, c, b])
    return True


def spiral_ordering_2d_array(matrix: List[List[int]]) -> List[int]:
    """Write a program which takes an nxn 2D array and returns the spiral
    ordering of the array.
    """
    result = []
    row = 0
    col = 0
    width = len(matrix) - 1
    while width > 0:
        for row_step, col_step in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            for _ in range(width):
                result.append(matrix[row][col])
                row += row_step
                col += col_step
        row += 1
        col += 1
        width -= 2
    if width == 0:
        result.append(matrix[row][col])
    return result


def rotate_2d_array(matrix: List[List[int]]):
    """Write a function that takes as input an n X n 2D array, and rotates the
    array by 90 degrees clockwise.
    """
    # row = 0
    # col = 0
    # width = len(matrix) - 1
    # max_width = width

    # while width > 0:
    #     memo = matrix[row][col : col + width]
    #     for row_step, col_step in ((0, 1), (1, 0), (0, -1), (-1, 0)):
    #         for idx in range(width):
    #             dest_row = col
    #             dest_col = max_width - row
    #             matrix[dest_row][dest_col], memo[idx] = memo[idx], matrix[dest_row][dest_col]
    #             row += row_step
    #             col += col_step
    #     row += 1
    #     col += 1
    #     width -= 2

    width = len(matrix) - 1
    for i in range(len(matrix) // 2):
        for j in range(i, width - i):
            matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = (
                matrix[~j][i],
                matrix[~i][~j],
                matrix[j][~i],
                matrix[i][j],
            )


def compute_rows_pascals_triangle(n: int):
    """Write a program which takes as input a nonnegative integer n and returns
    the first n rows of Pascal's triangle.
    """
