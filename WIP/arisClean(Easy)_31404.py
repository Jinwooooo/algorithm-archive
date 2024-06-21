# import sys
# input = sys.stdin.readline

# HEIGHT, WIDTH = map(int, input().strip().split(' '))
# INIT_ARIS_DATA = list(map(int, input().strip().split(' ')))
# ROOM_A = [list(map(int, input().strip())) for _ in range(HEIGHT)]
# ROOM_B = [list(map(int, input().strip())) for _ in range(HEIGHT)]
# CLEAN = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

# def simulate_aris():
#     curr_move = 0
#     final_move = 0
#     cycle_tracker = set()
#     row, col, d = INIT_ARIS_DATA

#     drow = [-1,0,1,0]
#     dcol = [0,1,0,-1]
    
#     while True:
#         if not CLEAN[row][col]:
#             nd = (d + ROOM_A[row][col]) % 4
#         else:
#             nd = (d + ROOM_B[row][col]) % 4

#         nrow = row + drow[nd]
#         ncol = col + dcol[nd]

#         if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
#             curr_move += 1

#             if not CLEAN[row][col]:
#                 final_move = curr_move
#                 CLEAN[row][col] = True
#                 cycle_tracker.clear()
#             else:
#                 if (nrow, ncol, nd) in cycle_tracker:
#                     break
            
#             cycle_tracker.add((nrow,ncol,nd))
#             row, col, d = nrow, ncol, nd
#         else:
#             if not CLEAN[row][col]:
#                 curr_move += 1
#                 final_move = curr_move
#             break

#     return final_move

# print(simulate_aris())


import sys
input = sys.stdin.readline

HEIGHT, WIDTH = map(int, input().strip().split(' '))
INIT_ARIS_DATA = list(map(int, input().strip().split(' ')))
ROOM_A = [list(map(int, input().strip())) for _ in range(HEIGHT)]
ROOM_B = [list(map(int, input().strip())) for _ in range(HEIGHT)]
CLEAN = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

def simulate_aris():
    curr_move = 0
    final_move = 0
    clear_ctr = 0
    cycle_tracker = [[[0 for _ in range(4)] for _ in range(WIDTH)] for _ in range(HEIGHT)]
    row, col, d = INIT_ARIS_DATA

    drow = [-1,0,1,0]
    dcol = [0,1,0,-1]
    
    while True:
        if not CLEAN[row][col]:
            nd = (d + ROOM_A[row][col]) % 4
        else:
            nd = (d + ROOM_B[row][col]) % 4

        nrow = row + drow[nd]
        ncol = col + dcol[nd]

        if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
            curr_move += 1

            if not CLEAN[row][col]:
                final_move = curr_move
                CLEAN[row][col] = True
                clear_ctr += 1
            else:
                if cycle_tracker[row][col][nd] == clear_ctr:
                    break
            
            cycle_tracker[row][col][nd] = clear_ctr
            row, col, d = nrow, ncol, nd
        else:
            if not CLEAN[row][col]:
                curr_move += 1
                final_move = curr_move
            break

    return final_move

print(simulate_aris())

# import sys
# input = sys.stdin.readline

# HEIGHT, WIDTH = map(int, input().strip().split(' '))
# INIT_ARIS_DATA = list(map(int, input().strip().split(' ')))
# ROOM_A = [list(map(int, input().strip())) for _ in range(HEIGHT)]
# ROOM_B = [list(map(int, input().strip())) for _ in range(HEIGHT)]
# CLEAN = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

# def simulate_aris():
#     curr_move = 0
#     final_move = 0
#     prev_state = (-1,-1,-1)
#     row, col, d = INIT_ARIS_DATA

#     drow = [-1,0,1,0]
#     dcol = [0,1,0,-1]
    
#     while True:
#         if not CLEAN[row][col]:
#             nd = (d + ROOM_A[row][col]) % 4
#         else:
#             nd = (d + ROOM_B[row][col]) % 4

#         nrow = row + drow[nd]
#         ncol = col + dcol[nd]

#         if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
#             curr_move += 1

#             if not CLEAN[row][col]:
#                 prev_state = (row,col,nd)
#                 final_move = curr_move
#                 CLEAN[row][col] = True
#             else:
#                 if prev_state == (row,col,nd):
#                     break
            
#             row, col, d = nrow, ncol, nd
#         else:
#             if not CLEAN[row][col]:
#                 curr_move += 1
#                 final_move = curr_move
#             break

#     return final_move

# print(simulate_aris())

