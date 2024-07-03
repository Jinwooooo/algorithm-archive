import sys
input = sys.stdin.readline

SIZE, NO_QUERIES = map(int, input().strip().split(' '))
MATRIX = [list(map(int, input().strip().split(' '))) for _ in range(SIZE)]

DP = [[0 for _ in range(SIZE + 1)] for _ in range(SIZE + 1)]
for row in range(1, SIZE + 1):
	for col in range(1, SIZE + 1):
		DP[row][col] = DP[row][col-1] + DP[row-1][col] - DP[row-1][col-1] + MATRIX[row-1][col-1]

result = []
for _ in range(NO_QUERIES):
	row_start, col_start, row_end, col_end = map(int, input().strip().split(' '))
	result.append(DP[row_end][col_end] - DP[row_start-1][col_end] - DP[row_end][col_start-1] + DP[row_start-1][col_start-1])

for r in result:
	print(r)
