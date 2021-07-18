import copy

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

#define the problem
class PUZZLE:
    def __init__(self, table, size):
        self.table = table
        self.size = size

    def print(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.table[i][j], end=" ")
            print("")

    #check if all the cells are assigned or not
    def isComplete(self):
        for row in self.table:
            for cell in row:
                if cell.assigned == False:
                    return False
        return True


    def isConsistent(self, i, j, value):
        temptable = copy.deepcopy(self.table)
        temptable[i][j].digit = value
        string_rows = []
        string_columns = []
        for m in range(self.size):
            string_r = ''
            string_c = ''
            for n in range(self.size):
                string_r += str(temptable[m][n].digit)
                string_c += str(temptable[n][m].digit)
            if '-' not in string_r:
                # check condition 1 in rows
                if string_r.count('0') != string_r.count('1'):
                    return False
                # check condition 2 in rows
                if string_r in string_rows:
                    return False
                else: string_rows.append(string_r)
            if '-' not in string_c:
                # check condition 1 in columns
                if string_c.count('0') != string_c.count('1'):
                    return False
                #check condition 2 in columns
                if string_c in string_columns:
                    return False
                else: string_columns.append(string_c)
            #check condition 3
            if '000' in string_r or '111' in string_r or '000' in string_c or '111' in string_c:
                return False
        return True

    def select_variable(self):
        for i, rows in enumerate(self.table):
            for j, cell in enumerate(rows):
                if cell.digit == '-':
                    return (i, j)

    def check_consistency(self, new_domain):
        for i in range(self.size):
            for j in range(self.size):
                if len(new_domain[(i, j)]) == 0 and self.table[i][j].assigned == False:
                    return False
        return True

    def update_domain(self, i, j, value):
        pass

    def least_constraint_value(self, puzzle, i, j):
        pass

#csp model to solve the problem
class CSP:

    def forward_checking(self, i, j, value, problem, domains):
        new_domain = copy.deepcopy(domains)
        new_domain[(i, j)].remove(value)
        return new_domain

    def mac(self):
        pass

    def backtrack(self, problem, domains):
        if (problem.isComplete()):
            return problem
        i, j = problem.select_variable()
        for value in domains[(i, j)]:
            if problem.isConsistent(i, j, value):
                problem.table[i][j].digit = value
                problem.table[i][j].assigned = True
                new_domain = self.forward_checking(i, j, value, problem, domains)
                if problem.check_consistency(new_domain):
                    result = self.backtrack(problem, new_domain)
                    if result:
                        return result
                problem.table[i][j].digit = '-'
                problem.table[i][j].assigned = False
        return False



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
    #init domain
    domains = {}
    for i in range(n):
        for j in range(n):
            if table[i][j].digit == '-':
                domains[(i, j)] = [0, 1]
            else:
                domains[(i, j)] = []

    puzzle = PUZZLE(table, n)
    #solve the puzzle
    csp_model = CSP()
    result = csp_model.backtrack(puzzle, domains)
    print("The answer is:")
    if (result):
        puzzle.print()
    else:
        print("Solving the puzzle was not successful!")


