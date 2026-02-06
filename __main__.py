import sys
from config_parser import load_config, ConfigError
from mazegen import MazeGenerator
from maze_drawer import MazeDrawer
# from solver import MazeSolver
from curses import wrapper



def main(stdscr) -> None:
    # ... (Keep your config and generation logic above) ...

    generator = MazeGenerator(sys.argv, "dfs")
    maze = generator.generate()

    # 1. Create the drawer ONCE
    drawer = MazeDrawer(maze, stdscr)

    while True:
        drawer.draw()
        key = stdscr.getch()
        if key == ord('q'):
            break


if __name__ == "__main__":
    wrapper(main)
