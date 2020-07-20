import bisect

N = int(input())
L = [[] for i in range(0, 6)]
index = list(map(int, input().split()))

num = 1
for i in range(N):
    L[index[i]].append(num)
    num += 1

Q = int(input())

for _ in range(Q):
    a, b, c = map(int, input().split())
    du1 = bisect.bisect_left(L[c], a)
    du2 = bisect.bisect_right(L[c], b)
    print(du2 - du1)
