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

# import sys
# from collections import deque
# input = sys.stdin.readline

# def calculate_index(r, c):
#     return r * W + c
    
# direction_x = [0, 1, 0, -1] # 상 우 하 좌 (시계방향)
# direction_y = [-1, 0, 1, 0]

# def is_movable(dr, dc):
#     if (0 <= dr < H and 0 <= dc < W):
#         return True
#     return False

# def solution():
#     global answer, b_count, parent

#     while queue:
#         current_r, current_c, current_d = queue.pop()
#         is_rule_b = False
#         new_direction = 0

#         if (clear_board[current_r][current_c]): # RULE_B
#             b_count += 1
#             is_rule_b = True
#             new_direction = (current_d + rule_b[current_r][current_c]) % 4

#             if (path_start_index == -1):
#                 next_index_set.clear()
#                 path_start_index = calculate_index(current_r, current_c)

#         else: # RULE_A
#             answer += (b_count + 1)
#             b_count = 0
#             clear_board[current_r][current_c] = True
#             new_direction = (current_d + rule_a[current_r][current_c]) % 4
#             path_start_index = -1

#         dr = current_r + direction_y[new_direction]
#         dc = current_c + direction_x[new_direction]

#         if (is_movable(dr, dc)):
#             if (is_rule_b):
#                 current_index = calculate_index(current_r, current_c)
#                 next_index = calculate_index(dr, dc)

#                 if (current_index != path_start_index):
#                     queue.append((dr, dc, new_direction))
#                     continue
                
#                 if (next_index in next_index_set):
#                     break
                
#                 next_index_set.add(next_index)
                
#             queue.append((dr, dc, new_direction))
#         else:
#             break

# H, W = map(int, input().split())
# R, C, D = map(int, input().split())

# clear_board = [[False for _ in range(W)] for _ in range(H)]

# path_start_index = -1
# next_index_set = set()

# rule_a = []
# rule_b = []

# for _ in range(H):
#     rule_a.append(list(map(int, str(input().rstrip()))))

# for _ in range(H):
#     rule_b.append(list(map(int, str(input().rstrip()))))

# queue = deque()
# queue.append((R, C, D))
# answer = 0
# b_count = 0

# solution()

# print(answer)

import sys
input = sys.stdin.readline

HEIGHT, WIDTH = map(int, input().strip().split(' '))
INIT_ARIS_DATA = list(map(int, input().strip().split(' ')))
ROOM_A = [list(map(int, input().strip())) for _ in range(HEIGHT)]
ROOM_B = [list(map(int, input().strip())) for _ in range(HEIGHT)]
CLEAN = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

def simulate_aris():
    curr_move = 0
    final_move = 0
    cycle_tracker = set()
    row, col, d = INIT_ARIS_DATA

    drow = [-1,0,1,0]
    dcol = [0,1,0,-1]
    
    while True:
        if not CLEAN[row][col]:
            nd = (d + ROOM_A[row][col]) % 4
        else:
            nd = (d + ROOM_B[row][col]) % 4

        nrow = row + drow[nd]
        ncol = col + dcol[nd]

        if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
            curr_move += 1

            if not CLEAN[row][col]:
                final_move = curr_move
                CLEAN[row][col] = True
                cycle_tracker.clear()
            else:
                if (nrow, ncol, nd) in cycle_tracker:
                    break
            
            cycle_tracker.add((nrow,ncol,nd))
            row, col, d = nrow, ncol, nd
        else:
            if not CLEAN[row][col]:
                curr_move += 1
                final_move = curr_move
            break

    return final_move

print(simulate_aris())


