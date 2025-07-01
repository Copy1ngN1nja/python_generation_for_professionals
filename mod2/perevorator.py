n, x, y, a, b = map(int, input().split())

vec = [i for i in range(1, n + 1)]
vec[x-1:y] = vec[x-1:y][::-1]
vec[a-1:b] = vec[a-1:b][::-1]
print(*vec)