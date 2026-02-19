from pattern_42 import is_pattern_42
from mazegennotperfect import convert_to_imperfect_maze


class Cell:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.up = self.down = self.left = self.right = True
        self.is_start = self.is_end = self.visited = False
        self.path_42 = False
        self.solution_path = False

class MazeGenerator:
    def __init__(self, config):
        # self.seed = config.seed
        self.config = config
        self.grid = [
            [Cell(x, y) for x in range(self.config.width)]
            for y in range(self.config.height)
        ]

    def generate(self, algorithm):
        sx, sy = self.config.entry
        self.grid[sy][sx].is_start = True

        ex, ey = self.config.exit
        self.grid[ey][ex].is_end = True

        if self.config.is_path_42:
            is_pattern_42(self.grid, self.config)
        else:
            print("maze is samll ")

        yield from algorithm.apply(self.grid, self.config)

        if not self.config.perfect:
            yield from convert_to_imperfect_maze(self.grid, self.config)

    def reset(self):
        """Restores the grid to its initial state (all walls up, no one visited)."""
        for row in self.grid:
            for cell in row:
                cell.visited = False
                cell.up = True
                cell.down = True
                cell.left = True
                cell.right = True
                cell.path_42 = False # Clear the old solution path
                cell.is_start = False
                cell.is_end = False
