import sys
from config_parser import load_config, ConfigError
from mazegen import MazeGenerator
from maze_drawer import MazeDrawer
from solver import solve
from mazegen_algorithm import DFS, Prim
from hex_encoder import hex_encoder
from curses import wrapper
import time
from maze import Maze


def main(stdscr) -> None:
    argv = sys.argv
    if len(argv) != 2:
        raise ConfigError("Usage: python3 a_maze_ing.py <config_file>")

    config = load_config(argv[1])
    generator = MazeGenerator(config)
    algorithm = DFS() if config.algo == "dfs" else Prim()
    maze_grid = Maze(config.width, config.height, generator.grid)
    drawer = MazeDrawer(maze_grid, stdscr) 

    for _ in generator.generate(algorithm):
        pass
        drawer.draw()
        time.sleep(0.05)

    solution_path = solve(maze_grid, config)
    hex_encoder(maze_grid, config, solution_path)

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == "__main__":
    try:
        wrapper(main)
    except Exception as e:
        print(f"[EROOR]: {e}")
