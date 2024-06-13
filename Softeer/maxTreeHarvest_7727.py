import sys
input = sys.stdin.readline

SIZE, USERS = map(int, input().strip().split(' '))
FIELD = [list(map(int, input().strip().split(' '))) for _ in range(SIZE)]
COORD_USERS = [list(map(int, input().strip().split(' '))) for _ in range(USERS)]

def get_all_paths(coord):
	all_paths = []
	visited = set()
	visited.add((coord[0],coord[1]))
	dfs(coord[0], coord[1], 0, [coord], all_paths, visited)

	return all_paths

def dfs(row, col, depth, path, all_paths, visited):
	if depth == 3:
		all_paths.append(path.copy())
		return

	drow = [1,-1,0,0]
	dcol = [0,0,1,-1]

	for d in range(4):
		nrow = row + drow[d]
		ncol = col + dcol[d]

		if 0 <= nrow < SIZE and 0 <= ncol < SIZE:
			if (nrow,ncol) not in visited:
				visited.add((nrow,ncol))
				path.append((nrow,ncol))
				dfs(nrow, ncol, depth + 1, path, all_paths, visited)
				path.pop()
				visited.remove((nrow, ncol))

def get_total_fruits(visited):
	total_fruits = 0
	for row in range(SIZE):
		for col in range(SIZE):
			if visited[row][col]:
				total_fruits += FIELD[row][col]

	return total_fruits


data = [[],[],[]]
for idx in range(USERS):
	curr_coord = (COORD_USERS[idx][0]-1, COORD_USERS[idx][1]-1)
	data[idx] = get_all_paths(curr_coord)

global_max = 0
if USERS == 1:
	for user1 in data[0]:
		visited = [[False for _ in range(SIZE)] for _ in range(SIZE)]
		for row1, col1 in user1:
			visited[row1][col1] = True
			global_max = max(global_max, get_total_fruits(visited))
elif USERS == 2:
	for user1 in data[0]:
		for user2 in data[1]:
			visited = [[False for _ in range(SIZE)] for _ in range(SIZE)]
			for row1, col1 in user1:
				visited[row1][col1] = True
			for row2, col2 in user2:
				visited[row2][col2] = True
			global_max = max(global_max, get_total_fruits(visited))
elif USERS == 3:
	for user1 in data[0]:
		for user2 in data[1]:
			for user3 in data[2]:
				visited = [[False for _ in range(SIZE)] for _ in range(SIZE)]
				for row1, col1 in user1:
					visited[row1][col1] = True
				for row2, col2 in user2:
					visited[row2][col2] = True
				for row3, col3 in user3:
					visited[row3][col3] = True
				global_max = max(global_max, get_total_fruits(visited))

print(global_max)
