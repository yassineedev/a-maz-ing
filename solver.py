class MazeSolver():
    def __init__(self, maze):
        self.maze = maze

    def solve(self):
        queue = []
        visited = set()
        parent = dict()
        # st