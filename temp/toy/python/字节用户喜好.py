import bisect

N = int(input())
L = [[] for i in range(0, 300050)]

index = [int(i) for i in input().split()]

num = 1;
for i in range(0, N):
    L[index[i]].append(num)
    num = num + 1;

Q = int(input())
for i in range(Q):
    a, b, c = map(int, input().strip().split())

    i1 = bisect.bisect_left(L[c], a)
    i2 = bisect.bisect_right(L[c], b)

    print(i2 - i1)