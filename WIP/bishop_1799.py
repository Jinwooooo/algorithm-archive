'''
naive solution
goes through all possible choices
time complexity is O(2^(N^2))
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

SIZE = int(input().strip())
BOARD = [list(map(int, input().strip().split(' '))) for _ in range(SIZE)]

def is_safe(row, col, arr_bishops):
	for orow, ocol in arr_bishops:
		if abs(orow - row) == abs(ocol - col):
			return False
	return True

def dfs(board, arr_bishops, row, col, max_bishops):
	if col == SIZE:
		col = 0
		row += 1

	if row == SIZE:
		return max(max_bishops, len(arr_bishops))

	max_bishops = dfs(board, arr_bishops, row, col + 1, max_bishops)

	if SIZE * SIZE - (row * SIZE + col) + len(arr_bishops) <= max_bishops:
		return max_bishops

	if board[row][col] == 1 and is_safe(row, col, arr_bishops):
		arr_bishops.add((row,col))
		max_bishops = dfs(board, arr_bishops, row, col + 1, max_bishops)
		arr_bishops.remove((row,col))	

	return max_bishops

arr_bishops = set()
print(dfs(BOARD, arr_bishops, 0, 0, 0))

'''
Recursion with pruning with additional upper bound heuristics
time complexity is O(N^3)
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

SIZE = int(input().strip())
BOARD = [list(map(int, input().strip().split(' '))) for _ in range(SIZE)]

# Initialize diagonal states
rd = [0] * (2 * SIZE - 1)  # Right-down diagonals (x - y)

def in_range(y, x):
	return 0 <= y < SIZE and 0 <= x < SIZE

def calculate_upper_bound(diag, arr_bishops):
	upper_bound = 0
	for d in range(diag, 2 * SIZE - 1):
		for y in range(d + 1):
			x = d - y
			if in_range(y, x) and BOARD[y][x] and rd[x - y + SIZE - 1] == 0:
				upper_bound += 1
				break
	return upper_bound

def dfs(board, arr_bishops, diag, max_bishops):
	global max_found

	if diag == 2 * SIZE - 1:
		max_found = max(max_found, len(arr_bishops))
		return max_found

	# Calculate upper bound and prune
	ub = calculate_upper_bound(diag, arr_bishops)
	if len(arr_bishops) + ub <= max_found:
		return max_found

	# Try placing a bishop at each valid (row, col) on the current diagonal
	for y in range(diag + 1):
		x = diag - y
		if in_range(y, x) and board[y][x] == 1 and rd[x - y + SIZE - 1] == 0:
			arr_bishops.add((y, x))
			rd[x - y + SIZE - 1] = 1
			max_bishops = dfs(board, arr_bishops, diag + 1, max_bishops)
			arr_bishops.remove((y, x))
			rd[x - y + SIZE - 1] = 0

	# Consider not placing any bishop on this diagonal
	max_bishops = dfs(board, arr_bishops, diag + 1, max_bishops)
	return max_bishops

arr_bishops = set()
max_found = 0
print(dfs(BOARD, arr_bishops, 0, 0))

'''
reduces the problem into a "Bipartite Graph Matching Problem"
aka. utilizes Hungarian Algorithm/Hopcroft-Karp Algorithm
time complexity is O(N^(5/2))
'''
import sys
input = sys.stdin.readline

def dfs(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or dfs(C[x]):
            C[x] = n
            return True

    return False


N = int(input())
board = [[0] * (N+1)]
for _ in range(N):
	board.append([0] + list(map(int, input().split())))

A, B = [[0] * (N+1) for _ in range(N+1)], [[0] * (N+1) for _ in range(N+1)]

n = 1
for s in range(2, 2*N+1):
	for i in range(1, N+1):
		j = s - i
		if i >= 1 and i <= N and j >= 1 and j <= N:
			A[i][j] = n
	n += 1

n = 1
for s in range(-N+1, N):
	for i in range(1, N+1):
		j = s + i
		if i >= 1 and i <= N and j >= 1 and j <= N:
			B[i][j] = n
	n += 1

G = [[] for _ in range(n+1)]
C = [0] * (n+1)
for i in range(1, N+1):
	for j in range(1, N+1):
		if board[i][j]:
			G[A[i][j]].append(B[i][j])

ans = 0
for i in range(1, n+1):
	V = [0] * (n+1)
	if dfs(i):
		ans += 1

print(ans)

