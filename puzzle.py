
#check if a cell is assigned or not
class cell:
    def __init__(self, binary_digit):
        self.digit = binary_digit

        if binary_digit != '-':
            self.digit = int(binary_digit)
            self.assigned = True
        else:
            self.assigned = False
    def __str__(self):
        return str(self.digit)

class PUZZLE:
    def __init__(self, puzzle, size):
        self.puzzle = puzzle
        self.size = size


class CSP:
    def mrv(self):
        pass

    def lcv(self):
        pass

    def forward_checking(self):
        pass

    def mac(self):
        pass

    def backtrack(self):
        pass

if __name__ == '__main__':
    #the input
    n, m = input("").split(" ")
    n = int(n)
    table = [[] for i in range(n)]
    for i in range(n):
        table[i] = input("").split(" ")
    for i in range(n):
        for j in range(n):
            table[i][j] = cell(table[i][j])
    puzzle = PUZZLE(table, n)

