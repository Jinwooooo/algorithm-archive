import sys
input = sys.stdin.readline

SIZE = int(input().strip())
PETRI = list(map(int, input().strip().split(' ')))
petri_pre = []
petri_post = []

for idx in range(SIZE):
	petri_pre.append([PETRI[idx], idx+1, False])

while len(petri_pre) > 1:
	for idx in range(len(petri_pre)):
		if not petri_pre[idx][2]:
			# avoiding index out of range (special case at the start and end element)
			if idx == 0:
				if petri_pre[idx][0] >= petri_pre[idx+1][0]:
					new_size = petri_pre[idx][0] + petri_pre[idx+1][0]
					petri_post.append([new_size, petri_pre[idx][1], False])
					petri_pre[idx] = [new_size, petri_pre[idx][1], True]
					petri_pre[idx+1] = [new_size, petri_pre[idx][1], True]
			elif idx == len(petri_pre) - 1:
				if petri_pre[idx][0] >= petri_pre[idx-1][0]:
					new_size = petri_pre[idx-1][0] + petri_pre[idx][0]
					if len(petri_post) > 0:
						petri_post.pop()
					petri_post.append([new_size, petri_pre[idx][1], False])
					petri_pre[idx-1] = [new_size, petri_pre[idx][1], True]
					petri_pre[idx] = [new_size, petri_pre[idx][1], True]
				else:
					# sometimes the last element cannot merge, the element should continue the next day
					petri_post.append([petri_pre[idx][0], petri_pre[idx][1], False])
			else:
				# merge both sides
				if petri_pre[idx][0] >= petri_pre[idx-1][0] and petri_pre[idx][0] >= petri_pre[idx+1][0]:
					new_size = petri_pre[idx-1][0] + petri_pre[idx][0] + petri_pre[idx+1][0]
					if len(petri_post) > 0:
						petri_post.pop()
					petri_post.append([new_size, petri_pre[idx][1], False])
					petri_pre[idx][2] = True
					petri_pre[idx-1] = [new_size, petri_pre[idx][1], True]
					petri_pre[idx] = [new_size, petri_pre[idx][1], True]
					petri_pre[idx+1] = [new_size, petri_pre[idx][1], True]
					

				# merge left only
				if petri_pre[idx][0] >= petri_pre[idx-1][0] and petri_pre[idx][0] < petri_pre[idx+1][0]:
					new_size = petri_pre[idx-1][0] + petri_pre[idx][0]
					if len(petri_post) > 0:
						petri_post.pop()
					petri_post.append([new_size, petri_pre[idx][1], False])
					petri_pre[idx-1] = [new_size, petri_pre[idx][1], True]
					petri_pre[idx] = [new_size, petri_pre[idx][1], True]
					

				# merge right only
				if petri_pre[idx][0] < petri_pre[idx-1][0] and petri_pre[idx][0] >= petri_pre[idx+1][0]:
					new_size = petri_pre[idx][0] + petri_pre[idx+1][0]
					petri_post.append([new_size, petri_pre[idx][1], False])
					petri_pre[idx] = [new_size, petri_pre[idx][1], True]
					petri_pre[idx+1] = [new_size, petri_pre[idx][1], True]
	#		[DEBUG]		
			print(petri_pre)
			print(petri_post)	

	print('---for---')

	# swapping for next day
	petri_pre = petri_post
	petri_post = []

print(petri_pre[0][0])
print(petri_pre[0][1])



