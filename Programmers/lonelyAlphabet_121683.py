from collections import defaultdict

def solution(input_string):
    q_input = list(map(str, input_string))
    lonely_dict = defaultdict(list)
    
    prev_elem = ''
    while q_input:
        curr_elem = q_input.pop()
        
        if prev_elem == curr_elem:
            continue
        
        if len(lonely_dict[curr_elem]) == 0:
            lonely_dict[curr_elem] = [1,1]
            prev_elem = curr_elem
        else:
            lonely_dict[curr_elem][0] += 1
            lonely_dict[curr_elem][1] += 1
            prev_elem = curr_elem
    
    result = []
    for dict_elem in lonely_dict:
        if lonely_dict[dict_elem][0] >= 2 and lonely_dict[dict_elem][1] >= 2:
            result.append(dict_elem)
    
    if len(result) == 0:
        result = 'N'
    else:
        result.sort()
        result = ''.join(result)
    
    return result
