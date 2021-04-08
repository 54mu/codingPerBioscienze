from samus_library import read_lst
import sys

for f in sys.argv[1:]:
	for personaggio in read_lst(f):
		print("ciao {}".format(personaggio))
