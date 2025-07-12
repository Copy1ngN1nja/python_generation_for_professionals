def cnt(n, cur=0):
    if n == 0:
        return cur
    else:
        return cnt(n // 10, cur + 1)
    
n = int(input())
print(cnt(n))