from collections import deque

class ChessGraph:
    def __init__(self):
        self.board_size = 8
        self.directions = {
            "Knight": [
                (-2, -1), (-2, 1), (2, -1), (2, 1),
                (-1, -2), (-1, 2), (1, -2), (1, 2)
            ]
        }

    def is_valid(self, x, y):
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    def bfs_move(self, piece, start, end):
        queue = deque([(start, 0)]) 
        visited = set()

        while queue:
            (x, y), distance = queue.popleft()
            if (x, y) == end:
                return distance

            if (x, y) not in visited:
                visited.add((x, y))
                for dx, dy in self.directions[piece]:
                    new_x, new_y = x + dx, y + dy
                    if self.is_valid(new_x, new_y):
                        queue.append(((new_x, new_y), distance + 1))

        return -1 
