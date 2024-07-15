import sys
input = sys.stdin.readline

SIZE = int(input().strip())
PAPER = [list(map(int, input().strip().split(' '))) for _ in range(SIZE)]

dict_result = {-1 : 0, 0 : 0, 1 : 0}

def dfs(dict_result, curr_size, row_start, row_end, col_start, col_end):
	if chk_same(row_start, row_end, col_start, col_end):
		dict_result[PAPER[row_start][col_start]] += 1
		return

	new_size = curr_size // 3
	dfs(dict_result, new_size, row_start, row_start + new_size - 1, col_start, col_start + new_size - 1)
	dfs(dict_result, new_size, row_start, row_start + new_size - 1, col_start + new_size, col_start + new_size * 2 - 1)
	dfs(dict_result, new_size, row_start, row_start + new_size - 1, col_start + new_size * 2, col_end)
	dfs(dict_result, new_size, row_start + new_size, row_start + new_size * 2 - 1, col_start, col_start + new_size - 1)
	dfs(dict_result, new_size, row_start + new_size, row_start + new_size * 2 - 1, col_start + new_size, col_start + new_size * 2 - 1)
	dfs(dict_result, new_size, row_start + new_size, row_start + new_size * 2 - 1, col_start + new_size * 2, col_end)
	dfs(dict_result, new_size, row_start + new_size * 2, row_end, col_start, col_start + new_size - 1)
	dfs(dict_result, new_size, row_start + new_size * 2, row_end, col_start + new_size, col_start + new_size * 2 - 1)
	dfs(dict_result, new_size, row_start + new_size * 2, row_end, col_start + new_size * 2, col_end)

def chk_same(row_start, row_end, col_start, col_end):
	curr_val = PAPER[row_start][col_start]

	for row in range(row_start, row_end + 1):
		for col in range(col_start, col_end + 1):
			if PAPER[row][col] != curr_val:
				return False

	return True

dfs(dict_result, SIZE, 0, SIZE-1, 0, SIZE-1)
print(dict_result[-1])
print(dict_result[0])
print(dict_result[1])
