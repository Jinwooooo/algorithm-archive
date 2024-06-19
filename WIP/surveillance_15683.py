import sys
from collections import deque
from itertools import product
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
			elif ROOM[row][col] == 0:
				surveillance_space_ctr += 1

	return arr_cctv, surveillance_space_ctr + len(arr_cctv)

def mk_observe(arr_mk_coord, cctv_coord, d):
	row, col = cctv_coord

	drow = [-1,0,1,0]
	dcol = [0,1,0,-1]

	while True:
		nrow = row + drow[d]
		ncol = col + dcol[d]

		if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
			if ROOM[nrow][ncol] == 6:
				return
			else:
				arr_mk_coord.add((nrow,ncol))
		else:
			return

		row = nrow
		col = ncol

arr_cctv, surveillance_space_ctr = get_cctv_coord()
arr_combo = list(product([0,1,2,3], repeat=len(arr_cctv)))

global_min = surveillance_space_ctr

for combo in arr_combo:
	arr_mk_coord = set()
	for row, col, _ in arr_cctv:
		arr_mk_coord.add((row, col))

	for idx in range(len(arr_cctv)):
		cctv_row, cctv_col, cctv_type = arr_cctv[idx]
		cctv_d = combo[idx]

		if cctv_type == 1:
			mk_observe(arr_mk_coord, (cctv_row, cctv_col), cctv_d)
		elif cctv_type == 2:
			mk_observe(arr_mk_coord, (cctv_row, cctv_col), cctv_d)
			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+2)%4)
		elif cctv_type == 3:
			mk_observe(arr_mk_coord, (cctv_row, cctv_col), cctv_d)
			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+1)%4)
		elif cctv_type == 4:
			mk_observe(arr_mk_coord, (cctv_row, cctv_col), cctv_d)
			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+1)%4)
			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+3)%4)
		else:
			mk_observe(arr_mk_coord, (cctv_row, cctv_col), cctv_d)
			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+1)%4)
			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+2)%4)
			mk_observe(arr_mk_coord, (cctv_row, cctv_col), (cctv_d+3)%4)

	global_min = min(global_min, surveillance_space_ctr - len(arr_mk_coord))

print(global_min)
