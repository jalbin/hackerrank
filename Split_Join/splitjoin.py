a = "this is a string"

def split_and_join(line):
	line = "-".join(line.split(" "))
	return line

print(split_and_join(a))