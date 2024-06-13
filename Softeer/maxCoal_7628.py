import sys
input = sys.stdin.readline

_ = int(input().strip())
arr_house_size = tuple(map(int, input().strip().split(' ')))

global_max_ctr = 0

for coal_size in range(2, 101):
    max_ctr = 0
    for house_size in arr_house_size:
        if house_size % coal_size == 0:
            max_ctr += 1
    global_max_ctr = max(global_max_ctr, max_ctr)

print(global_max_ctr)
