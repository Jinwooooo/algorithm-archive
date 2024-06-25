import sys
from collections import deque
input = sys.stdin.readline

HEIGHT, WIDTH = map(int, input().strip().split(' '))
CAVE = [list(input().strip()) for _ in range(HEIGHT)]
NO_THROWS = int(input().strip())
ARR_THROWS = list(map(int, input().strip().split(' ')))

def bfs_bot_mineral(visited, arr_coord, coord):
	queue = deque([(coord[0], coord[1])])
	visited[coord[0]][coord[1]] = True

	drow = [1,-1,0,0]
	dcol = [0,0,1,-1]

	while queue:
		row, col = queue.popleft()

		for d in range(4):
			nrow = row + drow[d]
			ncol = col + dcol[d]

			if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
				if CAVE[nrow][ncol] == 'x' and not visited[nrow][ncol]:
					queue.append((nrow,ncol))
					visited[nrow][ncol] = True
					arr_coord.append((nrow,ncol))

	return visited, arr_coord

def bfs_floating_mineral(visited, coord):
	arr_coord = [(coord[0], coord[1])]

	queue = deque([(coord[0], coord[1])])
	visited[coord[0]][coord[1]] = True

	drow = [1,-1,0,0]
	dcol = [0,0,1,-1]

	while queue:
		row, col = queue.popleft()

		for d in range(4):
			nrow = row + drow[d]
			ncol = col + dcol[d]

			if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
				if CAVE[nrow][ncol] == 'x' and not visited[nrow][ncol]:
					queue.append((nrow,ncol))
					visited[nrow][ncol] = True
					arr_coord.append((nrow,ncol))

	return visited, arr_coord

def chk_floating_mineral(visited, coord):
	arr_coord = []

	drow = [-1,0,0,1]
	dcol = [0,1,-1,0]

	row, col = coord[0], coord[1]

	for d in range(4):
		nrow = row + drow[d]
		ncol = col + dcol[d]

		if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
			if CAVE[nrow][ncol] == 'x' and not visited[nrow][ncol]:
				arr_coord.append((nrow,ncol))

	return arr_coord

def simulate_destroy(throw_h, throw_d):
	row = HEIGHT - throw_h

	if throw_d % 2:
		for col in range(WIDTH):
			if CAVE[row][col] == 'x':
				CAVE[row][col] = '.'
				return row, col
	else:
		for col in range(WIDTH - 1, -1, -1):
			if CAVE[row][col] == 'x':
				CAVE[row][col] = '.'
				return row, col

	return -1, -1

def simulate_float_land(arr_bot_coord, arr_float_coord):
	arr_new_float_coord = simulate_float_fall(arr_bot_coord, arr_float_coord)

	for row, col in arr_float_coord:
		CAVE[row][col] = '.'
	for row, col in arr_new_float_coord:
		CAVE[row][col] = 'x'

def simulate_float_fall(arr_bot_coord, arr_float_coord):
	if max(row for row, _ in arr_float_coord) < HEIGHT - 1:
		arr_new_float_coord = [(row+1, col) for row, col in arr_float_coord]
		if not any(elem in arr_bot_coord for elem in arr_new_float_coord):
			return simulate_float_fall(arr_bot_coord, arr_new_float_coord)
		else:
			return arr_float_coord
	else:
		return arr_float_coord


for curr_throw in range(NO_THROWS):
	destroyed_coord = simulate_destroy(ARR_THROWS[curr_throw], curr_throw)
	visited = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]
	arr_bot_coord = []

	if destroyed_coord[0] != -1:
		for col in range(WIDTH):
			if CAVE[HEIGHT-1][col] == 'x' and not visited[HEIGHT-1][col]:
				visited, arr_bot_coord = bfs_bot_mineral(visited, arr_bot_coord, (HEIGHT-1,col))
		arr_float_point_coord = chk_floating_mineral(visited, destroyed_coord)
		
		while arr_float_point_coord:
			curr_float_point_coord = arr_float_point_coord.pop()

			visited, curr_arr_float_coord = bfs_floating_mineral(visited, curr_float_point_coord)
			simulate_float_land(arr_bot_coord, curr_arr_float_coord)

			for test_float_point_coord in arr_float_point_coord:
				if test_float_point_coord in curr_arr_float_coord:
					arr_float_point_coord.remove(test_float_point_coord)

for row in CAVE:
	print(''.join(row))



