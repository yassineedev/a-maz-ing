from mazegen import MazeGenerator

maze = MazeGenerator.generate


class MazeDrawer:
    def __init__(self, maze):
        self.maze = maze

    # Draw part here
    def draw(self):
        print("╔" + "══" * self.maze.width + "╗")

        for y in range(self.maze.height):
            # ── Cell content + vertical walls ──
            line = "║"
            for x in range(self.maze.width):
                cell = self.maze.grid[y][x]

                if cell.is_start:
                    body = "S"
                elif cell.is_end:
                    body = "E"
                else:
                    body = " "

                side = "║" if cell.right else " "
                line += body + side
            print(line)

            # ── Bottom walls ──
            line = "╠"
            for x in range(self.maze.width):
                cell = self.maze.grid[y][x]
                bottom = "══" if cell.down else "  "
                line += bottom
            line += "╣"
            print(line)

        # Bottom border
        print("╚" + "══" * self.maze.width + "╝")

    # Solve prototype
    def solve(self) -> str:
        pass

    def show_path(self) -> None:
        pass

    def rotate_colors(self) -> None:
        pass