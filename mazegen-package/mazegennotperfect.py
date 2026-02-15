import random


def count_walls(cell):
    return sum([cell.up, cell.down, cell.left, cell.right])


def get_dead_ends(grid):
    dead_ends = []
    for row in grid:
        for cell in row:
            if count_walls(cell) == 3:
                dead_ends.append(cell)
    return dead_ends


def get_valid_neighbors(grid, cell, config):
    valid_neighbors = []
    cx, cy = cell.x, cell.y

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dy, dx in directions:
        ny, nx = cy + dy, cx + dx

        if not (0 <= ny < config.height and 0 <= nx < config.width):
            continue

        neighbor = grid[ny][nx]

        if neighbor.path_42:
            continue

        if dx == 1 and cell.right:
            valid_neighbors.append(neighbor)
        elif dx == -1 and cell.left:
            valid_neighbors.append(neighbor)
        elif dy == 1 and cell.down:
            valid_neighbors.append(neighbor)
        elif dy == -1 and cell.up:
            valid_neighbors.append(neighbor)

    return valid_neighbors


def break_wall(a, b):
    if a.x < b.x: a.right = b.left = False
    elif a.x > b.x: a.left =  b.right = False
    elif a.y < b.y: a.down = b.up = False
    elif a.y > b.y: a.up = b.down = False


def convert_to_imperfect_maze(grid, config):
    len_rep = int(len(get_dead_ends(grid)))
    for _ in range(len_rep):
        dead_ends = get_dead_ends(grid)
        if not dead_ends:
            break

        cell = random.choice(dead_ends)
        neighbors = get_valid_neighbors(grid, cell, config)

        if not neighbors:
            continue

        neighbor = random.choice(neighbors)
        break_wall(cell, neighbor)

        yield grid