import sys
from math import inf
from collections import defaultdict, deque
input = sys.stdin.readline

result = []

for _ in range(int(input().strip())):
	no_buildings, no_edges = map(int, input().strip().split(' '))
	arr_cost = [0] + list(map(int, input().strip().split(' ')))

	graph = defaultdict(list)
	for _ in range(no_edges):
		start, end = map(int, input().strip().split(' '))
		graph[start].append(end)
	destination = int(input().strip())


for r in result:
	print(r)

