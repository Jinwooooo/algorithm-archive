# import sys
# from collections import deque
# from itertools import product
# input = sys.stdin.readline

# HEIGHT, WIDTH = map(int, input().strip().split(' '))
# ROOM = [list(map(int, input().strip().split(' '))) for _ in range(HEIGHT)]

# def get_cctv_coord():
# 	arr_cctv = []
# 	surveillance_space_ctr = 0

# 	for row in range(HEIGHT):
# 		for col in range(WIDTH):
# 			if 0 < ROOM[row][col] < 6:
# 				arr_cctv.append((row, col, ROOM[row][col]))
# 			elif ROOM[row][col] == 0:
# 				surveillance_space_ctr += 1

# 	return arr_cctv, surveillance_space_ctr + len(arr_cctv)

# def mk_observe(arr_mk_coord, cctv_coord, d):
# 	row, col = cctv_coord

# 	drow = [-1,0,1,0]
# 	dcol = [0,1,0,-1]

# 	while True:
# 		nrow = row + drow[d]
# 		ncol = col + dcol[d]

# 		if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
# 			if ROOM[nrow][ncol] == 6:
# 				return
# 			else:
# 				arr_mk_coord.add((nrow,ncol))
# 		else:
# 			return

# 		row = nrow
# 		col = ncol

# arr_cctv, surveillance_space_ctr = get_cctv_coord()
# arr_combo = list(product([0,1,2,3], repeat=len(arr_cctv)))

# global_min = surveillance_space_ctr

# for combo in arr_combo:
# 	arr_mk_coord = set()
# 	for row, col, _ in arr_cctv:
# 		arr_mk_coord.add((row, col))

# 	for idx in range(len(arr_cctv)):
# 		cctv_row, cctv_col, cctv_type = arr_cctv[idx]
# 		cctv_d = combo[idx]

# 		if cctv_type == 1:
# 			mk_observe(arr_mk_coord, (cctv_row, cctv_col), cctv_d)
# 		elif cctv_type == 2:
# 			mk_observe(arr_mk_coord, (cctv_row, cctv_col), cctv_d)
# 			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+2)%4)
# 		elif cctv_type == 3:
# 			mk_observe(arr_mk_coord, (cctv_row, cctv_col), cctv_d)
# 			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+1)%4)
# 		elif cctv_type == 4:
# 			mk_observe(arr_mk_coord, (cctv_row, cctv_col), cctv_d)
# 			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+1)%4)
# 			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+3)%4)
# 		else:
# 			mk_observe(arr_mk_coord, (cctv_row, cctv_col), cctv_d)
# 			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+1)%4)
# 			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+2)%4)
# 			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+3)%4)

# 	global_min = min(global_min, surveillance_space_ctr - len(arr_mk_coord))

# print(global_min)

import sys
from math import inf
from itertools import product
import time
import tracemalloc
input = sys.stdin.readline

HEIGHT, WIDTH = map(int, input().strip().split(' '))
ROOM = [list(map(int, input().strip().split(' '))) for _ in range(HEIGHT)]

def get_cctv_coord():
	arr_cctv = []
	surveillance_space_ctr = 0

	for row in range(HEIGHT):
		for col in range(WIDTH):
			if 0 < ROOM[row][col] < 6:
				arr_cctv.append((row, col, ROOM[row][col]))

	return arr_cctv

def mk_observe(room, cctv_coord, d):
	row, col = cctv_coord

	drow = [-1,0,1,0]
	dcol = [0,1,0,-1]

	while True:
		nrow = row + drow[d]
		ncol = col + dcol[d]

		if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
			if room[nrow][ncol] == 6:
				return
			else:
				room[nrow][ncol] = -1
		else:
			return

		row = nrow
		col = ncol

def get_blindspot(room):
	blindspot = 0

	for row in room:
		for cell in row:
			if cell == 0:
				blindspot += 1

	return blindspot

tracemalloc.start()
start_time = time.time()
arr_cctv = get_cctv_coord()
arr_combo = list(product([0,1,2,3], repeat=len(arr_cctv)))
end_iter_time = time.time()
tracemalloc.stop()

global_min = inf
counter = 0

for combo in arr_combo:
	curr_room = [row[:] for row in ROOM]

	for idx in range(len(arr_cctv)):
		counter += 1

		cctv_row, cctv_col, cctv_type = arr_cctv[idx]
		cctv_d = combo[idx]

		if cctv_type == 1:
			mk_observe(curr_room, (cctv_row, cctv_col), cctv_d)
		elif cctv_type == 2:
			mk_observe(curr_room, (cctv_row, cctv_col), cctv_d)
			mk_observe(curr_room, (cctv_row, cctv_col), (cctv_d+2)%4)
		elif cctv_type == 3:
			mk_observe(curr_room, (cctv_row, cctv_col), cctv_d)
			mk_observe(curr_room, (cctv_row, cctv_col), (cctv_d+1)%4)
		elif cctv_type == 4:
			mk_observe(curr_room, (cctv_row, cctv_col), cctv_d)
			mk_observe(curr_room, (cctv_row, cctv_col), (cctv_d+1)%4)
			mk_observe(curr_room, (cctv_row, cctv_col), (cctv_d+3)%4)
		else:
			mk_observe(curr_room, (cctv_row, cctv_col), cctv_d)
			mk_observe(curr_room, (cctv_row, cctv_col), (cctv_d+1)%4)
			mk_observe(curr_room, (cctv_row, cctv_col), (cctv_d+2)%4)
			mk_observe(curr_room, (cctv_row, cctv_col), (cctv_d+3)%4)

	global_min = min(global_min, get_blindspot(curr_room))
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()

print(global_min)
print(counter)
print(f"Current memory usage: {current / 10**6}MB; Peak: {peak / 10**6}MB")
print(f"Time taken: {end_iter_time - start_time:.6f} seconds")
print(f"Time taken: {end_time - start_time:.6f} seconds")
