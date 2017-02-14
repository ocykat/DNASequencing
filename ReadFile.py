#Fasta format
def ReadFasta(filename):
	genome = ''
	with open(filename, 'r') as f:
		for line in f:
			if line[0] != '>':
				genome += line.rstrip()
	return genome

#Fastq format
def ReadFastq(filename):
	sequences = []
	qualities = []
	with open(filename) as fh:
		while True:
			fh.readline() #1st line
			seq = fh.readline().rstrip() #2nd line
			fh.readline() #3rd line
			qual = fh.readline().rstrip() #4th line
			if len(seq) == 0:
				break
			sequences.append(seq)
			qualities.append(qual)
	return sequences, qualities

def Phred33ToQ(qual):
	return ord(qual) - 33