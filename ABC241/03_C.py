import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

# FIXME: 2/26 TLE


def check_row(row, col):
    if row > search_limit:
        return False
    count = 0
    for i in range(6):
        # print(cells[col][row+i])
        if cells[col][row + i] == '#':
            count += 1
            if count >= 4:
                return True
    return False


def check_col(row, col):
    if col > search_limit:
        return False
    count = 0
    for i in range(6):
        if cells[col + i][row] == '#':
            count += 1
            if count >= 4:
                return True
    return False


def check_diagonal(row, col):
    if row > search_limit or col > search_limit:
        return False
    count = 0
    for i in range(6):
        if cells[col + i][row + i] == '#':
            count += 1
            if count >= 4:
                return True
    return False


def check_diagonal2(row, col):
    if row < 6 or col > search_limit:
        return False
    count = 0
    for i in range(6):
        if cells[col + i][row - i] == '#':
            count += 1
            if count >= 4:
                return True
    return False


N = I()
cells = [S() for i in range(N)]
search_limit = N - 6

for row in range(N):
    for col in range(N):
        # print(f'row:{row},col:{col}')
        if check_row(row, col) or check_col(row, col) or check_diagonal(row, col) or check_diagonal2(row, col):
            print('Yes')
            sys.exit()

print('No')
