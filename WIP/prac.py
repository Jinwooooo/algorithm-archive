# width, height = 5, 5
# matrix = [[0 for _ in range(height)] for _ in range(width)]
# all_path = []
# visited = set()

# def dfs(curr_coord, curr_path, all_path, visited, width, height, depth):
# 	if depth == 1:
# 		all_path.append(curr_path.copy())
# 		return

# 	drow = [1,-1,0,0]
# 	dcol = [0,0,1,-1]

# 	for d in range(4):
# 		nrow = curr_coord[0] + drow[d]
# 		ncol = curr_coord[1] + dcol[d]

# 		if 0 <= nrow < height and 0 <= ncol < width and (nrow,ncol) not in visited:
# 			visited.add((nrow,ncol))
# 			curr_path.append((nrow,ncol))
# 			dfs((nrow,ncol), curr_path, all_path, visited, width, height, depth + 1)
# 			curr_path.pop()
# 			visited.remove((nrow,ncol))

# dfs((2,2), [(2,2)], all_path, visited, width, height, 0)
# print(all_path)

# def get_dna(query):
# 	row, col = query
# 	stack = []

# 	col -= 1
# 	while row > 1:
# 		stack.append(col % 4)
# 		row -= 1
# 		col //= 4

# 	while len(stack) > 0:
# 		curr_idx = stack.pop()
# 		if curr_idx == 0:
# 			return 'RR'
# 		if curr_idx == 3:
# 			return 'rr'

# 	return 'Rr'

# print(get_dna([4, 26]))

# def dfs(query):
# 	row, col = query
# 	print(row, col)

# 	if row == 1:
# 		return 'Rr'

# 	col -= 1
# 	curr_idx = col % 4
# 	if curr_idx == 0:
# 		return 'RR'
# 	if curr_idx == 3:
# 		return 'rr'

# 	col += 1
# 	dfs([row - 1, col // 4])

# print(dfs([3, 9]))

# from collections import deque

# def solution(queries):
#     all_levels = [[] for _ in range(15)]
#     all_levels[0].append(('R','r'))
#     curr_level = 0
    
#     while curr_level < 12:
#         for curr_dna in all_levels[curr_level]:
#             if curr_dna == ('R','r'):
#                 all_levels[curr_level+1].append((curr_dna[0], curr_dna[0]))
#                 all_levels[curr_level+1].append(('R', 'r'))
#                 all_levels[curr_level+1].append(('R', 'r'))
#                 all_levels[curr_level+1].append((curr_dna[1], curr_dna[1]))
#             else:
#                 all_levels[curr_level+1].append((curr_dna[0], curr_dna[0]))
#                 all_levels[curr_level+1].append((curr_dna[0], curr_dna[1]))
#                 all_levels[curr_level+1].append((curr_dna[1], curr_dna[0]))
#                 all_levels[curr_level+1].append((curr_dna[1], curr_dna[1]))
#         curr_level += 1    
    
#     result = []
#     for row, col in queries:
#         result.append(''.join(all_levels[row-1][col-1]))
    
#     return result

# from copy import deepcopy
# from collections import deque

# size = 3
# temp = 'a b c'
# temp = temp.split(' ')

# curr_arr = [temp[0]] 
# all_arr = []
# leftover = deque(temp)

# def dfs(leftover, curr_arr, all_arr, size):
# 	print(curr_arr)
# 	print(leftover)
# 	if len(curr_arr) >= 3:
# 		all_arr.append(curr_arr.copy())
# 		return

# 	deep_arr = deepcopy(curr_arr)
# 	concat_elem = leftover.popleft()

# 	curr_arr.append(concat_elem)
# 	deep_arr.append(' ' + concat_elem)

# 	dfs(leftover, curr_arr, all_arr, size)
# 	dfs(leftover, deep_arr, all_arr, size)

# dfs(leftover, curr_arr, all_arr, size)
# print(all_arr)





