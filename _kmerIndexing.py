import bisect
import sys

class Index(object):
    def __init__(self, t, k): 
        self.k = k
        self.index = []
        
        # lap chi muc va sap xep
        for i in range(len(t) - k + 1):
            self.index.append((t[i:i+k], i)) # mot cap (k-mer, vi tri)
            self.index.sort()

    # ham truy van
    def query(self, p):
        kmer = p[:self.k]
        # tim kiem nhi phan
        i = bisect.bisect_left(self.index, (kmer, -1))
        hits = [] #where the k-mer occurs
        while i<len(self.index):
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

# tim kiem p trong t sau khi tien xu ly t
def queryIndex(p, t, index):
    k = index.k
    offsets = []
    for i in index.query(p):
        if p[k:] == t[(i+k):(i+len(p))]: # kiem tra phan con lai cua p co trung t
            offsets.append(i) # neu co ghi nhan vi tri
    return offsets

# Thu code
t = 'GCTACGATCTAGAATCTA'
p = 'TCTA'
index = Index(t, 2)
print queryIndex(p, t, index)
# KQ dung: [7, 14]