import sys
from config_parser import load_config, ConfigError
from mazegen import MazeGenerator
from maze_drawer import MazeDrawer
from solver import MazeSolver
from mazegen_algorithm import DFS, Prim
from hex_encoder import hex_encoder

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        sys.exit(1)

    try:
        # ------- Mohamed --------
        config = load_config(sys.argv[1])
        generator = MazeGenerator(config)
        maze = generator.generate(DFS())
        

        # ------- Yassen --------
        solver = MazeSolver(maze)
        solution_path = solver.solve()
        hex_encoder(maze, config, solution_path)
        drawer = MazeDrawer(maze)
        drawer.draw()

    except ConfigError as e:
        print(f"Config error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR]: {e}")
        sys.exit(1)
        

if __name__ == "__main__":
    main()
