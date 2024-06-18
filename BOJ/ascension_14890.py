import sys
input = sys.stdin.readline

SIZE, LIMIT = map(int, input().strip().split(' '))
FIELD = [list(map(int, input().strip().split(' '))) for _ in range(SIZE)]

def chk_ascension_validity(arr):
	mod_arr = [[val, False] for val in arr]

	for _ in range(2):
		lp = 0
		rp = 1

		while rp < SIZE:
			if mod_arr[lp][0] == mod_arr[rp][0]:
				lp += 1
				rp += 1
			else:
				if mod_arr[lp][0] - mod_arr[rp][0] == -1:
					lp += 1
					rp += 1
				elif mod_arr[lp][0] - mod_arr[rp][0] == 1:
					if lp + LIMIT >= SIZE:
						return False
					else:
						new_height = mod_arr[rp][0]

						for idx in range(rp, lp + LIMIT + 1):
							if new_height == mod_arr[idx][0] and not mod_arr[idx][1]:
								mod_arr[idx][1] = True
							else:
								return False

						lp = lp + LIMIT
						rp = lp + 1
				else:
					return False

		mod_arr.reverse()

	return True

valid_ctr = 0
for row in FIELD:
	if chk_ascension_validity(row):
		valid_ctr += 1

for col in list(zip(*FIELD)):
	if chk_ascension_validity(col):
		valid_ctr += 1

print(valid_ctr)


# import sys
# input = sys.stdin.readline

# # SIZE = 8
# # LIMIT = 2
# # test0 = [2,2,2,2,2,2,2,2]
# # test1 = [1,1,1,2,2,1,1,1]
# # test2 = [4,3,3,2,2,1,1,1]
# # test3 = [1,1,2,2,3,3,3,4]
# # test4 = [4,3,3,2,2,2,1,1]

# def chk_ascension_validity(arr):
# 	mod_arr = [[val, False] for val in arr]

# 	for _ in range(2):
# 		lp = 0
# 		rp = 1

# 		while rp < SIZE:
# 			if mod_arr[lp][0] == mod_arr[rp][0]:
# 				lp += 1
# 				rp += 1
# 			else:
# 				if mod_arr[lp][0] - mod_arr[rp][0] == -1:
# 					# print('need opposite')
# 					# print(lp, rp)
# 					lp += 1
# 					rp += 1
# 				elif mod_arr[lp][0] - mod_arr[rp][0] == 1:
# 					# print('modify')
# 					if lp + LIMIT >= SIZE:
# 						# print('out of bounds')
# 						return False, mod_arr
# 					else:
# 						new_height = mod_arr[rp][0]
# 						for idx in range(rp, lp + LIMIT + 1):
# 							if new_height == mod_arr[idx][0] and not mod_arr[idx][1]:
# 								mod_arr[idx][1] = True
# 							else:
# 								# print('not consistent, abort')
# 								# print(lp, rp)
# 								# print(mod_arr)
# 								return False, mod_arr
# 						lp = lp + LIMIT
# 						rp = lp + 1
# 				else:
# 					# print('too high, abort')
# 					return False, mod_arr
# 		# print('left -> right')
# 		# print(mod_arr)

# 		mod_arr.reverse()

# 	return True, mod_arr


