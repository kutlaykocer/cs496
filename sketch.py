
class Sketch:
    matrix = [[]]
    size = 0

    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for i in range(size)] for i in range(size)]

    def print_matrix(self):
        for i in range(self.size):
            print(self.matrix[0][i])

    def get_matrix(self):
        return self.matrix

    def count_matrix(self, i, j):
        self.matrix[i][j] += 1
