n = int(input())
tree = [[]for _ in range(n)]
for i in range(n):
    tree[i].extend(map(int, input().split()))

num = sorted(map(int, input().split()))

inord = []

def inorder(root):
    if root != -1:
        inorder(tree[root][0])
        inord.append(root)
        inorder(tree[root][1])


lev, cur = [0], [0]
while cur:
    chd = [y for x in cur for y in tree[x] if y != -1]
    if chd:
        lev.extend(chd)
    cur = chd

inorder(0)
# print(lev)
# print(inord)

res = [0] * n
for i in range(n):
    res[inord[i]] = num[i]

ans = [res[x] for x in lev]

print(num)
# sorted
print(res)
print(inord)
# inorder
print(lev)
# level sort/order
print(ans)

print(' '.join(map(str, ans)))