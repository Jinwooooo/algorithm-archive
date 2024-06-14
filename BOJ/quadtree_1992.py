import sys
input = sys.stdin.readline

SIZE = int(input().strip())
MATRIX = [list(map(int, input().strip())) for _ in range(SIZE)]

def solve_quadtree(result, curr_size, row_start, row_end, col_start, col_end):
	if chk_is_same(row_start, row_end, col_start, col_end):
		result.append(MATRIX[row_start][col_start])
		return result

	new_size = curr_size // 2
	result.append('(')
	solve_quadtree(result, new_size, row_start, row_start + new_size - 1, col_start, col_start + new_size - 1)
	solve_quadtree(result, new_size, row_start, row_start + new_size - 1, col_start + new_size, col_end)
	solve_quadtree(result, new_size, row_start + new_size, row_end, col_start, col_start + new_size - 1)
	solve_quadtree(result, new_size, row_start + new_size, row_end, col_start + new_size, col_end)
	result.append(')')

	return result


def chk_is_same(row_start, row_end, col_start, col_end):
	is_same = True
	curr_val = MATRIX[row_start][col_start]

	for row in range(row_start, row_end + 1):
		for col in range(col_start, col_end + 1):
			if MATRIX[row][col] != curr_val:
				return False

	return True

result = solve_quadtree([], SIZE, 0, SIZE - 1, 0, SIZE - 1)
print(''.join(map(str, result)))
