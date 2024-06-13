import sys
input = sys.stdin.readline

arr_size, sum_size = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split(' '))) + [0]

lp = 0
rp = 1

sum_ctr = 0
curr_sum = arr[lp]

while rp < arr_size + 1:
	if curr_sum < sum_size:
		curr_sum += arr[rp]
		rp += 1
	elif curr_sum == sum_size:
		sum_ctr += 1
		curr_sum -= arr[lp]
		lp += 1
	else:
		curr_sum -= arr[lp]
		lp += 1

print(sum_ctr)




