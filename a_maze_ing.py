import sys
from config_parser import load_config, ConfigError
from mazegen import MazeGenerator
from maze_drawer import MazeDrawer
from solver import MazeSolver


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        sys.exit(1)

    try:
        config = load_config(sys.argv[1])
    except ConfigError as e:
        print(f"Config error: {e}")
        sys.exit(1)

    # ------- Mohamed --------
    generator = MazeGenerator(config, "dfs")
    maze = generator.generate()

    # ------- Yassen --------
    solver = MazeSolver(maze)
    solution_path = solver.solve()

    drawer = MazeDrawer(maze, solution_path)
    drawer.draw()


if __name__ == "__main__":
    main()