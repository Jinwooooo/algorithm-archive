import sys
input = sys.stdin.readline

VER_PATTERN = int(input().strip())
LENGTH = int(input().strip())
STRING = list(input().strip())

pivot, lp, rp = 0, 0, 0

for idx in range(LENGTH):
	if STRING[idx] == 'I':
		pivot = idx
		lp = pivot + 1
		rp = pivot + 2
		break

result = 0
oi_ctr = 0

while rp < LENGTH:
	curr = STRING[lp]
	nxt = STRING[rp]

	if curr == 'O' and nxt == 'I':
		oi_ctr += 1
		lp = rp + 1
		rp = lp + 1
	else:
		valid = oi_ctr - VER_PATTERN + 1
		if valid > 0:
			result += valid

		pivot = lp
		while pivot < LENGTH:
			if STRING[pivot] == 'I':
				oi_ctr = 0
				lp = pivot + 1
				rp = pivot + 2
				break
			pivot += 1

valid = oi_ctr - VER_PATTERN + 1
if valid > 0:
	result += valid

print(result)


# pattern = ['I']
# extend = 'OI'
# for i in range(VER_PATTERN):
# 	pattern.append(extend)
# pattern = list(''.join(map(str, pattern)))

# result = 0
# for idx in range(LENGTH):
# 	if idx + len(pattern) > LENGTH:
# 		break
	
# 	is_valid = True
# 	pat_idx = 0
# 	for str_idx in range(idx, idx + len(pattern)):
# 		if STRING[str_idx] != pattern[pat_idx]:
# 			is_valid = False
# 			break
# 		pat_idx += 1

# 	if is_valid:
# 		result += 1

# print(result)