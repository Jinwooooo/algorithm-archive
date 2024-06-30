'''
UNION-FIND by RANK solution
due to the overhead of the constant updates for PARENT/RANK structure
it is slower than the DFS solution
~1200ms for AC
'''
import sys
input = sys.stdin.readline

HEIGHT, WIDTH = map(int, input().strip().split(' '))
MAP = [list(map(str, input().strip())) for _ in range(HEIGHT)]
PARENT = [idx for idx in range(HEIGHT * WIDTH)]
RANK = [0 for _ in range(HEIGHT * WIDTH)]
DIRECT = {'U': (-1,0), 'D': (1,0), 'R': (0,1), 'L': (0,-1)}

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

for row in range(HEIGHT):
	for col in range(WIDTH):
		nrow = row + DIRECT[MAP[row][col]][0]
		ncol = col + DIRECT[MAP[row][col]][1]
		
		union(coord_to_idx(row, col), coord_to_idx(nrow, ncol))

cycle = set(find(idx) for idx in range(HEIGHT * WIDTH))
print(len(cycle))

'''
DFS solution
~500ms for AC
'''
# import sys
# input = sys.stdin.readline

# HEIGHT, WIDTH = map(int, input().strip().split(' '))
# MAP = [list(map(str, input().strip())) for _ in range(HEIGHT)]
# VISITED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
# DIRECT = {'U': (-1,0), 'D': (1,0), 'R': (0,1), 'L': (0,-1)}

# def dfs(row, col):
# 	if VISITED[row][col] == 2:
# 		return VISITED[row][col] == 2

# 	VISITED[row][col] = 1
# 	nrow = row + DIRECT[MAP[row][col]][0]
# 	ncol = col + DIRECT[MAP[row][col]][1]

# 	if not VISITED[nrow][ncol]:
# 		if dfs(nrow, ncol):
# 			VISITED[row][col] = 2
# 			return True
# 	elif VISITED[nrow][ncol] == 1:
# 		VISITED[row][col] = 2
# 		return True

# 	VISITED[nrow][ncol] = 3
# 	return False

# cycle = 0
# for row in range(HEIGHT):
# 	for col in range(WIDTH):
# 		if not VISITED[row][col]:
# 			if dfs(row, col):
# 				cycle += 1

# print(cycle)
