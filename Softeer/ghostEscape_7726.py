import sys
from collections import deque
input = sys.stdin.readline

HEIGHT, WIDTH = map(int, input().strip().split(' '))
BOARD = [list(input().strip()) for _ in range(HEIGHT)]

def get_coord():
    coord_exit = (-1,-1)
    coord_dynamic = deque()

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if BOARD[row][col] == 'N':
                coord_dynamic.append((row,col,'N'))
            if BOARD[row][col] == 'D':
                coord_exit = (row,col)

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if BOARD[row][col] == 'G':
                coord_dynamic.append((row,col,'G'))

    return coord_exit, coord_dynamic

def bfs(coord_exit, coord_dynamic):
    erow, ecol = coord_exit
    queue = coord_dynamic

    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]

    while queue:
        row, col, piece = queue.popleft()

        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]

            if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
                if piece == 'N':
                    if nrow == erow and ncol == ecol:
                        return 'Yes'

                    if BOARD[nrow][ncol] == '.':
                        BOARD[nrow][ncol] = 'N'
                        queue.append((nrow,ncol,'N'))
                else:
                    if BOARD[nrow][ncol] != 'G':
                        BOARD[nrow][ncol] = 'G'
                        queue.append((nrow,ncol,'G'))

    return 'No'

coord_exit, coord_dynamic = get_coord()
print(bfs(coord_exit, coord_dynamic))


