


A = tuple(int(i.strip()) for i in input().split(' '))
B = tuple(int(j.strip()) for j in input().split(' '))


def axb(A,B):
	# print [(x,y) for x in A  for y in B ]
	print(' '.join('({}, {})'.format(*pair) for pair in [(x,y) for x in A  for y in B ]))

axb(A,B)