import typing as t

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

lines = open("/home/aurelien/AOC/2023/aoc10.txt").read().splitlines()

tiles = [list(line) for line in lines]

directions = {"DOWN": (1, 0), "RIGHT": (0, 1), "UP": (-1, 0), "LEFT": (0, -1)}

pipes = {
    "|": {"DOWN": "DOWN", "UP": "UP"},
    "-": {"RIGHT": "RIGHT", "LEFT": "LEFT"},
    "L": {"DOWN": "RIGHT", "LEFT": "UP"},
    "J": {"DOWN": "LEFT", "RIGHT": "UP"},
    "7": {"UP": "LEFT", "RIGHT": "DOWN"},
    "F": {"UP": "RIGHT", "LEFT": "DOWN"},
    "S": {},
    ".": {},
}


def get_start_coords(tiles: t.List[t.List[str]]) -> t.Tuple[int, int]:
    for i in range(len(tiles)):
        if "S" in tiles[i]:
            return i, tiles[i].index("S")


def out_of_bounds(x, y, array: t.List[t.List[t.Any]]):
    return x >= len(array) or x < 0 or y >= len(array[x]) or y < 0


def invert(way: str):
    if way == "RIGHT":
        return "LEFT"
    elif way == "LEFT":
        return "RIGHT"
    elif way == "UP":
        return "DOWN"
    elif way == "DOWN":
        return "UP"


def start_pipe(
    x: int, y: int, tiles: t.List[t.List[str]]
) -> t.Tuple[int, int, str, str]:
    for way, d in directions.items():
        i = x + d[0]
        j = y + d[1]
        if not out_of_bounds(i, j, tiles):
            pipe = pipes[tiles[i][j]]
            if invert(way) in pipe:
                return i, j, tiles[i][j], way
    print("LOL")


def first_star(tiles: t.List[t.List[str]]) -> int:
    x, y = get_start_coords(tiles)
    x, y, pipe, way = start_pipe(x, y, tiles)
    loop = [pipe]
    while pipe != "S":
        way = pipes[pipe][way]
        d_x, d_y = directions[way]
        x += d_x
        y += d_y
        pipe = tiles[x][y]
        loop.append(pipe)
    return len(loop) // 2


def second_star(tiles: t.List[t.List[str]]) -> int:
    x, y = get_start_coords(tiles)
    x, y, pipe, way = start_pipe(x, y, tiles)
    loop = {(x, y): pipe}
    while pipe != "S":
        way = pipes[pipe][way]
        d_x, d_y = directions[way]
        x += d_x
        y += d_y
        pipe = tiles[x][y]
        loop[(x, y)] = pipe
    polygon = Polygon(loop.keys())
    count = 0
    for i in range(len(tiles)):
        for j in range(len(tiles[i])):
            if (i, j) not in loop and polygon.contains(Point(i, j)):
                count += 1
    return count


print(first_star(tiles))
print(second_star(tiles))
