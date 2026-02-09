import random
from maze import Maze


class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        self.up = True
        self.down = True
        self.left = True
        self.right = True

        self.is_start = False
        self.is_end = False
        self.visited = False

    def __str__(self):
        return " " if not self.down else "_"


class MazeGenerator:
    def __init__(self, config, algorithm):
        self.config = config
        self.algorithm = algorithm
        self.WIDTH = 20
        self.HEIGHT = 25
        self.ENTRY = (0, 0)
        self.EXIT = (9, 9)

        self.grid = [
            [Cell(x, y) for x in range(self.WIDTH)]
            for y in range(self.HEIGHT)
        ]

    def research_about_neighbor(self, cell) -> list[Cell]:
        neighbors = []

        cx, cy = cell.x, cell.y
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < self.WIDTH and 0 <= ny < self.HEIGHT:
                n = self.grid[ny][nx]
                if not n.visited:
                    neighbors.append(n)

        return neighbors

    def prepare_maze(self) -> None:
        """
        Initialize the maze grid BEFORE generation.
        All cells are unvisited and all walls are closed.
        Marks ENTRY and EXIT.
        """
        self.grid = [
            [Cell(x, y) for x in range(self.WIDTH)]
            for y in range(self.HEIGHT)
        ]

        # Reset walls & visited for each cell
        for row in self.grid:
            for cell in row:
                cell.up = True
                cell.down = True
                cell.left = True
                cell.right = True
                cell.visited = False
                cell.is_start = False
                cell.is_end = False

        # Mark the start and end
        sx, sy = self.ENTRY
        self.grid[sy][sx].is_start = True

        ex, ey = self.EXIT
        self.grid[ey][ex].is_end = True

    def generate_steps(self):
        """
        DFS generator that yields the maze state after each cell opens.
        """
        stack: list[Cell] = []

        sx, sy = self.ENTRY
        start = self.grid[sy][sx]
        start.visited = True
        start.is_start = True

        stack.append(start)

        while stack:
            cell = stack[-1]
            neighbors = self.research_about_neighbor(cell)

            if not neighbors:
                stack.pop()
                continue

            neighbor = random.choice(neighbors)
            neighbor.visited = True

            # Remove walls
            if neighbor.x > cell.x:
                cell.right = False
                neighbor.left = False
            elif neighbor.x < cell.x:
                cell.left = False
                neighbor.right = False
            elif neighbor.y > cell.y:
                cell.down = False
                neighbor.up = False
            elif neighbor.y < cell.y:
                cell.up = False
                neighbor.down = False

            stack.append(neighbor)

            yield self.grid

    def generate_closed_maze(self):
        """
        Returns a maze where ALL walls are closed.
        This is the initial state for animation.
        """
        self.prepare_maze()

        maze = Maze(self.WIDTH, self.HEIGHT, self.grid)
        return maze