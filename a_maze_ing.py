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


# ================ Golabal Variabls ========== #
time_flag = False


def on_off_time():
    global time_flag
    time_flag = not time_flag
    return time_flag


# ======= Regenerate Maze by pressing key '1' #
def call_generator(stdscr, config, algorithm, generator, drawer):
    generator.reset()
    drawer.show_panel()
    for _ in generator.generate(algorithm):
        global time_flag
        drawer.draw()
        if time_flag:
            time.sleep(0.01)


def main(stdscr) -> None:
    argv = sys.argv
    if len(argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        sys.exit(1)

    config = load_config(argv[1])
    generator = MazeGenerator(config)
    algorithm = DFS() if config.algo == "dfs" else Prim()
    maze_grid = Maze(config.width, config.height, generator.grid)
    drawer = MazeDrawer(maze_grid, stdscr)
    drawer.show_panel()
    for _ in generator.generate(algorithm):
        global time_flag
        drawer.draw()
        if time_flag:
            time.sleep(0.01)

    while True:
        drawer.draw()

        key = stdscr.getch()

        if key == curses.KEY_RESIZE:
            curses.update_lines_cols()
            stdscr.clear()
            drawer.draw()
            continue
        if key == ord("0"):
            on_off_time()
            stdscr.refresh()
        if key == ord("1"):
            call_generator(stdscr, config, algorithm, generator, drawer)
        elif key == ord("2"):
            if not drawer.show_solution:
                solve(maze_grid, config)
                drawer.draw()
                drawer.solve()  # This will animate and set show_solution to True
            else:
                drawer.toggle_solution()  # This will hide it
        elif key == ord("3"):
            drawer.shift_theme()
        if key == ord("4"):
            break


if __name__ == "__main__":
    try:
        wrapper(main)
    except Exception as e:
        print(f"[EROOR]: {e}")
