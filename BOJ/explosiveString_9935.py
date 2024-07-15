import sys
from collections import deque
input = sys.stdin.readline

string = deque(list(input().strip()))
explode = list(input().strip())
stack = []

while string:
	stack.append(string.popleft())

	if stack[-1] == explode[-1]:
		if stack[len(stack) - len(explode):len(stack)] == explode:
			for _ in range(len(explode)):
				stack.pop()

if len(stack) == 0:
	print('FRULA')
else:
	print(''.join(stack))
