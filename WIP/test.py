HEIGHT = 3
WIDTH = 4
ROOM_A = [[3,3,3,0],
          [3,0,2,1],
          [3,3,3,2]]
WARP = [-1 for _ in range(HEIGHT * WIDTH * 4)]
RANK = [0 for _ in range(HEIGHT * WIDTH * 4)]

start = (2,1,1)

def compute_idx(row, col, d):
    return (row * WIDTH + col) * 4 + d

def find(idx):
    if WARP[idx] != idx:
        WARP[idx] = find(WARP[idx])
    return WARP[idx]

def union(idx1, idx2):
    root1 = find(idx1)
    root2 = find(idx2)
    if root1 != root2:
        if RANK[root1] > RANK[root2]:
            WARP[root2] = root1
        elif RANK[root1] < RANK[root2]:
            WARP[root1] = root2
        else:
            WARP[root2] = root1
            RANK[root1] += 1

def simulate_aris(coord):
    row, col, d = coord

    drow = [-1,0,1,0]
    dcol = [0,1,0,-1]

    start_idx = compute_idx(row,col,d)
    WARP[start_idx] = start_idx
    
    for _ in range(2):
        nd = (d + ROOM_A[row][col]) % 4
        nrow = row + drow[nd]
        ncol = col + dcol[nd]

        if 0 <= nrow < HEIGHT and 0 <= ncol < WIDTH:
            curr_idx = compute_idx(row,col,d)
            next_idx = compute_idx(nrow,ncol,nd)

            if WARP[next_idx] == -1:
                WARP[next_idx] = next_idx

            union(curr_idx, next_idx)

            print((row,col,d), (nrow,ncol,nd))
            print(curr_idx, next_idx)
            print(WARP)
            print('---')

            row, col, d = nrow, ncol, nd
        else:
            break

simulate_aris(start)
# print(WARP)
# print(RANK)
# print('******')
# simulate_aris((1,1,0))
# print(WARP)
# print(RANK)