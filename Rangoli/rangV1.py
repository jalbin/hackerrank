
def print_rangoli(size):
	
	print("\n".join([ '-'.join((size-i)*['-'] + [chr(x) for x in range(97+(size-i),97+size)][::-1] + [chr(x) for x in range(97+(size-i),97+size)][1::] + (size-i)*['-']) for i in range(1,size+1) ] + ['-'.join(j*['-'] + [chr(y) for y in range(97+j,97+size)][::-1] + [chr(y) for y in range(97+j,97+size)][1::] + j*['-']) for j in range(1,size) ]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)