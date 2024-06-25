import sys
from collections import deque
input = sys.stdin.readline

HEIGHT, WIDTH = map(int, input().strip().split(' '))
MAZE = [list(map(int, input().strip())) for _ in range(HEIGHT)]
VISITED_0 = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]
VISITED_1 = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

def bfs():
	queue = deque([(0,0,1,False)])
	VISITED_0[0][0] = True
	VISITED_1[0][0] = True

	while queue:
		row, col, dist, status = queue.popleft()

		if row == HEIGHT -1 and col == WIDTH - 1:
			return dist

		drow = [-1,0,1,0]
		dcol = [0,1,0,-1]

		for d in range(4):
			nrow = row + drow[d]
			ncol = col + dcol[d]

			if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
				if MAZE[nrow][ncol] == 0 and not VISITED_0[nrow][ncol] and not status:
					queue.append((nrow,ncol,dist+1,False))
					VISITED_0[nrow][ncol] = True
				elif MAZE[nrow][ncol] == 0 and not VISITED_1[nrow][ncol] and status:
					queue.append((nrow,ncol,dist+1,True))
					VISITED_1[nrow][ncol] = True
				elif MAZE[nrow][ncol] == 1 and not VISITED_1[nrow][ncol] and not status:
					queue.append((nrow,ncol,dist+1,True))
					VISITED_1[nrow][ncol] = True

	return -1

print(bfs())

# import sys
# from math import inf
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# HEIGHT, WIDTH = map(int, input().strip().split(' '))
# MAZE = [list(map(int, input().strip())) for _ in range(HEIGHT)]
# MAZE[0][0] = -1

# def dfs(maze, data, curr_depth, min_depth):
# 	row, col, status = data

# 	if row == HEIGHT -1 and col == WIDTH - 1:
# 		return min(min_depth, curr_depth)

# 	drow = [-1,0,1,0]
# 	dcol = [0,1,0,-1]

# 	for d in range(4):
# 		nrow = row + drow[d]
# 		ncol = col + dcol[d]

# 		if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH and maze[nrow][ncol] != -1:
# 			if maze[nrow][ncol] == 0:
# 				next_maze = [row[:] for row in maze]
# 				next_maze[nrow][ncol] = -1
# 				if status:
# 					min_depth = dfs(next_maze, (nrow,ncol,True), curr_depth + 1, min_depth)
# 				else:
# 					min_depth = dfs(next_maze, (nrow,ncol,False), curr_depth + 1, min_depth)
# 			else:
# 				if not status:
# 					next_maze = [row[:] for row in maze]
# 					next_maze[nrow][ncol] = -1
# 					min_depth = dfs(next_maze, (nrow,ncol,True), curr_depth + 1, min_depth)

# 	return min_depth

# print(dfs(MAZE, (0,0,False), 1, inf))

