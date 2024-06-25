import sys
from collections import deque
input = sys.stdin.readline

START, END = map(int, input().strip().split(' '))

def bfs(start):
	queue = deque([(start, 1)])

	while queue:
		curr, depth = queue.popleft()

		if curr == END:
			return depth

		if curr * 2 <= END:
			queue.append((curr * 2, depth + 1))

		if curr * 10 + 1 <= END:
			queue.append((curr * 10 + 1, depth + 1))

	return -1

if START == END:
	print(1)
elif START > END:
	print(-1)
else:
	print(bfs(START))

