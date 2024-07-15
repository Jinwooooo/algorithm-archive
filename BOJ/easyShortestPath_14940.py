import sys
from collections import deque
input = sys.stdin.readline

HEIGHT, WIDTH = map(int, input().strip().split(' '))
MAP = [list(map(int, input().strip().split(' '))) for _ in range(HEIGHT)]
VISITED = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

def get_start_coord():
	for row in range(HEIGHT):
		for col in range(WIDTH):
			if MAP[row][col] == 2:
				MAP[row][col] = 0
				return row, col

def bfs(row, col):
	VISITED[row][col] = True
	queue = deque([(row,col)])

	drow = [-1,0,1,0]
	dcol = [0,1,0,-1]

	while queue:
		row, col = queue.popleft()

		for d in range(4):
			nrow = row + drow[d]
			ncol = col + dcol[d]

			if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH and not VISITED[nrow][ncol] and MAP[nrow][ncol] != 0:
				MAP[nrow][ncol] = MAP[row][col] + 1
				VISITED[nrow][ncol] = True
				queue.append((nrow,ncol))

start_row, start_col = get_start_coord()
bfs(start_row, start_col)

for row in range(HEIGHT):
		for col in range(WIDTH):
			if not VISITED[row][col] and MAP[row][col] == 1:
				MAP[row][col] = -1

for row in MAP:
	print(*row)
