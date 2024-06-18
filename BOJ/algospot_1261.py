import sys
from heapq import heappush, heappop
input = sys.stdin.readline

WIDTH, HEIGHT = map(int, input().strip().split(' '))
MAZE = [list(input().strip()) for _ in range(HEIGHT)]

def dijkstra():
	# data format = (wall_ctr, row, col)
	MAZE[0][0] = '-1'
	heap = [(0,0,0)]

	drow = [-1,1,0,0]
	dcol = [0,0,-1,1]

	while heap:
		wall_ctr, row, col = heappop(heap)

		if (row,col) == (HEIGHT-1,WIDTH-1):
			return wall_ctr

		for d in range(4):
			nrow = row + drow[d]
			ncol = col + dcol[d]
			
			if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH and MAZE[nrow][ncol] != '-1':
				if MAZE[nrow][ncol] == '1':
					heappush(heap, (wall_ctr+1,nrow,ncol))
				else:
					heappush(heap, (wall_ctr,nrow,ncol))
				MAZE[nrow][ncol] = '-1'

print(dijkstra())
