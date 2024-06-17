"""
finding prime below given value w/ complexity N^(3/2)
-> naive sieve of era (nlog(logn)), which is better, but isn't quite useful exam-like environment
-> with extra steps (i.e like bitmasking and such), it can become with complexity n
	(https://www.geeksforgeeks.org/sieve-eratosthenes-0n-time-complexity/)
"""

def is_prime(val):
	for i in range(2, int(val**(0.5)) + 1):
		if val % i == 0:
			return False

	return True

n = 100
prime = set()
for idx in range(2, n):
	if is_prime(idx):
		prime.add(idx)

print(prime)

