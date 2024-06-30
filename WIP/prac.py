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

# import sys
# input = sys.stdin.readline

# HEIGHT, WIDTH = map(int, input().strip().split(' '))
# INIT_ARIS_DATA = list(map(int, input().strip().split(' ')))
# ROOM_A = [list(map(int, input().strip())) for _ in range(HEIGHT)]
# ROOM_B = [list(map(int, input().strip())) for _ in range(HEIGHT)]
# CLEAN = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

# def simulate_aris():
#     curr_move = 0
#     final_move = 0
#     cycle_tracker = set()
#     row, col, d = INIT_ARIS_DATA

#     drow = [-1,0,1,0]
#     dcol = [0,1,0,-1]
    
#     while True:
#         if not CLEAN[row][col]:
#             nd = (d + ROOM_A[row][col]) % 4
#         else:
#             nd = (d + ROOM_B[row][col]) % 4

#         nrow = row + drow[nd]
#         ncol = col + dcol[nd]

#         if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
#             curr_move += 1

#             if not CLEAN[row][col]:
#                 final_move = curr_move
#                 CLEAN[row][col] = True
#                 cycle_tracker.clear()
#             else:
#                 if (nrow, ncol, nd) in cycle_tracker:
#                     break
            
#             cycle_tracker.add((nrow,ncol,nd))
#             row, col, d = nrow, ncol, nd
#         else:
#             if not CLEAN[row][col]:
#                 curr_move += 1
#                 final_move = curr_move
#             break

#     return final_move

# print(simulate_aris())

# HEIGHT = 3
# WIDTH = 4
# ROOM_B = [[3,3,3,0],
#           [3,0,2,1],
#           [3,3,3,2]]
# CLEAN = [[True for _ in range(WIDTH)] for _ in range(HEIGHT)]

# WARP = [-1 for _ in range(HEIGHT * WIDTH * 4)]
# # COST = [0 for _ in range(HEIGHT * WIDTH * 4)]

# def compute_idx(row, col, d):
#     return (row * WIDTH + col) * 4 + d

# def update_warp_cost(stack, curr_idx):
#     update_cost = len(stack)

#     while stack:
#         update_idx = stack.pop()
#         WARP[update_idx] = curr_idx
#         # COST[update_idx] = update_cost
#         # update_cost -= 1

# def simulate_aris(coord):
#     row, col, d = coord
#     stack = []

#     drow = [-1,0,1,0]
#     dcol = [0,1,0,-1]

#     for _ in range(5):
#         if CLEAN[row][col]:
#             curr_idx = compute_idx(row,col,d)

#             if WARP[curr_idx] == -1:
#                 stack.append(curr_idx)

#                 nd = (d + ROOM_B[row][col]) % 4
#                 nrow = row + drow[nd]
#                 ncol = col + dcol[nd]
#             else:
#                 nd = ((WARP[curr_idx] % 4) + ROOM_B[row][col]) % 4
#                 nrow = WARP[curr_idx] // (WIDTH * 4) + drow[nd]
#                 ncol = ((WARP[curr_idx] // 4) % WIDTH) + dcol[nd]

#         if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
#             if not CLEAN[nrow][ncol]:
#                 update_warp_cost(stack, curr_idx)

#             row, col, d = nrow, ncol, nd
#         else:
#             break

#     update_warp_cost(stack, curr_idx)


# simulate_aris((2,1,1))
# print(WARP)
# print('*****')
# simulate_aris((1,1,1))
# print(WARP)

import sys
input = sys.stdin.readline
near = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]


def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]


def union(up, down):
    u = find(up)
    d = find(down)
    if u == d:
        return

    parents[u] = d
    rank[d] += rank[u]
    rank[u] = 0


r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
parents = list(range(r*c))
rank = [1] * r*c

for i in range(r):
    for j in range(c):

        mn, x, y = board[i][j], i, j

        
        for a, b in near:
            ni, nj = i+a, j+b
            if ni < 0 or ni >= r or nj < 0 or nj >= c:
                continue

            if mn > board[ni][nj]:
                mn, x, y = board[ni][nj], ni, nj

        if mn != board[i][j]:
            union(i*c+j, x*c+y)

print(parents)
print(rank)

for i in range(r):
    print(' '.join(map(str, rank[i*c:(i+1)*c])))






