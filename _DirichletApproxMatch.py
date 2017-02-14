from _BoyerMoore import *

# Ham tra ve cac vi tri trong t ma o do p trung lap khong hoan toan
def approximate_match(p, t, n):
	# n: so sai khac toi da giua p va t
	
	segment_length = int(round(len(p)/(n+1))) # do dai mot doan trong (n+1) doan ngan
	all_matches = set() # khoi tao tap hop cac vi tri cua ket qua

	# xet tung doan ngan
	for i in range(n+1):
		
		# vi tri khoi dau mot doan ngan
		start = i*segment_length 
		end = min((i+1)*segment_length, len(p))

		# tim cac vi tri ma doan ngan trung lap hoan toan voi t - dung Boyer-Moore
		p_bm = BoyerMoore(p[start:end], alphabet='ACGT')
		matches = boyer_moore(p[start:end], p_bm, t)

		# voi moi vi tri doan ngan trung lap, kiem tra co thoa yeu cau bai toan
		for m in matches:
			
			# kiem tra p co vuot ra ngoai t hay khong
			if m < start or m - start + len(p) > len(t):
				continue

			mismatches = 0 # khoi tao bien so luong sai khac 
			
			# kiem tra sai khac truoc doan ngan
			for j in range(0, start):
				if p[j] != t[m-start+j]:
					mismatches += 1
					if mismatches > n:
						break

			# kiem tra sai khac sau doan ngan
			for j in range(end, len(p)):
				if p[j] != t[m-start+j]:
					mismatches += 1
					if mismatches > n:
						break

			#kiem tra lan cuoi truoc khi nap vao tap hop ket qua
			if mismatches <= n:
				all_matches.add(m-start)
	
	return list(all_matches)

# Thu code
p = 'AACTTG'
t = 'CACTTAATTTG'
print approximate_match(p, t, 2)
# KQ dung: [0, 5]

