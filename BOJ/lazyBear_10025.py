import sys
input = sys.stdin.readline

no_bucket, max_reach = map(int, input().strip().split(' '))
arr_ice = [-1] + [0 for _ in range(10**6)]
max_idx = 0
for _ in range(no_bucket):
	ice, idx = map(int, input().strip().split(' '))
	max_idx = max(max_idx, idx)
	arr_ice[idx] = ice

def solve_lazy_bear(max_reach, arr_ice, max_idx):
	lp = 1
	rp = lp + max_reach * 2
	if rp >= max_idx:
		return sum(arr_ice)
	curr_ice = sum(arr_ice[lp:rp+1])
	max_ice = curr_ice

	while rp < max_idx:
		lp += 1
		rp += 1

		curr_ice = curr_ice - arr_ice[lp-1] + arr_ice[rp]
		max_ice = max(max_ice, curr_ice)
		
	return max_ice

print(solve_lazy_bear(max_reach, arr_ice, max_idx))