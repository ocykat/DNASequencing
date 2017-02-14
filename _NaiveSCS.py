import itertools
from _Overlap import *

# ham tra ve chuoi chung ngan nhat cua cac doan trong tap hop ss
def scs(ss):
    
    shortest_sup = None # khoi tao chuoi chung ngan nhat
    
    # di qua tat ca cac hoan vi cua ss
    for ssperm in itertools.permutations(ss): 
    
        sup = ssperm[0]
        for i in range(len(ss)-1):
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1) # olen: do dai phan goi
            sup += ssperm[i+1][olen:] # ssperm[i+1][olen:]: phan khong bi goi
        
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup
    
    return shortest_sup

# Thu code:
# print scs(['ACGGTACGAGC', 'GAGCTTCGGA', 'GACACGG'])
# KQ dung: 'GACACGGTACGAGCTTCGGA'

print scs(['AACCC', 'CCCTTT', 'TTTGGG'])