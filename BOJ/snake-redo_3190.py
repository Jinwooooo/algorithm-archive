import sys
from collections import deque
input = sys.stdin.readline

# input 
SIZE = int(input().strip())
ARR_APPLE = [tuple(map(int, input().strip().split(' '))) for _ in range(int(input().strip()))]
ARR_MOVE = deque([tuple(map(str, input().strip().split(' '))) for _ in range(int(input().strip()))])

# simulation init var
snake_data = [1, deque([(0,0)])]

board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
for row, col in ARR_APPLE:
    board[row-1][col-1] = -1

# simulation func
def move_snake(board, snake_data):
    arr_dir = [(-1,0),(0,1),(1,0),(0,-1)]

    nrow = snake_data[1][0][0] + arr_dir[snake_data[0]][0]
    ncol = snake_data[1][0][1] + arr_dir[snake_data[0]][1]

    # [endgame cond #1] hitting the wall
    if not (0 <= nrow < SIZE and 0 <= ncol < SIZE):
        return board, [-1, []]

    # next cell has apple
    if board[nrow][ncol] == -1:
        board[nrow][ncol] = 0
        snake_data[1].appendleft((nrow,ncol))
    else:
        # simulate snake 1 tick move
        # https://www.acmicpc.net/board/view/109911 - colliding condition => head moves before the tail
        snake_data[1].appendleft((nrow,ncol))

        # [endgame cond #2] hitting itself
        if chk_duplicates(snake_data):
            return board, [-1, []]

        snake_data[1].pop()

    return board, snake_data

def chk_duplicates(snake_data):
    visited = set()

    for coord in snake_data[1]:
        if coord in visited:
            return True
        visited.add(coord)

    return False

global_ticks = 0

while ARR_MOVE:
    ticks, turn = ARR_MOVE.popleft()

    if len(ARR_MOVE) > 0:
        for _ in range(global_ticks, int(ticks)):
            board, snake_data = move_snake(board, snake_data)
            if snake_data[0] == -1:
                print(global_ticks + 1)
                exit()
            else:
                global_ticks += 1
    else:
        while True:
            if global_ticks == int(ticks):
                if turn == 'L':
                    snake_data[0] -= 1
                    if snake_data[0] == -1:
                        snake_data[0] = 3
                else:
                    snake_data[0] += 1
                    if snake_data[0] == 4:
                        snake_data[0] = 0
            board, snake_data = move_snake(board, snake_data)
            if snake_data[0] == -1:
                print(global_ticks + 1)
                exit()
            else:
                global_ticks += 1

    if turn == 'L':
        snake_data[0] -= 1
        if snake_data[0] == -1:
            snake_data[0] = 3
    else:
        snake_data[0] += 1
        if snake_data[0] == 4:
            snake_data[0] = 0
