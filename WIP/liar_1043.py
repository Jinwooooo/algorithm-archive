import sys
input = sys.stdin.readline

no_ppl, no_party = map(int, input().strip().split(' '))
arr_know = list(map(int, input().strip().split(' ')))
arr_party = [list(map(int, input().strip().split(' ')))[1:] for _ in range(no_party)]
parent = [idx for idx in range(no_ppl + 1)]

def find(parent, idx):
	if parent[idx] != idx:
		parent[idx] = find(parent, parent[idx])
	return parent[idx]

def union(parent, idx1, idx2):
	r1 = find(parent, idx1)
	r2 = find(parent, idx2)

	if r1 != r2:
		parent[r2] = r1

for party in arr_party:
	for idx in range(len(party) - 1):
		union(parent, party[idx], party[idx + 1])

know_linker_idx = set()
for idx in range(1, len(arr_know)):
	know_linker_idx.add(find(parent, arr_know[idx]))

result = no_party
for party in arr_party:
	for idx in range(len(party)):
		if find(parent, party[idx]) in know_linker_idx:
			result -= 1
			break
print(result)


# import sys
# from collections import defaultdict, deque
# input = sys.stdin.readline

# def bfs(graph, arr_linked, no_ppl, start):
# 	if arr_linked[start]:
# 		return arr_linked

# 	arr_linked[start] = True
# 	queue = deque([start])

# 	while queue:
# 		curr = queue.popleft()

# 		for neighbor in graph[curr]:
# 			if not arr_linked[neighbor]:
# 				arr_linked[neighbor] = True
# 				queue.append(neighbor)

# 	return arr_linked

# no_ppl, no_party = map(int, input().strip().split(' '))
# arr_know = list(map(int, input().strip().split(' ')))
# arr_party = [list(map(int, input().strip().split(' '))) for _ in range(no_party)]

# graph = defaultdict(list)
# for party in arr_party:
# 	if party[0] == 0 or party[0] == 1:
# 		continue

# 	start = party[1]
# 	rest = party[2:]
# 	for r in rest:
# 		graph[start].append(r)
# 		graph[r].append(start)

# arr_know = arr_know[1:]
# arr_linked = [False for _ in range(no_ppl + 1)]
# for know in arr_know:
# 	arr_linked = bfs(graph, arr_linked, no_ppl, know)

# result = 0
# for party in arr_party:
# 	can_exaggerate = True
# 	for idx in range(1, len(party)):
# 		if arr_linked[party[idx]]:
# 			can_exaggerate = False
# 			break
# 	if can_exaggerate:
# 		result += 1

# print(result)

