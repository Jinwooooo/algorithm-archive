import sys
from math import inf
input = sys.stdin.readline

def bellman_ford(arr_edges, no_nodes):
	arr_dist = [inf for _ in range(no_nodes + 1)]
	arr_dist[1] = 0

	for iteration in range(no_nodes):
		for dist, start, end in arr_edges:
			if arr_dist[end] > arr_dist[start] + dist:
				arr_dist[end] = arr_dist[start] + dist
				if iteration == no_nodes - 1:
					return 'YES'

	return 'NO'

arr_result = []
for _ in range(int(input().strip())):
	no_nodes, no_roads, no_warps = map(int, input().strip().split(' '))
	arr_edges = []
	for _ in range(no_roads):
		start, end, dist = map(int, input().strip().split(' '))
		arr_edges.append((dist,start,end))
		arr_edges.append((dist,end,start))
	for _ in range(no_warps):
		start, end, dist = map(int, input().strip().split(' '))
		arr_edges.append((-dist,start,end))

	arr_result.append(bellman_ford(arr_edges, no_nodes))

for r in arr_result:
	print(r)



# import sys
# from math import inf
# from collections import defaultdict
# input = sys.stdin.readline

# def bellman_ford(start, graph, no_nodes):
# 	arr_dist = [inf for _ in range(no_nodes + 1)]
# 	arr_dist[start] = 0

# 	for _ in range(no_nodes):
# 		for curr_node in graph:
# 			for next_dist, next_node in graph[curr_node]:
# 				if arr_dist[next_node] > arr_dist[curr_node] + next_dist:
# 					arr_dist[next_node] = arr_dist[curr_node] + next_dist

# 	for curr_node in graph:
# 		for next_dist, next_node in graph[curr_node]:
# 			if arr_dist[next_node] > arr_dist[curr_node] + next_dist:
# 				return 'YES', arr_dist

# 	return 'NO', arr_dist


# arr_result = []
# for _ in range(int(input().strip())):
# 	no_nodes, no_roads, no_warps = map(int, input().strip().split(' '))
# 	visited = [True] + [False for _ in range(no_nodes)]
# 	graph = defaultdict(list)
# 	for _ in range(no_roads):
# 		start, end, dist = map(int, input().strip().split(' '))
# 		graph[start].append((dist,end))
# 		graph[end].append((dist,start))
# 	for _ in range(no_warps):
# 		start, end, dist = map(int, input().strip().split(' '))
# 		graph[start].append((-dist,end))

# 	idx = 1
# 	while True:
# 		if all(visited):
# 			arr_result.append('NO')
# 			break

# 		result, arr_dist = bellman_ford(idx, graph, no_nodes)
# 		if result == 'YES':
# 			arr_result.append(result)
# 			break
# 		else:
# 			for i in range(1, len(arr_dist)):
# 				if arr_dist[i] != inf:
# 					visited[i] = True

# 		for j in range(1, len(arr_dist)):
# 			if not visited[j]:
# 				idx = j
# 				break

# for r in arr_result:
# 	print(r)