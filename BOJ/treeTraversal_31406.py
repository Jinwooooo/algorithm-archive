import sys
input = sys.stdin.readline

NO_FOLDER, NO_CMD = map(int, input().strip().split(' '))
ARR_FOLDER = [[]] + [list(map(int, input().strip().split(' ')))[1:] for _ in range(NO_FOLDER)]
ARR_CMD = [list(map(str, input().strip().split(' '))) for _ in range(NO_CMD)]

def dfs(curr_order, arr_toggle_cond, curr_folder, depth):
	curr_order.append(curr_folder)

	for lower_folder in ARR_FOLDER[curr_folder]:
		if arr_toggle_cond[lower_folder]:
			dfs(curr_order, arr_toggle_cond, lower_folder, depth + 1)

# initializing
cursor = 1
result = []
arr_toggle_cond = [False, True] + [False for _ in range(NO_FOLDER - 1)]
for folder in ARR_FOLDER[1]:
	arr_toggle_cond[folder] = True
curr_order = []
dfs(curr_order, arr_toggle_cond, 1, 0)

for cmd in ARR_CMD:
	if cmd[0] == 'toggle':
		arr_open_folder = ARR_FOLDER[curr_order[cursor]]

		for open_folder in arr_open_folder:
			arr_toggle_cond[open_folder] = not arr_toggle_cond[open_folder]

		curr_order = []
		dfs(curr_order, arr_toggle_cond, 1, 0)
	else:
		_, move = cmd

		# special case when the move goes below or over the valid index
		cursor += int(move)
		if cursor < 1:
			cursor = 1
		if cursor >= len(curr_order):
			cursor = len(curr_order) - 1

		result.append(curr_order[cursor])

for r in result:
	print(r)
