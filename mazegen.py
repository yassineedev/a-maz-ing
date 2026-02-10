import random
from maze import Maze
from pattern_42 import is_pattern_42

class Cell:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.up = self.down = self.left = self.right = True
        self.is_start = self.is_end = self.visited = False
        self.path_42 = False

class MazeGenerator:
    def __init__(self, config):
        self.config = config
        self.grid = [
            [Cell(x, y) for x in range(self.config.width)]
            for y in range(self.config.height)
        ]

    def generate(self, algorithm):
        if not self.config.width < 8 or self.config.height < 6:
            is_pattern_42(self.grid, self.config)
        
        sx, sy = self.config.entry
        self.grid[sy][sx].is_start = True

        yield from algorithm.apply(self.grid, self.config)

        if not self.config.perfect:
            from mazegennotperfect import convert_to_imperfect_maze
            yield from convert_to_imperfect_maze(self.grid, self.config)

        ex, ey = self.config.exit
        self.grid[ex][ey].is_end = True
    def prepare_maze(self) -> None:
        self.grid = [
            [Cell(x, y) for x in range(self.config.width)]
            for y in range(self.config.height)
        ]
        for row in self.grid:
            for cell in row:
                cell.up = True
                cell.down = True
                cell.left = True
                cell.right = True
                cell.visited = False
                cell.is_start = False
                cell.is_end = False
                cell.path_42 = False

        sx, sy = self.config.entry
        self.grid[sy][sx].is_start = True

        ex, ey = self.config.exit
        self.grid[ey][ex].is_end = True

    def generate_closed_maze(self):
        self.prepare_maze()
        return Maze(self.config.width, self.config.height, self.grid)