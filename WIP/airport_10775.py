import sys
input = sys.stdin.readline

NO_GATES = int(input().strip())
NO_PLANES = int(input().strip())
ARR_PLANES = []
for _ in range(NO_PLANES):
	ARR_PLANES.append(int(input().strip()))

PARENT = [idx for idx in range(NO_GATES + 1)]

def find(idx):
	if PARENT[idx] != idx:
		PARENT[idx] = find(PARENT[idx])
	return PARENT[idx]

def union(idx1, idx2):
	r1 = find(idx1)
	r2 = find(idx2)

	if r1 != r2:
		PARENT[r2] = r1

no_docking = 0
for plane in ARR_PLANES:
	if find(plane) != 0:
		union(find(plane) - 1, find(plane))
		no_docking += 1
	else:
		break

print(no_docking)


# print(PARENT)
# print([find(idx) for idx in range(NO_GATES + 1)])