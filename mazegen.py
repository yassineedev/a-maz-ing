import random
from maze import Maze
# from mazegen_algorithm import MazeAlgorithm
from pattern_42 import is_pattern_42
from mazegennotperfect import convert_to_imperfect_maze

class Cell:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.up = self.down = self.left = self.right = True
        self.is_start = self.is_end = self.visited = False
        self.path_42 = False


    def __str__(self):
        return " " if not self.down else "_"


class MazeGenerator:
    from mazegen_algorithm import MazeAlgorithm
    def __init__(self, config):
        self.config = config

    def generate(self, algorithm: MazeAlgorithm):
        grid = [
            [Cell(x, y) for x in range(self.config.width)]
            for y in range(self.config.height)
        ]
        if self.config.width < 8 or self.config.height < 6:
            print("Error: Maze too small for the 42 pattern.")
        else:
             is_pattern_42(grid, self.config)

        sx, sy = self.config.entry
        grid[sy][sx].is_start = True

        algorithm.apply(grid, self.config)
        if not self.config.perfect:
            convert_to_imperfect_maze(grid, self.config)

        ex, ey = self.config.exit
        grid[ey][ex].is_end = True

        maze = Maze(self.config.width, self.config.height, grid)
        return maze