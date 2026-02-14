def get_unvisited_neighbors(grid, cell, config):
    neighbors = []
    cx, cy = cell.x, cell.y

    # LEFT
    if cx > 0 and not cell.left:
        n = grid[cy][cx - 1]
        if not n.visited and not n.path_42:
            neighbors.append(n)

    # RIGHT
    if cx < config.width - 1 and not cell.right:
        n = grid[cy][cx + 1]
        if not n.visited and not n.path_42:
            neighbors.append(n)

    # UP
    if cy > 0 and not cell.up:
        n = grid[cy - 1][cx]
        if not n.visited and not n.path_42:
            neighbors.append(n)

    # DOWN
    if cy < config.height - 1 and not cell.down:
        n = grid[cy + 1][cx]
        if not n.visited and not n.path_42:
            neighbors.append(n)

    return neighbors