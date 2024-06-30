import sys
input = sys.stdin.readline

HEIGHT, WIDTH = map(int, input().strip().split(' '))
BOARD = [list(map(int, input().strip().split(' '))) for _ in range(HEIGHT)]
PARENT = [idx for idx in range(WIDTH * HEIGHT)]
DESTINATION = [1 for _ in range(WIDTH * HEIGHT)]

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
		PARENT[r1] = r2
		DESTINATION[r2] += DESTINATION[r1]
		DESTINATION[r1] = 0

def simulate(row, col):
	drow = [-1,-1,0,1,1,1,0,-1]
	dcol = [0,1,1,1,0,-1,-1,-1]

	mval, crow, ccol = BOARD[row][col], row, col

	for d in range(8):
		nrow = row + drow[d]
		ncol = col + dcol[d]

		if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
			if mval > BOARD[nrow][ncol]:
				mval, crow, ccol = BOARD[nrow][ncol], nrow, ncol

	if mval != BOARD[row][col]:
		union(coord_to_idx(row, col), coord_to_idx(crow, ccol))

for row in range(HEIGHT):
	for col in range(WIDTH):
		simulate(row, col)

for row in range(HEIGHT):
	print(' '.join(map(str, DESTINATION[row * WIDTH : (row + 1) * WIDTH])))

# import sys
# input = sys.stdin.readline

# HEIGHT, WIDTH = map(int, input().strip().split(' '))
# BOARD = [list(map(int, input().strip().split(' '))) for _ in range(HEIGHT)]
# DESTINATION = [-1 for _ in range(WIDTH * HEIGHT)]
# RESULT = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

# def coord_to_idx(row, col):
# 	return row * WIDTH + col

# def idx_to_coord(idx):
# 	return idx // WIDTH, idx % WIDTH

# def simulate(row, col):
# 	idx = coord_to_idx(row, col)
# 	if DESTINATION[idx] != -1:
# 		return

# 	stack = [(idx)]

# 	drow = [-1,-1,0,1,1,1,0,-1]
# 	dcol = [0,1,1,1,0,-1,-1,-1]

# 	while True:
# 		curr_min = BOARD[row][col]

# 		for d in range(8):
# 			nrow = row + drow[d]
# 			ncol = col + dcol[d]

# 			if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
# 				if curr_min > BOARD[nrow][ncol]:
# 					curr_min = BOARD[nrow][ncol]
# 					mrow, mcol = nrow, ncol

# 		if curr_min != BOARD[row][col]:
# 			midx = coord_to_idx(mrow, mcol)
# 			stack.append(midx)
# 			row, col = mrow, mcol
# 		else:
# 			while stack:
# 				sidx = stack.pop()
# 				DESTINATION[sidx] = coord_to_idx(row, col)
# 			return

# for row in range(HEIGHT):
# 	for col in range(WIDTH):
# 		simulate(row, col)

# for idx in DESTINATION:
# 	row, col = idx_to_coord(idx)
# 	RESULT[row][col] += 1

# for row in RESULT:
# 	print(*row)


# import sys
# input = sys.stdin.readline

# HEIGHT, WIDTH = map(int, input().strip().split(' '))
# BOARD = [list(map(int, input().strip().split(' '))) for _ in range(HEIGHT)]
# RESULT = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

# def simulate(row, col):
# 	drow = [-1,-1,0,1,1,1,0,-1]
# 	dcol = [0,1,1,1,0,-1,-1,-1]

# 	while True:
# 		curr_min = BOARD[row][col]

# 		for d in range(8):
# 			nrow = row + drow[d]
# 			ncol = col + dcol[d]

# 			if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
# 				if curr_min > BOARD[nrow][ncol]:
# 					curr_min = BOARD[nrow][ncol]
# 					mrow, mcol = nrow, ncol

# 		if curr_min != BOARD[row][col]:
# 			row, col = mrow, mcol
# 		else:
# 			RESULT[row][col] += 1
# 			break

# for row in range(HEIGHT):
# 	for col in range(WIDTH):
# 		simulate(row, col)

# for row in RESULT:
# 	print(*row)
