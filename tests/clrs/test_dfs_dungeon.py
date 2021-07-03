import pytest
from algae.clrs.dfs import dungeon


def init_matrix():
    m_str = """
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . # # . . .
. . . . . # . . . .
. . . . . . . . . .
"""
    return [line.strip().split() for line in m_str.split("\n") if line.strip()]


base_dungeon = init_matrix()


@pytest.mark.parametrize(
    "matrix, start, finish, expected",
    [
        (base_dungeon, (0, 0), (2, 3), 5),
        (base_dungeon, (0, 0), (5, 9), 14),
        (base_dungeon, (5, 9), (0, 0), 14),
        (base_dungeon, (0, 0), (0, 0), 0),
        (base_dungeon, (0, 0), (1, 1), 2),
        (base_dungeon, (0, 0), (-1, -1), -1),
        (base_dungeon, (0, 0), (10, 45), -1),
        (base_dungeon, (0, 0), (4, 6), 12),
        (base_dungeon, (4, 6), (0, 0), 12),
    ],
)
def test_dungeon_solve(matrix, start, finish, expected):
    assert (
        dungeon.solve(matrix, start, finish) == expected
    ), f"Cannot reach from {start} to {finish} in {expected} steps"
