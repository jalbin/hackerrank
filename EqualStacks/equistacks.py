import re

s = 'abcde f  g   h'


def solve(s):
	result = [None]*(len(s[::-1].split())+len(list(filter(None, re.split(r"\w",s)))))
	result[::2] = s[::-1].split()
	result[1::2] = list(filter(None, re.split(r"\w",s)))

	return ''.join(result)


print(solve(s))


