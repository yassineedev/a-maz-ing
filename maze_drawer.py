from mazegen import MazeGenerator
import time

maze = MazeGenerator.generate


class MazeDrawer:
    def __init__(self, maze, stdscr):
        self.maze = maze
        self.stdscr = stdscr

    def draw(self, cell_size=2):
        self.stdscr.clear()
        height, width = self.stdscr.getmaxyx()
        cell_size = 3
        yy, x_ = 20, 30
        chars = x_ * cell_size + 1
        self.stdscr.addstr(0, 0, "█" * chars)
        for y in range(height):
            line = "█"
            
        self.stdscr.refresh()

    # Solve prototype
    def solve(self) -> str:
        pass

    def show_path(self) -> None:
        pass

    def rotate_colors(self) -> None:
        pass
