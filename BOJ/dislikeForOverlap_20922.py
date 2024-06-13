import sys
from collections import defaultdict
input = sys.stdin.readline

SIZE, MAX_CONSECUTIVE = map(int, input().strip().split(' '))
SERIES = list(map(int, input().strip().split(' ')))

lp = 0
rp = 1
curr_consec = defaultdict(int)
curr_consec[SERIES[lp]] += 1

global_max = 1
curr_max = 1
curr_over_val = -1

while rp < SIZE:
	if curr_consec[SERIES[rp]] + 1 > MAX_CONSECUTIVE:
		curr_consec[SERIES[lp]] -= 1
		curr_max -= 1
		lp += 1
	else:
		curr_consec[SERIES[rp]] += 1
		curr_max += 1
		rp += 1

		global_max = max(global_max, curr_max)

print(global_max)
