from collections import deque

def get_unvisited_neighbors(grid, cell, config):
    neighbors = []
    cx, cy = cell.x, cell.y

    # left = W
    if cx > 0 and not cell.left:
        n = grid[cy][cx - 1]
        if not n.visited and not n.path_42:
            neighbors.append((n, 'W'))

    # right = E
    if cx < config.width - 1 and not cell.right:
        n = grid[cy][cx + 1]
        if not n.visited and not n.path_42:
            neighbors.append((n, 'E'))

    # up = N
    if cy > 0 and not cell.up:
        n = grid[cy - 1][cx]
        if not n.visited and not n.path_42:
            neighbors.append((n, 'N'))

    # down = S
    if cy < config.height - 1 and not cell.down:
        n = grid[cy + 1][cx]
        if not n.visited and not n.path_42:
            neighbors.append((n, 'S'))

    return neighbors



def solve(maze, config):
    for row in maze.grid:
        for cell in row:
            cell.visited = False

    queue = deque()
    parent = {}
    move = {}

    start_x, start_y = config.entry
    end_x, end_y = config.exit

    start = maze.grid[start_y][start_x]
    end = maze.grid[end_y][end_x]

    queue.append(start)
    start.visited = True
    parent[(start.y, start.x)] = None

    found = False

    while queue:
        current = queue.popleft()

        if current is end:
            found = True
            break

        neighbors = get_unvisited_neighbors(maze.grid, current, config)

        for neighbor, direction in neighbors:
            neighbor.visited = True
            queue.append(neighbor)

            parent[(neighbor.y, neighbor.x)] = (current.y, current.x)
            move[(neighbor.y, neighbor.x)] = direction

    if not found:
        return ""

    path = []
    key = (end.y, end.x)

    while parent[key] is not None:
        path.append(move[key])
        key = parent[key]

    path.reverse()

    return path
