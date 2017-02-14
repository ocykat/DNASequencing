from _Overlap import *
import itertools

# ham tra ve hai doan a, b co doan goi dai nhat va chieu dai doan goi
def pick_maximal_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0
    
    for a, b in itertools.permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    
    return reada, readb, best_olen

# ham greedy_scs
def greedy_scs(reads, k):

    read_a, read_b, olen = pick_maximal_overlap(reads, k)
    # lap cho toi khi khong con bat ki cung nao thi gop tat ca lai
    while olen > 0:
        reads.remove(read_a) # loai bo a
        reads.remove(read_b) # loai bo b
        reads.append(read_a + read_b[olen:]) # cho vao gop cua a va b
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads)

# Thu code
# print greedy_scs(['ABC', 'BCA', 'CAB'], 2)
# KQ dung: CABCA

print greedy_scs(['AACCC', 'CCCTTT', 'TTTGGG'], 2)