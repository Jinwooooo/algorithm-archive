import sys
from collections import deque
input = sys.stdin.readline

HEIGHT, WIDTH = map(int, input().strip().split(' '))
LAKE = [list(map(str, input().strip())) for _ in range(HEIGHT)]
VISITED = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]
PARENT = [idx for idx in range(WIDTH * HEIGHT)]
RANK = [0 for _ in range(WIDTH * HEIGHT)]
SWAN_IDX = []

DROW = [-1,0,1,0]
DCOL = [0,1,0,-1]

def coord_to_idx(row, col):
	return row * WIDTH + col

def find(idx):
	if PARENT[idx] != idx:
		PARENT[idx] = find(PARENT[idx])
	return PARENT[idx]

def union(idx1, idx2):
	r1 = find(idx1)
	r2 = find(idx2)

	if r1 != r2:
		if RANK[r1] > RANK[r2]:
			PARENT[r2] = r1
		elif RANK[r1] < RANK[r2]:
			PARENT[r1] = r2
		else:
			PARENT[r2] = r1
			RANK[r1] += 1

def init(arr_ice_coord, arr_water_coord):
	for row in range(HEIGHT):
		for col in range(WIDTH):
			if LAKE[row][col] == 'L':
				LAKE[row][col] = '.'
				SWAN_IDX.append(coord_to_idx(row, col))
				arr_water_coord.append((row,col))
			elif LAKE[row][col] == '.':
				arr_water_coord.append((row,col))

	while arr_water_coord:
		row, col = arr_water_coord.popleft()
		idx1 = coord_to_idx(row, col)
		PARENT[idx1] = idx1

		for d in range(4):
			nrow = row + DROW[d]
			ncol = col + DCOL[d]

			if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
				if LAKE[nrow][ncol] == '.':
					idx2 = coord_to_idx(nrow, ncol)
					union(idx1, idx2)
				else:
					if not VISITED[nrow][ncol]:
						VISITED[nrow][ncol] = True
						arr_ice_coord.append((nrow,ncol))
	

def simulate_tick(arr_ice_coord, arr_water_coord):
	arr_next_coord = []

	while arr_ice_coord:
		row, col = arr_ice_coord.pop()

		for d in range(4):
			nrow = row + DROW[d]
			ncol = col + DCOL[d]

			if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH and LAKE[nrow][ncol] == '.':
				arr_water_coord.append((row,col))
				break

	while arr_water_coord:
		row, col = arr_water_coord.popleft()
		idx1 = coord_to_idx(row, col)
		PARENT[idx1] = idx1
		LAKE[row][col] = '.'

		for d in range(4):
			nrow = row + DROW[d]
			ncol = col + DCOL[d]

			if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
				if LAKE[nrow][ncol] == '.':
					idx2 = coord_to_idx(nrow, ncol)
					union(idx1, idx2)
				else:
					if not VISITED[nrow][ncol]:
						VISITED[nrow][ncol] = True
						arr_next_coord.append((nrow,ncol))

	return arr_next_coord

arr_ice_coord = deque([])
arr_water_coord = deque([])
day = 0

init(arr_ice_coord, arr_water_coord)

while find(SWAN_IDX[0]) != find(SWAN_IDX[1]):
	arr_ice_coord = simulate_tick(arr_ice_coord, arr_water_coord)
	day += 1

print(day)
