'''
bfs로 모든 정보를 생성하고 index활용하여 추출 시도
4^15 경우의 수 => 시간초과
dfs backtracking 같은 pruning 아님 수학적 공식같은 유형이 필요한 문제
'''
# from collections import deque

# def solution(queries):
#     all_levels = [[] for _ in range(15)]
#     all_levels[0].append(('R','r'))
#     curr_level = 0
    
#     while curr_level < 12:
#         for curr_dna in all_levels[curr_level]:
#             if curr_dna == ('R','r'):
#                 all_levels[curr_level+1].append((curr_dna[0], curr_dna[0]))
#                 all_levels[curr_level+1].append(('R', 'r'))
#                 all_levels[curr_level+1].append(('R', 'r'))
#                 all_levels[curr_level+1].append((curr_dna[1], curr_dna[1]))
#             else:
#                 all_levels[curr_level+1].append((curr_dna[0], curr_dna[0]))
#                 all_levels[curr_level+1].append((curr_dna[0], curr_dna[1]))
#                 all_levels[curr_level+1].append((curr_dna[1], curr_dna[0]))
#                 all_levels[curr_level+1].append((curr_dna[1], curr_dna[1]))
#         curr_level += 1    
    
#     result = []
#     for row, col in queries:
#         result.append(''.join(all_levels[row-1][col-1]))
    
#     return result

def solution(queries):
    def dfs(query):
		row, col = query

		if row == 1:
			return 'Rr'

		col -= 1
		curr_idx = col % 4
		if curr_idx == 0:
			return 'RR'
		if curr_idx == 3:
			return 'rr'

		col += 1
		dfs([row - 1, col // 4])

    result = []
    for query in queries:
        result.append(dfs(query))
    
    return result