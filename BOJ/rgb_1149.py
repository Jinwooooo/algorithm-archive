import sys
input = sys.stdin.readline

HEIGHT = int(input().strip())
MATRIX = [list(map(int, input().strip().split(' '))) for _ in range(HEIGHT)]

for row in range(1, HEIGHT):
	for curr_col in range(3):
		MATRIX[row][curr_col] = min(MATRIX[row][curr_col] + MATRIX[row - 1][(curr_col + 1) % 3], 
									MATRIX[row][curr_col] + MATRIX[row - 1][(curr_col + 2) % 3])

print(min(MATRIX[HEIGHT - 1]))
