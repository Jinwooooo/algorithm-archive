import sys
from collections import deque
input = sys.stdin.readline

result = []

for _ in range(int(input().strip())):
	cmds = list(map(str, input().strip()))
	size = int(input().strip())
	temp_str = input().strip()[1:-1]
	if temp_str == '':
		arr = deque()
	else:
		arr = deque(map(int, temp_str.split(',')))

	is_reverse = False
	is_error = False

	for cmd in cmds:
		if cmd == 'R':
			is_reverse = not is_reverse
		else:
			if not arr:
				is_error = True
				break

			if is_reverse:
				arr.pop()
			else:
				arr.popleft()

	if is_error:
		result.append('error')
	else:
		if is_reverse:
			arr.reverse()
		result.append('[' + ','.join(map(str, arr)) + ']')

for r in result:
	print(r)

