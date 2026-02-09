import sys
# from config_parser import load_config, ConfigError
from mazegen import MazeGenerator
from maze_drawer import MazeDrawer
from curses import wrapper
import time


def main(stdscr) -> None:
    generator = MazeGenerator(sys.argv, "dfs")
    maze = generator.generate_closed_maze()
    drawer = MazeDrawer(maze, stdscr)
    drawer.draw()
    time.sleep(0.5)

    for _ in generator.generate_steps():
        drawer.draw()
        time.sleep(0.05)

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break


if __name__ == "__main__":
    wrapper(main)
