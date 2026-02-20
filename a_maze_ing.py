import sys
from config_parser import load_config
from mazegen import MazeGenerator
from maze_drawer import MazeDrawer
from solver import solve
from mazegen_algorithm import DFS, Prim
from hex_encoder import hex_encoder
from curses import wrapper
import curses
import time
from maze import Maze


time_flag = False


def on_off_time() -> bool:
    """Toggle the global time_flag and return its new value."""
    global time_flag
    time_flag = not time_flag
    return time_flag


def show_error(stdscr: curses.window, message: str) -> None:
    """Display a centered error message in a popup window."""
    try:
        h, w = stdscr.getmaxyx()

        box_h = 5
        box_w = min(len(message) + 4, w - 2)

        start_y = max((h - box_h) // 2, 0)
        start_x = max((w - box_w) // 2, 0)

        win = curses.newwin(box_h, box_w, start_y, start_x)
        win.box()
        win.addstr(2, 2, message[: box_w - 4])
        win.refresh()
        win.getch()
    except curses.error:
        pass


def call_generator(
    stdscr: curses.window,
    maze_grid,
    config,
    algorithm,
    generator: MazeGenerator,
    drawer: MazeDrawer,
) -> None:
    """Regenerate the maze safely."""

    try:
        generator.reset()
        drawer.show_panel()

        for _ in generator.generate(algorithm):
            drawer.draw()
            if time_flag:
                time.sleep(0.01)
        solution = solve(maze_grid, config)
        hex_encoder(maze_grid, config, solution)
        drawer.regenerate_solver_fixer()

    except curses.error:
        stdscr.clear()

    except Exception as e:
        show_error(stdscr, f"Generation error: {e}")


def main(stdscr: curses.window) -> None:
    """Run the main curses application loop."""

    curses.curs_set(0)
    stdscr.keypad(True)

    if len(sys.argv) != 2:
        show_error(stdscr, "Usage: python3 a_maze_ing.py <config_file>")
        return

    try:
        config = load_config(sys.argv[1])
    except Exception as e:
        show_error(stdscr, f"Config error: {e}")
        return

    try:
        generator: MazeGenerator = MazeGenerator(config)
        algorithm = DFS() if config.algo == "dfs" else Prim()
        maze_grid: Maze = Maze(config.width, config.height, generator.grid)
        drawer: MazeDrawer = MazeDrawer(maze_grid, stdscr)
    except Exception as e:
        show_error(stdscr, f"Initialization error: {e}")
        return

    try:
        for _ in generator.generate(algorithm):
            drawer.draw()
            if time_flag:
                time.sleep(0.01)
        solution = solve(maze_grid, config)
        hex_encoder(maze_grid, config, solution)
    except Exception as e:
        show_error(stdscr, f"Initial generation error: {e}")
        return

    while True:
        try:
            drawer.draw()
            key: int = stdscr.getch()

            if key == curses.KEY_RESIZE:
                curses.update_lines_cols()
                stdscr.clear()
                continue

            if key == ord("4"):
                on_off_time()

            elif key == ord("1"):
                call_generator(
                    stdscr, maze_grid, config, algorithm, generator, drawer)

            elif key == ord("2"):
                if not drawer.show_solution:
                    solve(maze_grid, config)
                    drawer.draw()
                    drawer.solve()
                else:
                    drawer.toggle_solution()

            elif key == ord("3"):
                drawer.shift_theme()

            elif key == ord("5"):
                break

        except curses.error:
            stdscr.clear()
            continue

        except Exception as e:
            show_error(stdscr, f"Runtime error: {e}")
            break


if __name__ == "__main__":
    """Start the curses wrapper."""
    try:
        wrapper(main)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"\n[FATAL ERROR]: {e}")
