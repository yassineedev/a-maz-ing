from mazegen import MazeGenerator

maze = MazeGenerator.generate


class MazeDrawer:
    def __init__(self, maze):
        self.maze = maze

    # Draw part here
    def draw(self):
        print(" " + "_" * (self.maze.width * 2 - 1))

        for y in range(self.maze.height):
            line = "|"
            for x in range(self.maze.width):
                cell = self.maze.grid[y][x]

                if cell.is_start:
                    body = "S"
                elif cell.is_end:
                    body = "E"
                else:
                    body = " " if not cell.down else "_"

                side = " " if not cell.right else "|"

                line += body + side
            print(line)

    # Solve prototype
    def solve(self) -> str:
        pass

    def show_path(self) -> None:
        pass

    def rotate_colors(self) -> None:
        pass


draw = MazeDrawer(maze)
