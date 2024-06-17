import sys
sys.setrecursionlimit(10**6)

def solution(ability):
    width = len(ability[0])
    height = len(ability)
    
    def dfs(ability, curr_col, all_score, curr_score, visited_row, width, height):
        if curr_col >= width:
            all_score.append(curr_score)
            return
        
        for row in range(height):
            if row not in visited_row:
                visited_row.add(row)
                curr_score += ability[row][curr_col]
                dfs(ability, curr_col + 1, all_score, curr_score, visited_row, width, height)
                curr_score -= ability[row][curr_col]
                visited_row.remove(row)
    
    result = []
    for row in range(height):
        visited_row = set()
        visited_row.add(row)
        all_score = []
        dfs(ability, 1, all_score, ability[row][0], visited_row, width, height)
        result.append(max(all_score))

    return max(result)
