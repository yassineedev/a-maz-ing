from mazegen import Cell
import curses


class MazeDrawer:
    def __init__(self, maze, stdscr):
        self.maze = maze
        self.stdscr: curses.window = stdscr        

    def draw(self):
        self.stdscr.clear()
        height = len(self.maze.grid)
        width = len(self.maze.grid[0]) if height > 0 else 0
        curses.start_color()
        curses.use_default_colors()

        try:
            # Initialize colors
            curses.init_pair(1, curses.COLOR_RED, -1)
            curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
            curses.init_pair(5, curses.COLOR_RED, curses.COLOR_YELLOW)
            for y, row in enumerate(self.maze.grid):
                for x, cell in enumerate(row):
                    cy = y * 2
                    cx = x * 4
                    cell: Cell 

                    if cell.up:
                        self.stdscr.addstr(cy, cx, "▀▀▀▀", curses.color_pair(1))
                    else:
                        self.stdscr.addstr(cy, cx, "▀", curses.color_pair(1))
                    if cell.path_42:
                        self.stdscr.addstr(
                                cy + 1, cx , '    ', curses.color_pair(4))
                        self.stdscr.addstr(
                                cy , cx , '    ', curses.color_pair(4))
                        if cell.up:
                            self.stdscr.addstr(cy, cx, "▀▀▀▀", curses.color_pair(5))
                    if y == self.maze.height - 1:
                        self.stdscr.addstr(cy + 2, cx , "▀▀▀▀▀", curses.color_pair(1))
                    if cell.right and x == self.maze.width - 1:
                        self.stdscr.addstr(cy, cx + 4, "█", curses.color_pair(1))
                    if cell.left:
                        self.stdscr.addstr(cy, cx, "█", curses.color_pair(1))
                        self.stdscr.addstr(cy + 1, cx, "█", curses.color_pair(1))
                        if cell.is_start:
                            self.stdscr.addstr(
                                cy + 1, cx + 1, "██", curses.color_pair(3))
                        if cell.is_end:
                            self.stdscr.addstr(
                                cy + 1, cx + 1, "██", curses.color_pair(3))
                        if x == width - 1:
                            self.stdscr.addstr(cy + 1, cx + 4, "█", curses.color_pair(1))
                    else:
                        if x == width - 1:
                            self.stdscr.addstr(cy + 1, cx + 4, "█", curses.color_pair(1))
                        # if x < width - 2 and not cell.right:
                        #     self.stdscr.addstr(cy + 1, cx, "")
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