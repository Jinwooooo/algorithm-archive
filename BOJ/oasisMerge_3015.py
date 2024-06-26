'''
When a new height is met by using stack and multiple conditions, this solution can be solved with time complexity O(N). 
'''
import sys
input = sys.stdin.readline

SIZE = int(input().strip())
LINE = [int(input().strip()) for _ in range(SIZE)]
ARR_RESULT = [0 for _ in range(SIZE)]
STACK = []

for idx in range(SIZE):
	curr_height = LINE[idx]

	while STACK:
		if STACK[-1][0] < curr_height:
			_, stack_head_ctr = STACK.pop()
			ARR_RESULT[idx] += stack_head_ctr
		else:
			break

	if not STACK:
		STACK.append((curr_height, 1))
	else:
		if STACK[-1][0] == curr_height:
			_, stack_head_ctr = STACK.pop()
			ARR_RESULT[idx] += stack_head_ctr

			if STACK:
				ARR_RESULT[idx] += 1

			STACK.append((curr_height, stack_head_ctr + 1))
		else:
			STACK.append((curr_height, 1))
			ARR_RESULT[idx] += 1

# print(ARR_RESULT)
print(sum(ARR_RESULT))


'''
exceeds time limit because it has to compute the same calculation multiple times

e.g. if k = [2,4,1,2,2,5,1]
5 (idx=5) -> 2,2,4
2 (idx=4) -> 2,4 

2 (idx=4) is a valid subset of 5 (idx=5), so this value has to be computed only once
i.e. this solution is O(N^2)
'''
# import sys
# input = sys.stdin.readline

# SIZE = int(input().strip())
# LINE = [int(input().strip()) for _ in range(SIZE)]
# LINE.reverse()

# valid = 0

# for pivot_idx in range(SIZE):
# 	pivot_val = LINE[pivot_idx]
# 	max_val = 0

# 	for cmp_idx in range(pivot_idx + 1, SIZE):
# 		cmp_val = LINE[cmp_idx]
# 		max_val = max(cmp_val, max_val)

# 		if pivot_val < max_val:
# 			valid += 1
# 			break
# 		else:
# 			if cmp_val < max_val:
# 				continue
# 			else:
# 				valid += 1

# print(valid)
