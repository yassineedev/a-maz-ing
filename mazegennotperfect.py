import random

def count_walls(cell):
    walls = [cell.up, cell.down, cell.left, cell.right]
    return sum(walls)

def get_dead_ends(grid) -> list:
    dead_ends = []
    for row in grid:
        for cell in row:
            if count_walls(cell) == 3:
                dead_ends.append(cell)
    return dead_ends

def get_valid_neighbors(grid, cell, config) -> list:
    valid_neighbors = []
    cx, cy = cell.x, cell.y
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dy, dx in directions:
        ny, nx = cy + dy, cx + dx

        if 0 <= ny < config.height and 0 <= nx < config.width:
            neighbor = grid[ny][nx]
            if not neighbor.path_42:
                valid_neighbors.append(neighbor)
    
    return valid_neighbors

def break_wall(a, b) -> None:
    if a.x < b.x:
        a.right = b.left = False
    elif a.x > b.x:
        a.left = b.right = False
    elif a.y < b.y:
        a.down = b.up = False
    elif a.y > b.y:
        a.up = b.down = False

def convert_to_imperfect_maze(grid, config, chance=0.5):
    cells = get_dead_ends(grid)
    for cell in cells:
        if random.random() < chance:
            neighbors = get_valid_neighbors(grid, cell, config)
            if neighbors:
                break_wall(cell, random.choice(neighbors))
                yield grid