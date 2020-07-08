n = int(input())
tree = [[]for _ in range(n)]
for i in range(n):
    tree[i].extend(map(int, input().split()))

print(tree)
num = sorted(map(int, input().split()))
print(num)