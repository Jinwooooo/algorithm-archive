import sys
from math import inf
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

NO_STUDENTS, NO_ROADS, HOUSE = map(int, input().strip().split(' '))
GO_GRAPH = defaultdict(list)
BACK_GRAPH = defaultdict(list)
for road in range(NO_ROADS):
	start, end, dist = map(int, input().strip().split(' '))
	GO_GRAPH[start].append((dist,end))
	BACK_GRAPH[end].append((dist,start))

def dijkstra(graph, start):
	heap = [(0, start)]
	dist = [inf] + [inf for _ in range(NO_STUDENTS)]
	dist[start] = 0

	while heap:
		curr_dist, curr_house = heappop(heap)

		for next_dist, next_house in graph[curr_house]:
			ddist = curr_dist + next_dist
			if ddist < dist[next_house]:
				dist[next_house] = ddist
				heappush(heap, (ddist, next_house))

	return dist

result = []
go_dist = dijkstra(GO_GRAPH, HOUSE)
back_dist = dijkstra(BACK_GRAPH, HOUSE)
for student in range(1, NO_STUDENTS + 1):
	result.append(go_dist[student] + back_dist[student])

print(max(result))
