from mazegen import Cell
from themes import THEMES
import curses


class MazeDrawer:
    def __init__(self, maze, stdscr):
        self.maze = maze
        self.stdscr: curses.window = stdscr
        self.th_keys = list(THEMES.keys())
        self.panel_lst = [
            "==== ",
            "1. Re-generate a new maze",
            "2. Show/Hide path from entry to exit",
            "3. Rotate maze colors",
            "4. Quit",
            "==== Bonus Panel ====",
            "a. click 'a' to enable/disable animation"
        ]
        self.current_theme = 0
        self.panel_heigth = len(self.panel_lst) + 1
        curses.start_color()
        curses.use_default_colors()
        self.theme_setter()

    def theme_setter(self):
        theme_name = self.th_keys[self.current_theme]
        data = THEMES[theme_name]
        curses.init_pair(1, *data["WALL"])
        curses.init_pair(2, *data["START"])
        curses.init_pair(3, *data["END"])
        curses.init_pair(4, *data["PATH"])
        curses.init_pair(5, *data["PATH_UP"])

    def draw(self):
        self.stdscr.clear()
        height = len(self.maze.grid)
        width = len(self.maze.grid[0]) if height > 0 else 0

        required_height = height * 2 + 1
        required_width = width * 4

        ter_y, ter_x = self.stdscr.getmaxyx()

        if ter_y < required_height or ter_x < required_width:
            self.stdscr.clear()
            msg = "Terminal too small to draw your maze!"
            self.stdscr.addstr(ter_y // 2, (ter_x - len(msg)) // 2, msg)
            self.stdscr.refresh()
            return
        else:
            try:
                for y, row in enumerate(self.maze.grid):
                    self.show_panel()
                    for x, cell in enumerate(row):
                        cy = y * 2
                        cx = x * 4
                        cell: Cell
                        has_corner = False
                        if cell.up or cell.left:
                            has_corner = True
                        elif y > 0 and self.maze.grid[y - 1][x].left:
                            has_corner = True
                        elif x > 0 and self.maze.grid[y][x - 1].up:
                            has_corner = True
                        elif (
                            y > 0
                            and x > 0
                            and (
                                self.maze.grid[y - 1][x].left or self.maze.grid[y][x - 1].up
                            )
                        ):
                            has_corner = True
                        if cell.up:
                            self.stdscr.addstr(cy, cx, "▀▀▀▀", curses.color_pair(1))
                        elif has_corner:
                            self.stdscr.addstr(cy, cx, "▀", curses.color_pair(1))
                        if cell.is_start:
                            self.stdscr.addstr(cy + 1, cx + 1, "██", curses.color_pair(3))
                        if cell.is_end:
                            self.stdscr.addstr(cy + 1, cx + 1, "██", curses.color_pair(4))
                        if cell.path_42:
                            self.stdscr.addstr(cy + 1, cx, "    ", curses.color_pair(4))
                            self.stdscr.addstr(cy, cx, "    ", curses.color_pair(4))
                            if cell.up:
                                self.stdscr.addstr(cy, cx, "▀▀▀▀▀", curses.color_pair(5))
                        if y == self.maze.height - 1:
                            self.stdscr.addstr(cy + 2, cx, "▀▀▀▀▀", curses.color_pair(1))
                        if cell.right and x == self.maze.width - 1:
                            self.stdscr.addstr(cy, cx + 4, "█", curses.color_pair(1))
                        if cell.left:
                            self.stdscr.addstr(cy, cx, "█", curses.color_pair(1))
                            self.stdscr.addstr(cy + 1, cx, "█", curses.color_pair(1))
                            if x == width - 1:
                                self.stdscr.addstr(
                                    cy + 1, cx + 4, "█", curses.color_pair(1)
                                )
                        else:
                            if x == width - 1:
                                self.stdscr.addstr(
                                    cy + 1, cx + 4, "█", curses.color_pair(1)
                                )
            except Exception:
                pass

        self.stdscr.refresh()

    # Solve prototype
    def solve(self) -> str:
        pass

    def show_path(self) -> None:
        pass

    def shift_theme(self, random_theme=False):
        if random_theme:
            import random

            self.current_theme = random.randint(0, len(self.th_keys) - 1)
        else:
            self.current_theme = (self.current_theme + 1) % len(self.th_keys)

        self.theme_setter()
        self.draw()

    def show_panel(self):
        self.terminal_h, self.terminal_w = self.stdscr.getmaxyx()
        panel_y = self.terminal_h - self.panel_heigth
        for i, item in enumerate(self.panel_lst):
            if i >= self.panel_heigth - 1:
                break
            try:
                self.stdscr.addstr(panel_y + 1 + i, 2, item)
            except curses.error:
                pass
        self.stdscr.refresh()

    def show_info_panel(self):
        h, w = self.stdscr.getmaxyx()
        curses.init_pair(20, curses.COLOR_BLACK, curses.COLOR_WHITE)
        status = (
            f" MAZE {self.maze.width}x{self.maze.height} | ",
            "Algo: DFS | ",
            "Theme: theme x | ",
            f"Start: {self.maze.start}  |  "
            f"End: {self.maze.end} "
        )
        self.stdscr.addstr(y - 1, 0," " * (w - 1), curses.init_pair(20))
        status = status[: w - 1]
        self.stdscr.addstr(h - 1, 0, status, curses.init_pair(20))
