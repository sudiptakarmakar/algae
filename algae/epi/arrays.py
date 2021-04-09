import math
import random

from typing import List, Any


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
    pass


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
    pass


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
    length = len(elements)
    for i in range(size):
        index = random.randint(i, length)
        elements[i], elements[index] = elements[index], elements[i]


def sample_oinline_data():
    """Design a program that takes as input a size k, and reads packets,
    continuously maintaining a uniform random subset of size k of the read packets.
    """


def compute_random_permutation():
    pass


def compute_random_subset():
    pass


def generate_nonuniform_random_number():
    pass


def sudoku_checker():
    pass


def spiral_ordering_2d_array():
    pass


def rotate_2d_array():
    pass


def compute_rows_pascals_triangle():
    pass
