"""
Given a grid of R x C cells, each cell marked '#' as blocked, a starting point
coordinate 'S' and a finishing point coordinate 'F', return the minimum distance
between them.

S . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . F . . .
"""
import collections


def solve(m, start, finish):
    rows = len(m)
    cols = len(m[0])
    visited = set()

    def get_neighbors(r, c):
        for r_delta, c_delta in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            r_new, c_new = r + r_delta, c + c_delta
            if (
                0 <= r_new < rows
                and 0 <= c_new < cols
                and (r_new, c_new) not in visited
                and m[r_new][c_new] != "#"
            ):
                yield r_new, c_new

    pipe = collections.deque()
    pipe.append((start, 0))
    visited.add(start)

    while pipe:
        cell, distance = pipe.popleft()
        if cell == finish:
            return distance
        for neighbor in get_neighbors(*cell):
            pipe.append((neighbor, distance + 1))
            visited.add(neighbor)

    return -1


"""
youtube-dl --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" https://www.youtube.com/playlist?list=OLAK5uy_nRAj82ywkJ_YHiRh-sXKAbpiCiUfSx0-k

youtube-dl --extract-audio --audio-format mp3 -o "%(autonumber)02d-%(title)s.%(ext)s" --autonumber-start 1
https://www.youtube.com/playlist?list=OLAK5uy_nRAj82ywkJ_YHiRh-sXKAbpiCiUfSx0-k
"""
