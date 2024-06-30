import sys
from collections import defaultdict
input = sys.stdin.readline

RESULT = []

def find(parent, idx):
	if parent[idx] != idx:
		parent[idx] = find(parent, parent[idx])
	return parent[idx]

def union(parent, idx1, idx2):
	r1 = find(parent, idx1)
	r2 = find(parent, idx2)

	if r1 != r2:
		parent[r2] = r1

while True:
	no_samples, no_cmds = map(int, input().strip().split(' '))
	if no_samples == 0:
		break

	parent = [idx for idx in range(no_samples + 1)]
	diff = [0 for _ in range(no_samples)]

	for _ in range(no_cmds):
		cmd = list(map(str, input().strip().split(' ')))
		e1, e2 = int(cmd[1]), int(cmd[2])
		if cmd[0] == '!':
			union(parent, e1, e2)
		else:
			if find(parent, e1) != find(parent, e2):
				RESULT.append('UNKNOWN')
			else:
				RESULT.append('k')

	# print(parent)
	# print([find(parent, idx) for idx in range(no_samples + 1)])
print(RESULT)