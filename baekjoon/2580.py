sudoku = [list(map(int, input().split())) for i in range(9)]
global flag
flag = False


def check(k, i, j):
    # 가로줄 탐색 (i, x)
    for c in range(9):
        if k == sudoku[i][c]:
            return False
    # 세로줄 탐색 (x, j)
    for c in range(9):
        if k == sudoku[c][j]:
            return False
    # 3x3 탐색
    sector_row = (i // 3) * 3
    sector_col = (j // 3) * 3
    for c1 in range(sector_row, sector_row+3):
        for c2 in range(sector_col, sector_col+3):
            if k == sudoku[c1][c2]:
                return False
    return True


# 0을 찾아간 뒤
# 1 ~ 9의 숫자를 직접 다 넣어보며 dfs 진행
def dfs():
    global flag
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for k in range(1, 10):
                    # sudoku (i,j) 위치에서 k가 들어갔을 때 legal한지 검사
                    if check(k, i, j):
                        sudoku[i][j] = k
                        dfs()
                        if flag:
                            break
                        sudoku[i][j] = 0
                # k를 다 넣어봤는데 안되면 유망하지 않은 노드이므로 return
                return
            if flag:
                break
        if flag:
            break
    # 만약 9x9를 전부 다 돌았는데 0이 안 나옴 --> dfs 끝!
    flag = True


dfs()
for l1 in range(9):
    for l2 in range(9):
        print(sudoku[l1][l2], end=' ')
    print()

#pypy3