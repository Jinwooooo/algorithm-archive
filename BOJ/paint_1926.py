import sys
from collections import deque
input = sys.stdin.readline

HEIGHT, WIDTH = map(int, input().strip().split(' '))
DROW = [-1,0,1,0]
DCOL = [0,1,0,-1]

canvas = [list(map(int, input().strip().split(' '))) for _ in range(HEIGHT)]

def bfs(canvas, row, col):
	queue = deque([(row,col)])
	canvas[row][col] = 0

	painted_ctr = 1

	while queue:
		row, col = queue.popleft()

		for d in range(4):
			nrow = row + DROW[d]
			ncol = col + DCOL[d]

			if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH and canvas[nrow][ncol] != 0:
				queue.append((nrow,ncol))
				canvas[nrow][ncol] = 0
				painted_ctr += 1

	return canvas, painted_ctr

global_max = 0
unique_ctr = 0
for row in range(HEIGHT):
	for col in range(WIDTH):
		if canvas[row][col] == 1:
			unique_ctr += 1
			canvas, painted_ctr = bfs(canvas, row, col)
			global_max = max(global_max, painted_ctr)

print(unique_ctr)
print(global_max)
