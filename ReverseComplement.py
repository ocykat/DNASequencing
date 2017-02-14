complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'} #dictionary

def RC(s):
	t = ''
	for base in s:
		t = complement[base] + t
	return t