# def is_pattern_42(grid, config):
#     start_x = int((config.width - 7) / 2)
#     start_y = int((config.height - 5) / 2)

#     pattern = [
#         [1,0,1, 0, 1,1,1],
#         [1,0,1, 0, 0,0,1],
#         [1,1,1, 0, 1,1,1],
#         [0,0,1, 0, 1,0,0],
#         [0,0,1, 0, 1,1,1]
#     ]
#     for row in grid:
#         for cell in row:
#             rel_x = cell.x - start_x
#             rel_y = cell.y - start_y
            
#             if 0 <= rel_y < len(pattern) and 0 <= rel_x < len(pattern[0]):
#                 if pattern[rel_y][rel_x] == 1:
#                     cell.path_42 = True


def is_pattern_42(grid, config):
    start_x = int((config.width - 13) / 2)
    start_y = int((config.height - 5) / 2)

    pattern = [
        [1, 0, 1,1,1, 0, 1,1,1, 0, 1,1,1],
        [1, 0, 0,0,1, 0, 0,0,1, 0, 0,0,1],
        [1, 0, 1,1,1, 0, 1,1,1, 0, 0,0,1],
        [1, 0, 0,0,1, 0, 0,0,1, 0, 0,0,1],
        [1, 0, 1,1,1, 0, 1,1,1, 0, 0,0,1]
    ]
    for row in grid:
        for cell in row:
            rel_x = cell.x - start_x
            rel_y = cell.y - start_y
            
            if 0 <= rel_y < len(pattern) and 0 <= rel_x < len(pattern[0]):
                if pattern[rel_y][rel_x] == 1:
                    cell.path_42 = True