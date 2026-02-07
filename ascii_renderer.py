# ascii_renderer_demo.py

from typing import List, Tuple


# Bits: 0=N, 1=E, 2=S, 3=W
# 1 means CLOSED wall

def render_ascii(maze: List[List[int]],
                 entry: Tuple[int, int],
                 exit: Tuple[int, int],
                 path: List[str] | None = None) -> None:
    height = len(maze)
    width = len(maze[0])

    # Draw top border
    print("+" + "---+" * width)

    for y in range(height):
        # Draw cell content + vertical walls
        line_cells = "|"
        for x in range(width):
            if (x, y) == entry:
                cell = " E "
            elif (x, y) == exit:
                cell = " X "
            else:
                cell = "   "

            east_closed = maze[y][x] & (1 << 1)
            line_cells += cell
            line_cells += "|" if east_closed else " "
        print(line_cells)

        # Draw horizontal walls
        line_walls = "+"
        for x in range(width):
            south_closed = maze[y][x] & (1 << 2)
            line_walls += "---+" if south_closed else "   +"
        print(line_walls)


# ---------------- DEMO ----------------

def demo_maze() -> List[List[int]]:
    # 4x4 demo maze (hardcoded)
    # This is just to visualize something now
    return [
        [0b1011, 0b1001, 0b1001, 0b1101],
        [0b0011, 0b0001, 0b0100, 0b0101],
        [0b0011, 0b0100, 0b0010, 0b0101],
        [0b0111, 0b0110, 0b0110, 0b1110],
    ]


if __name__ == "__main__":
    maze = demo_maze()
    entry = (0, 0)
    exit = (3, 3)

    render_ascii(maze, entry, exit)