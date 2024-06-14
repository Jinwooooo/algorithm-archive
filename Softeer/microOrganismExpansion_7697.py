"""
INITIAL ATTEMPT
Tried to impl QUEUE logic w/ just pointers instead of built-in data structure
After trying to keep working on with QUEUE logic, found out that in cases like
6
4 1 5 2 3 6
made my current logic flawed, instead of trying to make my current framework work,
perhaps solving the problem with a built-in data structure would be more beneficial (logic + debugging more easier)
"""
# import sys
# input = sys.stdin.readline

# SIZE = int(input().strip())
# PETRI = list(map(int, input().strip().split(' ')))
# petri_pre = []
# petri_post = []

# for idx in range(SIZE):
# 	petri_pre.append([PETRI[idx], idx+1, False])

# while len(petri_pre) > 1:
# 	for idx in range(len(petri_pre)):
# 		if not petri_pre[idx][2]:
# 			# avoiding index out of range (special case at the start and end element)
# 			if idx == 0:
# 				if petri_pre[idx][0] >= petri_pre[idx+1][0]:
# 					new_size = petri_pre[idx][0] + petri_pre[idx+1][0]
# 					petri_post.append([new_size, petri_pre[idx][1], False])
# 					petri_pre[idx] = [new_size, petri_pre[idx][1], True]
# 					petri_pre[idx+1] = [new_size, petri_pre[idx][1], True]
# 			elif idx == len(petri_pre) - 1:
# 				if petri_pre[idx][0] >= petri_pre[idx-1][0]:
# 					new_size = petri_pre[idx-1][0] + petri_pre[idx][0]
# 					if len(petri_post) > 0:
# 						petri_post.pop()
# 					petri_post.append([new_size, petri_pre[idx][1], False])
# 					petri_pre[idx-1] = [new_size, petri_pre[idx][1], True]
# 					petri_pre[idx] = [new_size, petri_pre[idx][1], True]
# 				else:
# 					# sometimes the last element cannot merge, the element should continue the next day
# 					petri_post.append([petri_pre[idx][0], petri_pre[idx][1], False])
# 			else:
# 				# merge both sides
# 				if petri_pre[idx][0] >= petri_pre[idx-1][0] and petri_pre[idx][0] >= petri_pre[idx+1][0]:
# 					new_size = petri_pre[idx-1][0] + petri_pre[idx][0] + petri_pre[idx+1][0]
# 					if len(petri_post) > 0:
# 						petri_post.pop()
# 					petri_post.append([new_size, petri_pre[idx][1], False])
# 					petri_pre[idx][2] = True
# 					petri_pre[idx-1] = [new_size, petri_pre[idx][1], True]
# 					petri_pre[idx] = [new_size, petri_pre[idx][1], True]
# 					petri_pre[idx+1] = [new_size, petri_pre[idx][1], True]
					

# 				# merge left only
# 				if petri_pre[idx][0] >= petri_pre[idx-1][0] and petri_pre[idx][0] < petri_pre[idx+1][0]:
# 					new_size = petri_pre[idx-1][0] + petri_pre[idx][0]
# 					if len(petri_post) > 0:
# 						petri_post.pop()
# 					petri_post.append([new_size, petri_pre[idx][1], False])
# 					petri_pre[idx-1] = [new_size, petri_pre[idx][1], True]
# 					petri_pre[idx] = [new_size, petri_pre[idx][1], True]
					

# 				# merge right only
# 				if petri_pre[idx][0] < petri_pre[idx-1][0] and petri_pre[idx][0] >= petri_pre[idx+1][0]:
# 					new_size = petri_pre[idx][0] + petri_pre[idx+1][0]
# 					petri_post.append([new_size, petri_pre[idx][1], False])
# 					petri_pre[idx] = [new_size, petri_pre[idx][1], True]
# 					petri_pre[idx+1] = [new_size, petri_pre[idx][1], True]
# 	#		[DEBUG]		
# 			print(petri_pre)
# 			print(petri_post)	

# 	print('---for---')

# 	# swapping for next day
# 	petri_pre = petri_post
# 	petri_post = []

# print(petri_pre[0][0])
# print(petri_pre[0][1])

"""
SECOND ATTEMPT
After using queue and stack built-in data structure, solve the problem within 20 minutes :D
- increases readability as well :)
"""

import sys
from collections import deque
input = sys.stdin.readline

SIZE = int(input().strip())
PETRI = list(map(int, input().strip().split(' ')))
petri_pre = deque()
petri_post = []

for idx in range(SIZE):
	petri_pre.append([PETRI[idx], idx + 1])

while len(petri_pre) > 1:
	while petri_pre:
		org_size, org_idx = petri_pre.popleft()

		# general case (micro organism exist right and left)
		if len(petri_pre) > 0 and len(petri_post) > 0:
			new_size = org_size
			r_size, r_idx = petri_pre.popleft()
			l_size, l_idx = petri_post.pop()

			if org_size >= r_size:
				new_size += r_size
			else:
				petri_pre.appendleft([r_size, r_idx])

			if org_size >= l_size:
				new_size += l_size
			else:
				petri_post.append([l_size, l_idx])

			petri_post.append([new_size, org_idx])
		# special case (micro organism does not exist on left)
		elif len(petri_pre) > 0 and len(petri_post) <= 0:
			new_size = org_size
			r_size, r_idx = petri_pre.popleft()

			if org_size >= r_size:
				new_size += r_size
			else:
				petri_pre.appendleft([r_size, r_idx])

			petri_post.append([new_size, org_idx])
		# special case (micro organism does not exist on right)
		elif len(petri_pre) <= 0 and len(petri_post) > 0:
			new_size = org_size
			l_size, l_idx = petri_post.pop()

			if org_size >= l_size:
				new_size += l_size
			else:
				petri_post.append([l_size, l_idx])

			petri_post.append([new_size, org_idx])

		# print(petri_pre)
		# print(petri_post)

	petri_pre = deque(petri_post)
	petri_post = []

print(petri_pre[0][0])
print(petri_pre[0][1])


