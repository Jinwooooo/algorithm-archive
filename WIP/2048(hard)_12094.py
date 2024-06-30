import sys
from collections import deque
input = sys.stdin.readline

SIZE = int(input().strip())
BOARD = [list(map(int, input().strip().split(' '))) for _ in range(SIZE)]
MAX_DEPTH = 10
MEMO = [0 for _ in range(11)]

def up(board):
	for col in range(SIZE):
		deq = deque()

		for row in range(SIZE):
			if board[row][col] != 0:
				deq.append(board[row][col])
				board[row][col] = 0 

		idx = 0
		while len(deq) >= 2:
			curr = deq.popleft()
			nxt = deq.popleft()

			if curr == nxt:
				board[idx][col] = curr * 2
				idx += 1
			else:
				board[idx][col] = curr
				idx += 1
				deq.appendleft(nxt)

		if deq:
			board[idx][col] = deq.popleft()

	return board

def down(board):
	for col in range(SIZE):
		deq = deque()

		for row in range(SIZE-1, -1, -1):
			if board[row][col] != 0:
				deq.append(board[row][col])
				board[row][col] = 0 

		idx = SIZE - 1
		while len(deq) >= 2:
			curr = deq.popleft()
			nxt = deq.popleft()

			if curr == nxt:
				board[idx][col] = curr * 2
				idx -= 1
			else:
				board[idx][col] = curr
				idx -= 1
				deq.appendleft(nxt)

		if deq:
			board[idx][col] = deq.popleft()

	return board

def left(board):
	for row in range(SIZE):
		deq = deque()

		for col in range(SIZE):
			if board[row][col] != 0:
				deq.append(board[row][col])
				board[row][col] = 0

		idx = 0
		while len(deq) >= 2:
			curr = deq.popleft()
			nxt = deq.popleft()

			if curr == nxt:
				board[row][idx] = curr * 2
				idx += 1
			else:
				board[row][idx] = curr
				idx += 1
				deq.appendleft(nxt)

		if deq:
			board[row][idx] = deq.popleft()

	return board

def right(board):
	for row in range(SIZE):
		deq = deque()

		for col in range(SIZE-1, -1, -1):
			if board[row][col] != 0:
				deq.append(board[row][col])
				board[row][col] = 0

		idx = SIZE - 1
		while len(deq) >= 2:
			curr = deq.popleft()
			nxt = deq.popleft()

			if curr == nxt:
				board[row][idx] = curr * 2
				idx -= 1
			else:
				board[row][idx] = curr
				idx -= 1
				deq.appendleft(nxt)

		if deq:
			board[row][idx] = deq.popleft()

	return board

def is_same(board1, board2):
	for row1, row2 in zip(board1, board2):
		if row1 != row2:
			return False
	return True

def dfs(board, depth, max_block):
	max_block = max(max_block, max(max(row) for row in board))

	if max_block > MEMO[depth]:
		MEMO[depth] = max_block

	if max_block <= MEMO[depth] // (2 ** (MAX_DEPTH - depth)):
		return max_block

	if depth == MAX_DEPTH:
		return max_block

	original_board = [row[:] for row in board]

	new_board = up([row[:] for row in original_board])
	if not is_same(original_board, new_board):
		max_block = max(max_block, dfs(new_board, depth + 1, max_block))

	new_board = down([row[:] for row in original_board])
	if not is_same(original_board, new_board):
		max_block = max(max_block, dfs(new_board, depth + 1, max_block))

	new_board = left([row[:] for row in original_board])
	if not is_same(original_board, new_board):
		max_block = max(max_block, dfs(new_board, depth + 1, max_block))

	new_board = right([row[:] for row in original_board])
	if not is_same(original_board, new_board):
		max_block = max(max_block, dfs(new_board, depth + 1, max_block))

	return max_block

print(dfs(BOARD, 0, 0))
