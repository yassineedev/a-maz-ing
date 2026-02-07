import time


class MazeDrawer:
    def __init__(self, maze):
        self.maze = maze

    def draw(self):
        for row in self.maze.grid:
            for cell in row:
                
                if cell.left:
                    print("|", end="")
                elif cell.right:
                    print("|", end="")
                if cell.up:
                    print("_", end="")
                elif cell.down:
                    print("_", end="")
                if cell.y - 3 == self.maze.width:
                    print(".", end="")
            if cell.right:
                print("|", end="")
                
            print("")


    # Solve prototype
    def solve(self) -> str:
        pass

    def show_path(self) -> None:
        pass

    def rotate_colors(self) -> None:
        pass