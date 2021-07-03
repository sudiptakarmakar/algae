import pytest

from algae.leet.fb import m0089_gray_code


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, [0, 1, 3, 2]),
        (3, [0, 1, 3, 2, 6, 7, 5, 4]),
        (4, [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]),
    ],
)
def test_gray_code(n, expected):
    assert expected == m0089_gray_code.gray_code(n)


@pytest.mark.parametrize(
    "n",
    [3, 6, 20],
)
def test_gray_code_by_output(n):
    ans = m0089_gray_code.gray_code(n)
    assert all(f"{a^b:b}".count("1") == 1 for a, b in zip(ans, ans[1:] + ans[:1]))
