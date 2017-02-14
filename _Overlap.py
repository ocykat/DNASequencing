# Ham tra ve do dai phan goi (>= min_length) giua 2 doan a va b
def overlap(a, b, min_length):
        
    start = 0 # khoi tao bien vi tri tim kiem
    
    while True:
        # tim vi tri cua b trong a, bat dau tu vi tri start
        start = a.find(b[:min_length], start)
        
        # neu khong ton tai phan goi, tra ve so 0
        if start == -1:
            return 0
        
        # kiem tra tien to cua b co phai la hau to cua a
        if b.startswith(a[start:]):
            return len(a) - start
        
        # neu b chua la hau to cua a, tiep tuc tim kiem phan phia sau vi tri vua tim duoc
        start += 1

# Thu code
# print overlap('TTACGT', 'CGTACCGT', 3)
# KQ dung: 3