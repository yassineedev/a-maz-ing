import sys
from config_parser import load_config, ConfigError
from mazegen import MazeGenerator
from maze_drawer import MazeDrawer
from solver import MazeSolver
from mazegen_algorithm import DFS, Prim
from hex_encoder import hex_encoder
from curses import wrapper
import time

def main(stdscr) -> None:
    argv = sys.argv
    if len(argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        sys.exit(1)


    # ------- Mohamed --------
    config = load_config(argv[1])
    generator = MazeGenerator(config)
    maze = generator.generate_closed_maze()
    

    # ------- Yassine --------
    
    drawer = MazeDrawer(maze, stdscr) 
    drawer.draw()

    for _ in generator.generate(Prim()):
        drawer.draw()
        time.sleep(0.05)

    solver = MazeSolver(maze)
    solution_path = solver.solve()
    hex_encoder(maze, config, solution_path)

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == "__main__":
    try:
        wrapper(main)
    except Exception as e:
        print(e)