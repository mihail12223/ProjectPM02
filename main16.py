import math

def C(n, k):
    if k < 0 or k > n:
        return 0 
    res = 1
    for i in range(1, k+1):
        res = res * (n - i + 1) // i
    return res
    
def count(s, n = 12):
    total = 0
    max_k = min(n, s // 10)
    for k in range(max_k+1):
        sign = 1 if k % 2 == 0 else -1
        comb1 = C(n, k)
        comb2 = C(s + n - 1 - 10*k, n - 1)
        total += sign* comb1 * comb2
    return total
    
s = int(input())
print(count(s))