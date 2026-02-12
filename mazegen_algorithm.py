from abc import ABC, abstractmethod
import random
from mazegen import Cell


class MazeAlgorithm(ABC):
    @abstractmethod
    def apply(self, grid: list[list[Cell]], config) -> None:
        pass

    def get_unvisited_neighbors(self, grid, cell, config):
        neighbors = []
        cx, cy = cell.x, cell.y
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < config.width and 0 <= ny < config.height:
                n = grid[ny][nx]
                if not n.visited and not n.path_42:
                    neighbors.append(n)

        return neighbors

    def remove_walls(self, a, b):
        if a.x < b.x: a.right = b.left = False
        elif a.x > b.x: a.left = b.right = False
        elif a.y < b.y: a.down = b.up = False
        elif a.y > b.y: a.up = b.down = False

# ----- this is the first algorithem ----
class DFS(MazeAlgorithm):
    def apply(self, grid: list[list[Cell]], config):
        stack: list[Cell] = []
        sx, sy = config.entry
        start = grid[sy][sx]
        start.visited = True
        stack.append(start)

        while stack:
            cell = stack[-1]
            neighbors = self.get_unvisited_neighbors(grid, cell, config)
            if not neighbors:
                stack.pop()
                continue

            neighbor = random.choice(neighbors)
            self.remove_walls(cell, neighbor)
            neighbor.visited = True
            stack.append(neighbor)
            yield grid
# ----- this is the sacant algorithem ----
class Prim(MazeAlgorithm):
    def apply(self, grid, config):
        frontiers = []
        sx, sy = config.entry
        start = grid[sy][sx]

        for n in self.get_unvisited_neighbors(grid, start, config):
            frontiers.append((start, n))
        while frontiers:
            cell, neighbor = random.choice(frontiers)
            frontiers.remove((cell, neighbor))
            
            if neighbor.visited:
                continue

            self.remove_walls(cell, neighbor)
            neighbor.visited = True

            for n in self.get_unvisited_neighbors(grid, neighbor, config):
                frontiers.append((neighbor, n))
            yield grid
