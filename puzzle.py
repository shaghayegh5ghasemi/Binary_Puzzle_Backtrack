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
        self.domains = [[] for i in range(self.size)]
        #define domains
        for i in range(self.size):
            for j in range(self.size):
                self.domains[i].append([0, 1])
        # fix initial domain
        for i in range(n):
            for j in range(n):
                if self.table[i][j] != '-':
                    value = self.table[i][j]
                    self.domains[i][j] = [value]

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
        strings = []
        for m in range(self.size):
            string_r = ''
            string_c = ''
            for n in range(self.size):
                string_r += str(temptable[m][n])
                string_c += str(temptable[n][m])
            if '-' not in string_r:
                # check condition 1 in rows
                if string_r.count('0') != string_r.count('1'):
                    return False
                # check condition 2 in rows
                if string_r in strings:
                    return False
                else: strings.append(string_r)
            if '-' not in string_c:
                # check condition 1 in columns
                if string_c.count('0') != string_c.count('1'):
                    return False
                #check condition 2 in columns
                if string_c in strings:
                    return False
                else: strings.append(string_c)
            #check condition 3
            if '000' in string_r or '111' in string_r or '000' in string_c or '111' in string_c:
                return False
        return True

    def select_variable(self):
        pass

    def check_consistency(self):
        pass

    def update_domain(self, i, j, value):
        pass

    def least_constraint_value(self, puzzle, i, j):
        pass

#csp model to solve the problem
class CSP:

    def forward_checking(self):
        pass

    def mac(self):
        pass

    def backtrack(self, problem):
        if (problem.isComplete()):
            return problem
        i, j = problem.select_variable()
        for value in problem.domains[i][j]:
            if problem.isConsistent(i, j, value):
                problem.table[i][j].digit = value
                problem.table[i][j].assigned = True
            new_domain = problem.domains
            temp_domain = copy.deepcopy(problem.domains)
            new_domain[i][j] = [value]
            problem.domains = new_domain
            if problem.check_consistency(new_domain):
                result = self.backtrack(problem)
                if result:
                   return result
            problem.domains = temp_domain
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
    puzzle = PUZZLE(table, n)
    print(puzzle.isConsistent(1, 2, 0))
    #solve the puzzle
    # csp_model = CSP()
    # result = csp_model.backtrack(puzzle)
    # print("The answer is:")
    # if (result):
    #     puzzle.print()
    # else:
    #     print("Solving the puzzle was not successful!")


