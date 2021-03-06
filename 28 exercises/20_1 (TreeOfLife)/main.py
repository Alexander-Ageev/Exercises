DIFFERENT_YEARS = 2 # Variants of the differents growth's ways

MAX_AGE = 3

class Tree(object):
# Create matrix H*W, where 0 - none, n - age of branches
    def __init__ (self, H, W, tree):
        self.heigh = H
        self.width = W
        self.age = 0
        result = []
        for i in tree:
            line = []
            for j in i:
                if j == '.':
                    line.append(0)
                elif j == '+':
                    line.append(1)
            result.append(line)
        self.state = result
    
# Clear old and adjacent branches
    def _clear(self, i, j, map):
        self.state[i][j] = 0
        for t in map:
            try:
                branch_in_range = i + t[0] >= 0 and j + t[1] >= 0
                branch_not_aged = self.state[i + t[0]] [j + t[1]] < MAX_AGE            
                if branch_in_range and branch_not_aged:
                    self.state[i + t[0]] [j + t[1]] = 0
            except:
                pass

    def remove_branches (self):
        REMOVE_TEMPLATE = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(self.heigh):
            for j in range(self.width):
                if self.state[i][j] >= MAX_AGE:
                    self._clear(i, j, REMOVE_TEMPLATE)
    
    def growth(self):
        for i in range(self.heigh):
            for j in range(self.width):
                if self.state[i][j] > 0:
                    self.state[i][j] += 1
    
    def new_sprig(self):
        for i in range(self.heigh):
            for j in range(self.width):
                if self.state[i][j] == 0:
                    self.state[i][j] = 1

    def report(self):
        report = []
        for i in range(self.heigh):
            line = ''
            for j in range(self.width):
                if self.state[i][j] == 0:
                    line += '.'
                else:
                    line += '+'
            report.append(line)
        return report

def TreeOfLife(H, W, N, tree):
    tree_of_life = Tree(H, W, tree)
    for i in range(N):
        tree_of_life.growth()
        if i % DIFFERENT_YEARS == 0:
            tree_of_life.new_sprig()
        elif i % DIFFERENT_YEARS == 1:
            tree_of_life.remove_branches()
    result = tree_of_life.report()
    return result