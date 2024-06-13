import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

NO_SCV = int(input().strip())
ARR_SCV = list(map(int, input().strip().split(' ')))
for _ in range(3 - NO_SCV):
	ARR_SCV.append(0)
ARR_SCV = tuple(ARR_SCV)

def top_down_dp():
	all_cushion = list(permutations((9,3,1), 3))
	memo = set()
	memo.add(ARR_SCV)
	queue = deque([[ARR_SCV, 0]])	

	while queue:
		(s1,s2,s3), depth = queue.popleft()

		if [s1,s2,s3] == [0,0,0]:
			return depth

		for c1, c2, c3 in all_cushion:
			ns1 = max(s1 - c1, 0)
			ns2 = max(s2 - c2, 0)
			ns3 = max(s3 - c3, 0)

			new_arr_scv = (ns1,ns2,ns3)

			if new_arr_scv not in memo:
				memo.add(new_arr_scv)
				queue.append([new_arr_scv, depth + 1])

print(top_down_dp())
