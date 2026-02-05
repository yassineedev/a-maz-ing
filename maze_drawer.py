from mazegen import MazeGenerator

maze = MazeGenerator.generate


class MazeDrawer:
    def __init__(self, maze):
        self.maze = maze

    def draw(self, cell_size=3):
        width = self.maze.width
        height = self.maze.height

        print("█" + "▀" * (cell_size + 1) * width)

        for y in range(height):
            line = "█"
            for x in range(width):
                cell = self.maze.grid[y][x]

                if cell.is_start:
                    content = " S " .center(cell_size)
                elif cell.is_end:
                    content = " E ".center(cell_size)
                else:
                    content = " " * cell_size

                wall = "█" if cell.right else " "
                line += content + wall
            print(line)

            line = "█"
            for x in range(width):
                cell = self.maze.grid[y][x]
                floor = "▄" * cell_size if cell.down else " " *cell_size
                wall = "█" if cell.right else "▄"
                line += floor + wall
            print(line)


    # Solve prototype
    def solve(self) -> str:
        pass

    def show_path(self) -> None:
        pass

    def rotate_colors(self) -> None:
        pass