import sys
from collections import deque
input = sys.stdin.readline

SIZE = int(input().strip())
GRID = [list(input().strip()) for _ in range(SIZE)]
DROW = [-1,0,1,0]
DCOL = [0,1,0,-1]

def bfs(visited, row, col, is_colorblind):
	curr_color = GRID[row][col]
	queue = deque([(row,col)])
	visited[row][col] = True

	while queue:
		row, col = queue.popleft()

		for d in range(4):
			nrow = row + DROW[d]
			ncol = col + DCOL[d]

			if 0 <= nrow < SIZE and 0 <= ncol < SIZE and not visited[nrow][ncol]:
				if not is_colorblind:
					if GRID[nrow][ncol] == curr_color:
						queue.append((nrow,ncol))
						visited[nrow][ncol] = True
				else:
					if curr_color == 'R' or curr_color == 'G':
						if GRID[nrow][ncol] == 'R' or GRID[nrow][ncol] == 'G':
							queue.append((nrow,ncol))
							visited[nrow][ncol] = True
					else:
						if GRID[nrow][ncol] == curr_color:
							queue.append((nrow,ncol))
							visited[nrow][ncol] = True

	return visited

normal_visited = [[False for _ in range(SIZE)] for _ in range(SIZE)]
normal_set = 0

for row in range(SIZE):
	for col in range(SIZE):
		if not normal_visited[row][col]:
			normal_visited = bfs(normal_visited, row, col, False)
			normal_set +=1

colorblind_visited = [[False for _ in range(SIZE)] for _ in range(SIZE)]
colorblind_set = 0

for row in range(SIZE):
	for col in range(SIZE):
		if not colorblind_visited[row][col]:
			colorblind_visited = bfs(colorblind_visited, row, col, True)
			colorblind_set += 1

print(normal_set, colorblind_set)
