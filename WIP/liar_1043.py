import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(graph, arr_linked, no_ppl, start):
	if arr_linked[start]:
		return arr_linked

	arr_linked[start] = True
	queue = deque([start])

	while queue:
		curr = queue.popleft()

		for neighbor in graph[curr]:
			if not arr_linked[neighbor]:
				arr_linked[neighbor] = True
				queue.append(neighbor)

	return arr_linked

no_ppl, no_party = map(int, input().strip().split(' '))
arr_know = list(map(int, input().strip().split(' ')))
arr_party = [list(map(int, input().strip().split(' '))) for _ in range(no_party)]

graph = defaultdict(list)
for party in arr_party:
	if party[0] == 0 or party[0] == 1:
		continue

	start = party[1]
	rest = party[2:]
	for r in rest:
		graph[start].append(r)
		graph[r].append(start)

no_know = arr_know[0]
arr_know = arr_know[1:]
arr_linked = [False for _ in range(no_ppl + 1)]
for know in arr_know:
	arr_linked = bfs(graph, arr_linked, no_ppl, know)

result = 0
for party in arr_party:
	can_exaggerate = True
	for idx in range(1, len(party)):
		if arr_linked[party[idx]]:
			can_exaggerate = False
			break
	if can_exaggerate:
		result += 1

print(result)

