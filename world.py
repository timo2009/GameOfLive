import random

class World:
    def __init__(self, size, random_fill=False, density=0.1):
        self.size = size
        self.matrix = []

        if random_fill:
            self.matrix = [
                [1 if random.random() < density else 0 for _ in range(size)]
                for _ in range(size)
            ]
        else:
            self.matrix = [[0 for _ in range(size)] for _ in range(size)]

        self.alive = set()
        for x in range(size):
            for y in range(size):
                if self.matrix[x][y] == 1:
                    self.alive.add((x, y))

    def count_neighbors(self, x, y):
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        return sum(
            self.matrix[nx][ny]
            for nx in range(max(0, x - 1), min(rows, x + 2))
            for ny in range(max(0, y - 1), min(cols, y + 2))
            if (nx, ny) != (x, y)
        )

    def step(self):
        new_matrix = [row[:] for row in self.matrix]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                neighbors = self.count_neighbors(i, j)

                if self.matrix[i][j] == 1:
                    if neighbors not in (2, 3):
                        new_matrix[i][j] = 0
                else:
                    if neighbors == 3:
                        new_matrix[i][j] = 1

        self.matrix = new_matrix

        self.alive = set()
        for x in range(self.size):
            for y in range(self.size):
                if self.matrix[x][y] == 1:
                    self.alive.add((x, y))

# class World_2:
#     matrix = []
#
#     def count_surrounding_cells_by_for(self, x, y):
#         rows = len(self.matrix)
#         cols = len(self.matrix[0])
#
#         return sum(
#             self.matrix[nx][ny]
#             for nx in range(max(0, x - 1), min(rows, x + 2))
#             for ny in range(max(0, y - 1), min(cols, y + 2))
#             if (nx, ny) != (x, y)
#         )
#
#     def __init__(self, size, random_selection, start_points):
#         if random_selection:
#             self.matrix = [
#                 [random.randint(0, 1) for _ in range(size)]
#                 for _ in range(size)
#             ]
#         else:
#             self.matrix = [[0 for _ in range(size)] for _ in range(size)]
#             for x, y in start_points:
#                 if 0 <= x < size and 0 <= y < size:
#                     self.matrix[x][y] = 1
#
#     def step(self):
#         new_matrix = [row[:] for row in self.matrix]
#
#         for i in range(len(self.matrix)):
#             for j in range(len(self.matrix[i])):
#                 neighbors = self.count_surrounding_cells_by_for(i, j)
#
#                 if self.matrix[i][j] == 1:
#                     if neighbors not in (2, 3):
#                         new_matrix[i][j] = 0
#                 else:
#                     if neighbors == 3:
#                         new_matrix[i][j] = 1
#
#         self.matrix = new_matrix