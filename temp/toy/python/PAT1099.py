n = int(input())
tree = [[]for _ in range(n)]
for i in range(n):
    tree[i].extend(map(int, input().split()))


num = sorted(map(int, input().split()))
lev, cur = [0], [0]
while cur:
    chd = [y for x in cur for y in tree[x] if y != -1]
    if chd:
        lev.extend(chd)
    cur = chd
print(lev)