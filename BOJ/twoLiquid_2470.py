import sys
input = sys.stdin.readline

no_liquid = int(input().strip())
arr_liquid = list(map(int, input().strip().split(' ')))
arr_liquid.sort()

# print(arr_liquid)

lp = 0
rp = len(arr_liquid) - 1

curr_min = abs(arr_liquid[lp] + arr_liquid[rp])
curr_pair_idx = [lp, rp]
# print(lp, rp)
# print(curr_min)
# print('---')

while lp < rp:
	if lp + 1 >= rp or lp >= rp - 1:
		break

	lp_move_result = abs(arr_liquid[lp+1] + arr_liquid[rp])
	rp_move_result = abs(arr_liquid[lp] + arr_liquid[rp-1])

	if lp_move_result >= rp_move_result:
		if rp_move_result < curr_min:
			curr_min = rp_move_result
			curr_pair_idx = [lp,rp-1]
		rp -= 1
	else:
		if lp_move_result < curr_min:		
			curr_min = lp_move_result
			curr_pair_idx = [lp+1,rp]
		lp += 1

	# print(lp, rp)
	# print(curr_min)
	# print('---')

# print(curr_min)
# print(curr_pair_idx)
print(arr_liquid[curr_pair_idx[0]], arr_liquid[curr_pair_idx[1]])
