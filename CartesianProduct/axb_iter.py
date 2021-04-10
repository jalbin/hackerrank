
import itertools

A = tuple(int(i.strip()) for i in input().split(' '))
B = tuple(int(j.strip()) for j in input().split(' '))

def axb(A,B):
	print(' '.join('({}, {})'.format(*pair) for pair in itertools.product(A,B) ))
axb(A,B)

