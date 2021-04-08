def read_lst(filename):
	with open(filename, "r") as lista:
		return [x.rstrip() for x in lista.readlines()]

def read_lst_backwards(filename):
	with open(filename, "r") as lista:
		return [x.rstrip() for x in lista.readlines()][::-1]

