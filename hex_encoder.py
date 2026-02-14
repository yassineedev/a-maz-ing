from config_parser import ConfigError

def get_hex_value(cell) -> str:
    value = 0
    if cell.up: value |= (1 << 0) 
    if cell.right: value |= (1 << 1)
    if cell.down: value |= (1 << 2)
    if cell.left: value |= (1 << 3)

    return format(value, 'X') 

def hex_encoder(maze, config, solution_path):
    """ Writes the maze to file """
    try:
        with open(config.output_file, "w") as maze_file:
            for row in maze.grid:
                line = ""
                for cell in row:
                    line += get_hex_value(cell)
                maze_file.write(line + "\n")
            
            maze_file.write("\n")
            
            entry_str = f"{config.entry[0]},{config.entry[1]}"
            maze_file.write(entry_str + "\n")
            
            exit_str = f"{config.exit[0]},{config.exit[1]}"
            maze_file.write(exit_str + "\n")
            
            maze_file.write(solution_path + "\n")
            
    except Exception as e:
        raise ConfigError(f"Error writing output file: {e}")