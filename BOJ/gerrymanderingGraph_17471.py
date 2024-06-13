import sys
from math import inf
from collections import defaultdict, deque
input = sys.stdin.readline

NO_REGION = int(input().strip())
ARR_POPULATION = [0] + list(map(int, input().strip().split(' ')))
ADJ_DICT = defaultdict(list)
for idx in range(1, NO_REGION + 1):
    ADJ_DICT[idx] = list(map(int, input().strip().split(' ')))[1:]

# logically same as getting all combinations
def dfs(start, arr_curr, arr_out, size_curr):
    if len(arr_curr) == size_curr:
        arr_out.append(arr_curr.copy())
        return arr_out

    for idx in range(start, NO_REGION + 1):
        arr_curr.append(idx)
        arr_out = dfs(idx + 1, arr_curr, arr_out, size_curr)
        arr_curr.pop()

    return arr_out

# logically same as NOT gate (if left is 0, then right must be 1)
def get_r_region_cluster(l_region_cluster):
    r_region_cluster = []

    for l_region in l_region_cluster:
        visited = [True] + [False for _ in range(NO_REGION)]
        r_region = []

        for region in l_region:
            visited[region] = True

        for idx in range(NO_REGION + 1):
            if not visited[idx]:
                r_region.append(idx)

        r_region_cluster.append(r_region)

    return r_region_cluster

# checking for connectivity condition
def bfs(cluster):
    visited = [True] + [False for _ in range(NO_REGION)]
    visited[cluster[0]] = True
    q = deque([cluster[0]])

    while q:
        curr_region = q.popleft()

        for neighbor_region in ADJ_DICT[curr_region]:
            if not visited[neighbor_region] and neighbor_region in cluster:
                q.append(neighbor_region)
                visited[neighbor_region] = True

    for region in cluster:
        if not visited[region]:
            return False
    
    return True

def get_population_difference(l_region, r_region):
    l_population, r_population = 0, 0

    for l in l_region:
        l_population += ARR_POPULATION[l]

    for r in r_region:
        r_population += ARR_POPULATION[r]

    return abs(l_population - r_population)

# getting left and right region cluster combinations
l_region_cluster = []
for size in range(1, NO_REGION//2 + 1):
    l_region_cluster.extend(dfs(1, [], [], size))
r_region_cluster = get_r_region_cluster(l_region_cluster)

# checking connectivity and if no issue, compute population difference
global_min = inf
for idx in range(len(l_region_cluster)):
    if bfs(l_region_cluster[idx]) and bfs(r_region_cluster[idx]):
        global_min = min(global_min, get_population_difference(l_region_cluster[idx], r_region_cluster[idx]))

# output BOJ format
if global_min == inf:
    print(-1)
else:
    print(global_min)



# import sys
# from math import inf
# from itertools import combinations
# from collections import deque, defaultdict
# input = sys.stdin.readline

# # gets all possible tuples (some repetitions are included)
# def get_combo(arr_nodes):
# 	all_combo = set()
# 	for size in range(1, len(arr_nodes)//2 + 1):
# 		l_combo = list(sorted(combinations(arr_nodes, size)))
# 		r_combo = list(sorted(combinations(arr_nodes, len(arr_nodes) - size)))
# 		for l_tuple in l_combo:
# 			for r_tuple in r_combo:
# 				if not (set(l_tuple) & set(r_tuple)):
# 					all_combo.add((l_tuple, r_tuple))

# 	return all_combo

# # removes all repeated tuples
# # e.g. ((2,3),(1,4)) and ((1,4),(2,3)) are treated the same
# def ai_get_combo(arr_nodes):
#     set_combo = set()

#     for size in range(1, len(arr_nodes)):
#         for subset in combinations(arr_nodes, size):
#             remain = tuple(sorted(set(arr_nodes) - set(subset)))
#             combo = (tuple(sorted(subset)), remain)
#             sort_combo = tuple(sorted(combo))
#             set_combo.add(sort_combo)

#     return set_combo

# def bfs_region(adj_list, arr_population, arr_cluster, no_nodes):
# 	arr_visited = [True] + [False for _ in range(no_nodes)]
# 	arr_visited[arr_cluster[0]] = True
# 	queue = deque([arr_cluster[0]])

# 	while queue:
# 		curr_node = queue.popleft()

# 		for neighbor_node in adj_list[curr_node]:
# 			if not arr_visited[neighbor_node] and neighbor_node in arr_cluster:
# 				arr_visited[neighbor_node] = True
# 				queue.append(neighbor_node)

# 	cluster_population = -1
# 	if all([arr_visited[idx] for idx in arr_cluster]):
# 		cluster_population = sum(arr_population[idx] for idx in arr_cluster)

# 	return cluster_population


# # input variables
# no_nodes = int(input().strip())
# arr_population = [-1] + list(map(int, input().strip().split(' ')))
# adj_list = defaultdict(set)
# for node_1 in range(1, no_nodes + 1):
# 	arr_node_2 = list(map(int, input().strip().split(' ')))[1:]
# 	for node_2 in arr_node_2:
# 		adj_list[node_1].add(node_2)
# 		adj_list[node_2].add(node_1)

# # self variables
# arr_combo = list(get_combo([k for k in range(1, no_nodes + 1)]))
# global_min = inf

# for curr_combo in arr_combo:
# 	cluster_1 = bfs_region(adj_list, arr_population, curr_combo[0], no_nodes)
# 	cluster_2 = bfs_region(adj_list, arr_population, curr_combo[1], no_nodes)

# 	if cluster_1 > 0 and cluster_2 > 0:
# 		global_min = min(global_min, abs(cluster_1 - cluster_2))

# if global_min == inf:
# 	print('-1')
# else:
# 	print(global_min)


