from itertools import permutations
from _Overlap import *

# Ham tra ve do thi cac phan goi
def naive_overlap_map(reads, k): # reads: tap hop cac doan goi; k: do dai phan goi toi thieu
    
    olaps = {} # tu dien - do thi
    
    # xet tat ca cac cap (a, b) co the co
    for a,b in permutations(reads, 2):
        # tinh do dai phan goi
        olen = overlap(a, b, min_length = k)
        
        # neu do dai > 0 => them mot cung vao do thi
        if olen > 0:
            olaps[(a, b)] = olen
    return olaps

# Thu code
reads = ['ACGGATGATC', 'GATCAAGT', 'TTCACGGA']
print naive_overlap_map(reads, 3)
# KQ dung: {('ACGGATGATC', 'GATCAAGT'): 4, ('TTCACGGA', 'ACGGATGATC'): 5}