import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def insert(tree, path):
	if len(path) == 0:
		return

	curr_vertex = path.popleft()
	if path:
		tree[curr_vertex].append(path[0])

	insert(tree, path)

	# if path[0] not in tree:
	# 	tree[path[0]] = defaultdict()

	# add(tree[path[0]], path[1:])


for _ in range(int(input().strip())):
	path = deque(list(map(str, input().strip().split(' ')))[1:])
	tree = defaultdict(defaultdict)

	insert(tree, path)

print(tree)