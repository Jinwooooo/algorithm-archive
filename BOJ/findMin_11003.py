import sys
from collections import deque
input = sys.stdin.readline

SET_SIZE, SUBSET_SIZE = map(int, input().strip().split(' '))
ARR = list(map(int, input().strip().split(' ')))

result = []
deq = deque([])

for idx in range(SET_SIZE):
	if deq and deq[0] < idx - SUBSET_SIZE + 1:
		deq.popleft()

	while deq and ARR[deq[-1]] >= ARR[idx]:
		deq.pop()

	deq.append(idx)
	result.append(ARR[deq[0]])

print(*result)

