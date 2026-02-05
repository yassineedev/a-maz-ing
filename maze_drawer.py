from mazegen import MazeGenerator

maze = MazeGenerator.generate


class MazeDrawer:
    def __init__(self, maze):
        self.maze = maze

    # Draw part here
    # def draw(self):
    #     print(" " + "_" * (self.maze.width * 2 - 1))

    #     for y in range(self.maze.height):
    #         line = "║"
    #         for x in range(self.maze.width):
    #             cell = self.maze.grid[y][x]

    #             if cell.is_start:
    #                 body = "S"
    #             elif cell.is_end:
    #                 body = "E"
    #             else:
    #                 body = " " if not cell.down else "═"

    #             side = " " if not cell.right else "|"

    #             line += body + side
    #         print(line)

    def draw(self):
        width = self.maze.width
        height = self.maze.height

        # TOP BORDER
        print("+" + "---+" * width)

        for y in range(height):
            # CELL CONTENT ROW
            line = "|"
            for x in range(width):
                cell = self.maze.grid[y][x]

                if cell.is_start:
                    content = " S "
                elif cell.is_end:
                    content = " E "
                else:
                    content = " . "

                line += content
                line += "|" if cell.right else " "
            print(line)


            line = "+"
            for x in range(width):
                cell = self.maze.grid[y][x]
                line += "---+" if cell.down else "   +"
            print(line)

    # Solve prototype
    def solve(self) -> str:
        pass

    def show_path(self) -> None:
        pass

    def rotate_colors(self) -> None:
        pass