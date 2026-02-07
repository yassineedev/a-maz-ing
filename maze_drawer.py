from mazegen import MazeGenerator, Cell
import curses

maze = MazeGenerator.generate


class MazeDrawer:
    def __init__(self, maze, stdscr):
        self.maze = maze
        self.stdscr: curses.window = stdscr

    def draw(self, cell_size=2):
        self.stdscr.clear()
        height = len(self.maze.grid)
        width = len(self.maze.grid[0]) if height > 0 else 0
        curses.start_color()
        curses.use_default_colors()

        try:
            # Initialize colors
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

            for y, row in enumerate(self.maze.grid):
                for x, cell in enumerate(row):
                    cy = y * 2
                    cx = x * 3
                    cell: Cell

                    if cell.up:
                        self.stdscr.addstr(cy, cx, "███", 1)
                    else:
                        self.stdscr.addstr(cy, cx, "█  ", 1)

                    if y == self.maze.height - 1:
                        self.stdscr.addstr(cy + 2, cx, "████", 1)
                    if cell.right and x == self.maze.width - 1:
                        self.stdscr.addstr(cy, cx + 3, "█", 1)
                    if cell.left:
                        self.stdscr.addstr(cy + 1, cx, "█", 1)
                        if cell.is_start:
                            self.stdscr.addstr(cy + 1, cx + 1, "SS", 3)
                        if cell.is_end:
                            self.stdscr.addstr(cy + 1, cx + 1, "EE", 2)
                        if x == width - 1:
                            self.stdscr.addnstr(cy + 1, cx + 3, "█", 1)
                    else:
                        if x == width - 1:
                            self.stdscr.addstr(cy + 1, cx + 1, "  █", 1)
                        if x < width - 2 and not cell.right:
                            self.stdscr.addstr(cy + 1, cx, "    ", 1)
        except Exception:
            pass

        self.stdscr.refresh()

    # Solve prototype
    def solve(self) -> str:
        pass

    def show_path(self) -> None:
        pass

    def rotate_colors(self) -> None:
        pass
