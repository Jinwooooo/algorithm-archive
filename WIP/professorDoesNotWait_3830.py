import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

RESULT = []

def find(parent, dist, idx):
	if parent[idx] != idx:
		o_idx = parent[idx]
		parent[idx] = find(parent, dist, parent[idx])
		dist[idx] += dist[o_idx]
	return parent[idx]

def union(parent, dist, idx1, idx2, weight):
	r1 = find(parent, dist, idx1)
	r2 = find(parent, dist, idx2)

	if r1 != r2:
		parent[r1] = r2
		dist[r1] = dist[idx2] + weight - dist[idx1]

while True:
	no_samples, no_cmds = map(int, input().strip().split(' '))
	if no_samples == 0:
		break

	parent = [idx for idx in range(no_samples + 1)]
	dist = [0 for _ in range(no_samples + 1)]

	for _ in range(no_cmds):
		cmd = list(map(str, input().strip().split(' ')))
		idx1, idx2 = int(cmd[1]), int(cmd[2])
		if cmd[0] == '!':
			w = int(cmd[3])
			union(parent, dist, idx1, idx2, w)
		else:
			if find(parent, dist, idx1) != find(parent, dist, idx2):
				RESULT.append('UNKNOWN')
			else:
				RESULT.append(dist[idx1] - dist[idx2])

for r in RESULT:
	print(r)

