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

    #ckeck if there is any conflict in conditions by assigning new value to a cell
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

    #return the index of an unassigned cell using mrv
    def select_variable(self, domains):
        temp = []
        for i, rows in enumerate(self.table):
            for j, cell in enumerate(rows):
                if cell.digit == '-':
                    temp.append(((i, j), len(domains[(i, j)])))
        temp.sort(key=lambda x:x[1])
        return temp[0][0]

    # check if all unassigned cells have values to take
    def check_consistency(self, new_domain):
        for i in range(self.size):
            for j in range(self.size):
                if len(new_domain[(i, j)]) == 0 and self.table[i][j].assigned == False:
                    return False
        return True

#csp model to solve the problem
class CSP:
    #after assigning one value to a cell, we update domains of unassigned cells to delete the digits that will conflicts in some conditions
    def forward_checking(self, i, j, problem, domains):
        new_domain = copy.deepcopy(domains)
        new_domain[(i, j)] = []
        for m in range(problem.size):
            for n in range(problem.size):
                if problem.table[m][n].assigned == False:
                    for val in new_domain[(m, n)]:
                        if problem.isConsistent(m, n, val) == False:
                            new_domain[(m, n)].remove(val)
        return new_domain

    #check domain for arc consistency using AC3
    def mac(self, i, j, problem, domains):
        temp_problem = copy.deepcopy(problem)
        new_domain = copy.deepcopy(domains)
        new_domain[(i, j)] = []
        queue = []
        for m in range(problem.size):
            for n in range(problem.size):
                if problem.table[m][n].assigned == False:
                    for val in new_domain[(m, n)]:
                        if problem.isConsistent(m, n, val) == False:
                            new_domain[(m, n)].remove(val)
                            queue.append((m, n)) #if domain changes add neighbour to the queue
        for node in queue:
            if len(new_domain[node]) == 0:
                continue
            else:
                temp_problem.table[node[0]][node[1]].digit = new_domain[node][0]
                temp_problem.table[node[0]][node[1]].assigned = True
                for k in range(temp_problem.size):
                    for l in range(temp_problem.size):
                        if temp_problem.table[k][l].assigned == False:
                            for val in new_domain[(k, l)]:
                                if temp_problem.isConsistent(k, l, val) == False:
                                    new_domain[(k, l)].remove(val)
                                    queue.append((k, l)) #if domain changes add neighbour to the queue
        return new_domain


    # backtrack algorithm to solve the problem
    def backtrack(self, problem, domains):
        if (problem.isComplete()):
            return problem
        i, j = problem.select_variable(domains)
        for value in domains[(i, j)]:
            if problem.isConsistent(i, j, value):
                problem.table[i][j].digit = value
                problem.table[i][j].assigned = True
                new_domain = self.forward_checking(i, j, problem, domains)
                #new_domain = self.mac(i, j, problem, new_domain)
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
    if result:
        puzzle.print()
    else:
        print("Solving the puzzle was not successful!")


