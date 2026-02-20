from mazegen import Cell
from maze import Maze
from themes import THEMES
import curses


class MazeDrawer:
    def __init__(self, maze: Maze, stdscr: "curses.window") -> None:
        """ initialize base atrrubites of the drawing class """
        self.maze = maze
        self.stdscr: curses.window = stdscr
        self.th_keys = list(THEMES.keys())
        self.show_solution = False
        self.panel_lst = [
            "==== A-Maz-ing ====",
            "1. Re-generate a new maze",
            "2. Show/Hide path from entry to exit",
            "3. Rotate maze colors",
            "4. click '4' to enable/disable animation",
            "5. Quit",
            "",
            "Select option (1-5): "
        ]
        self.current_theme = 0
        self.panel_heigth = len(self.panel_lst) + 1
        curses.start_color()
        curses.use_default_colors()
        self.theme_setter()

    def theme_setter(self) -> None:
        """theme id setter"""
        theme_name = self.th_keys[self.current_theme]
        data = THEMES[theme_name]
        curses.init_pair(1, *data["WALL"])
        curses.init_pair(2, *data["START"])
        curses.init_pair(3, *data["END"])
        curses.init_pair(4, *data["PATH"])
        curses.init_pair(5, *data["PATH_UP"])

    def draw(self) -> None:
        """ Method to Draw the maze """
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
                                self.maze.grid[y - 1][x].left
                                or self.maze.grid[y][x - 1].up
                            )
                        ):
                            has_corner = True
                        if cell.up:
                            self.stdscr.addstr(
                                cy, cx, "▀▀▀▀", curses.color_pair(1))
                        elif has_corner:
                            self.stdscr.addstr(
                                cy, cx, "▀", curses.color_pair(1))
                        if cell.is_start:
                            self.stdscr.addstr(
                                cy + 1, cx + 1, "██", curses.color_pair(2)
                            )
                        if cell.is_end:
                            self.stdscr.addstr(
                                cy + 1, cx + 1, "██", curses.color_pair(3)
                            )
                        if cell.path_42:
                            self.stdscr.addstr(
                                cy + 1, cx, "    ", curses.color_pair(4))
                            self.stdscr.addstr(
                                cy, cx, "    ", curses.color_pair(4))
                            if cell.up:
                                self.stdscr.addstr(
                                    cy, cx, "▀▀▀▀▀", curses.color_pair(5)
                                )

                        if self.show_solution and cell.solution_path:
                            self.stdscr.addstr(
                                cy + 1, cx + 1, "███", curses.color_pair(4)
                            )
                            if cell.is_start:
                                self.stdscr.addstr(
                                    cy + 1, cx + 1, "██", curses.color_pair(2)
                                )
                            if (
                                y > 0
                                and self.maze.grid[y - 1][x].solution_path
                                and not cell.up
                            ):
                                self.stdscr.addstr(
                                    cy, cx + 1, "███", curses.color_pair(4)
                                )
                                if cell.up:
                                    self.stdscr.addstr(
                                        cy, cx, "▀▀▀▀", curses.color_pair(5)
                                    )
                            if (
                                x > 0
                                and self.maze.grid[y][x - 1].solution_path
                                and not cell.left
                            ):
                                self.stdscr.addstr(
                                    cy + 1, cx, "██", curses.color_pair(4)
                                )
                            if cell.is_end:
                                self.stdscr.addstr(
                                    cy + 1, cx + 1, "██", curses.color_pair(3)
                                )

                        if y == self.maze.height - 1:
                            self.stdscr.addstr(
                                cy + 2, cx, "▀▀▀▀▀", curses.color_pair(1)
                            )
                        if cell.right and x == self.maze.width - 1:
                            self.stdscr.addstr(
                                cy, cx + 4, "█", curses.color_pair(1))
                        if cell.left:
                            self.stdscr.addstr(
                                cy, cx, "█", curses.color_pair(1))
                            self.stdscr.addstr(
                                cy + 1, cx, "█", curses.color_pair(1))
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
        self.show_banner()
        self.show_panel()
        self.stdscr.refresh()

    def solve(self) -> None:
        """Animate the solution path drawing"""
        try:
            for y, row in enumerate(self.maze.grid):
                self.show_panel()

                for x, cell in enumerate(row):
                    if cell.solution_path:
                        cy = y * 2
                        cx = x * 4

                        self.stdscr.addstr(
                            cy + 1, cx + 1, "███", curses.color_pair(4))
                        if (
                            y > 0
                            and self.maze.grid[y - 1][x].solution_path
                            and not cell.up
                        ):
                            self.stdscr.addstr(
                                cy, cx + 1, "███", curses.color_pair(4))
                        if (
                            x > 0
                            and self.maze.grid[y][x - 1].solution_path
                            and not cell.left
                        ):
                            self.stdscr.addstr(
                                cy + 1, cx, "██", curses.color_pair(4))

                        if cell.solution_path and not cell.left:
                            self.stdscr.addstr(
                                cy, cx + 1, "", curses.color_pair(5))
                        elif cell.up and cell.solution_path:
                            self.stdscr.addstr(
                                cy, cx + 1, "▀▀▀", curses.color_pair(5))
                        self.stdscr.refresh()
                        curses.napms(30)

        except Exception:
            pass
        self.show_solution = True

    def toggle_solution(self) -> None:
        """Toggle the solution path visibility"""
        self.show_solution = not self.show_solution
        self.draw()

    def shift_theme(self) -> None:
        """ changing theme colors by using a dict as a source """
        self.current_theme = (self.current_theme + 1) % len(self.th_keys)

        self.theme_setter()
        self.draw()

    def show_panel(self) -> None:
        """ Show pnael of options """
        self.terminal_h, self.terminal_w = self.stdscr.getmaxyx()
        maze_end_y = (len(self.maze.grid) * 2) + 1
        panel_y = self.terminal_h - self.panel_heigth
        if panel_y <= maze_end_y:
            try:
                self.stdscr.addstr(
                    self.terminal_h - 1,
                    2,
                    "!! No space left for menu !!",
                    curses.A_REVERSE,
                )
            except curses.error:
                pass
        else:
            for i, item in enumerate(self.panel_lst):
                if i >= self.panel_heigth - 1:
                    break
                try:
                    self.stdscr.addstr(panel_y + 1 + i, 2, item)
                except curses.error:
                    pass
        last_index = len(self.panel_lst) - 1
        last_line_y = panel_y + 1 + last_index
        last_line_text = self.panel_lst[last_index]

        cursor_x = 2 + len(last_line_text)

        try:
            self.stdscr.move(last_line_y, cursor_x)
        except curses.error:
            pass
        self.stdscr.refresh()

    def regenerate_solver_fixer(self) -> None:
        "fixing solver path showing"
        if self.show_solution is True:
            self.show_solution = False
            self.draw()

    def show_banner(self) -> None:
        """Display a dynamic banner with maze status and current settings."""
        maze_info = f"Maze: {self.maze.width}x{self.maze.height}"
        theme_info = f"Theme: {self.th_keys[self.current_theme]}"
        solution_info = (
            "Solution: ON" if self.show_solution else "Solution: OFF"
        )

        banner_parts = [
            maze_info,
            theme_info,
            solution_info,
        ]
        banner_text = " | ".join(part for part in banner_parts if part)

        panel_y = self.terminal_h - self.panel_heigth
        banner_y = max(panel_y - 1, 0)
        banner_x = max((self.terminal_w - len(banner_text)) // 2, 0)

        try:
            self.stdscr.addstr(
                banner_y,
                banner_x,
                banner_text,
                curses.A_REVERSE,
            )
        except curses.error:
            pass
